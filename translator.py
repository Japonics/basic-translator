class Translator:
    def __init__(self):
        self.to_analyze = [
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

    def run_lexical_interpreter_simple(self):
        for word in self.to_analyze:
            interpreter = LexicalInterpreterSimple(word)
            tokens = interpreter.analyze()
            if tokens is not None:
                for token in tokens:
                    print(token)


if __name__ == 'main':
    translator = Translator()
    translator.run_lexical_interpreter_simple()
