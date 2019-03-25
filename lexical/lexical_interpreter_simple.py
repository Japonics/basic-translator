from expressions import EXPRESSIONS


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

            # Check that symbol is single letter word:
            # - save current token, append symbol as token, reset last symbol and current token
            if symbol in LexicalInterpreterSimple.single_tokens:
                if self.current_token is not None:
                    self.tokens.append(self.current_token)
                self.tokens.append(symbol)
                self.last_symbol = None
                self.current_token = None
                continue

            # Check that symbol is space:
            # - save current token and reset last symbol and current token
            if str(symbol).isspace():
                if self.current_token is not None:
                    self.tokens.append(self.current_token)

                self.last_symbol = None
                self.current_token = None
                continue

            # Check that last symbol is set
            # - update last symbol, start creating current token
            if self.last_symbol is None:
                self.last_symbol = symbol
                self.current_token = "{}".format(symbol)
                continue

            # Check if symbol is numeric
            # - update last symbol and append symbol to current token
            # Info: cause number can be appended after letter and other number
            if str(symbol).isnumeric():
                self.last_symbol = symbol
                self.current_token = "{}{}".format(self.current_token, symbol)
                continue

            # Check if symbol is float notation
            # - check that last symbol is numeric and append notation if not appear
            # in current token already (e.g 10.100.22 => 10100.22)
            elif str(symbol) is LexicalInterpreterSimple.float_notation:
                if str(self.last_symbol).isnumeric():
                    if LexicalInterpreterSimple.float_notation in self.current_token:
                        self.current_token = self.current_token.replace('.', '')
                    self.current_token = "{}{}".format(self.current_token, symbol)
                    self.last_symbol = symbol
                    continue

            # Check if symbol is letter
            # - depends on last symbol decide that symbol should be part of current token
            # or should end current token
            else:
                if str(self.last_symbol).isnumeric():
                    if self.current_token is not None:
                        if not self.current_token.isnumeric():
                            self.current_token = "{}{}".format(self.current_token, symbol)
                            continue
                        else:
                            self.tokens.append(self.current_token)
                            self.last_symbol = symbol
                            self.current_token = "{}".format(symbol)
                            continue
                    else:
                        self.last_symbol = symbol
                        self.current_token = "{}".format(symbol)
                        continue
                else:
                    self.last_symbol = symbol
                    self.current_token = "{}{}".format(self.current_token, symbol)
                    continue

        # If current token is set then add to tokens
        if self.current_token is not None:
            self.tokens.append(self.current_token)

        return self.tokens


if __name__ == '__main__':
    to_analyze = EXPRESSIONS

    for word in to_analyze:

        print("Word to analyze: {}".format(word))

        interpreter = LexicalInterpreterSimple(word)
        tokens = interpreter.analyze()
        for token in tokens:
            print(token)

