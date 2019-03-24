class LexicalInterpreterSimple:

    single_tokens = ['+', '-', '*', '/', '(', ')']
    float_notation = '.'

    def __init__(self, word_to_analyze):
        self.word = word_to_analyze
        self.tokens = []
        self.current_token = None
        self.last_symbol = None

    def analyze(self):

        for symbol in self.word:

            # Check that symbol is single letter word
            if symbol in LexicalInterpreterSimple.single_tokens:
                self.tokens.append(symbol)
                self.last_symbol = None
                self.current_token = None
                continue

            if str(symbol).isspace():
                self.last_symbol = None
                if self.current_token is not None:
                    self.tokens.append(self.current_token)
                self.current_token = None
                continue

            if self.last_symbol is None:
                self.last_symbol = symbol
                self.current_token = "{}".format(symbol)
                continue
            else:
                if str(symbol).isnumeric():
                    self.last_symbol = symbol
                    self.current_token = "{}{}".format(self.current_token, symbol)
                    continue
                else:
                    if str(self.last_symbol).isnumeric():
                        raise Exception("Lexical error")
                    else:
                        self.last_symbol = symbol
                        self.current_token = "{}{}".format(self.current_token, symbol)
                        continue

        return self.tokens


if __name__ == 'main':
    to_analyze = [
        '12 3x+2.5',
        '3 7',
        'x12+7.5',
        '3-7',
        '10 / 3',
        'x * y - z',
        'zmienna1 + zmienna2',
        'w1a*w2b',
        '10.3-alfa',
        '0.685739*5',
        '(x+y)*z',
        '(x+y)*z',
        '(a * a) + b',
        '(0.1 - beta) + 8v',
    ]
    for word in to_analyze:

        print("Word to analyze: {}".format(word))

        interpreter = LexicalInterpreterSimple(word)
        tokens = interpreter.analyze()
        for token in tokens:
            print(token)

