from expressions import EXPRESSIONS
from lexical.lexical_interpreter_simple import LexicalInterpreterSimple
from lexical.lexical_interpreter_regex import LexicalInterpreterRegex


class Translator:
    def __init__(self):
        self.to_analyze = EXPRESSIONS

    def run_lexical_interpreter_simple(self):
        for word in self.to_analyze:
            print("Analyze word: {}".format(word))
            interpreter = LexicalInterpreterSimple(word)
            tokens = interpreter.analyze()
            if tokens is not None:
                for token in tokens:
                    print(token)
            print("")

    def run_lexical_interpreter_regex(self):
        for word in self.to_analyze:
            interpreter = LexicalInterpreterRegex(word)
            tokens = interpreter.analyze()
            if tokens is not None:
                for token in tokens:
                    print(token)


if __name__ == '__main__':
    translator = Translator()
    # translator.run_lexical_interpreter_simple()
    translator.run_lexical_interpreter_regex()
