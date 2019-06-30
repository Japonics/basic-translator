from expressions import EXPRESSIONS
from lexical.lexical_interpreter_regex import LexicalInterpreterRegex
from syntactic.syntactic_interpreter import SyntacticInterpreter


class Translator:
    def __init__(self):
        self.to_analyze = EXPRESSIONS

    def run_interpreter(self):
        for word in self.to_analyze:

            lexer = LexicalInterpreterRegex(word)
            tokens = lexer.analyze()

            if tokens is None:
                continue

            print("")
            print("")
            print("")
            print("PROCESSING WORD")
            print("WORD: {}".format(word))
            # print("TOKENS: {}".format(tokens))
            syntactic = SyntacticInterpreter(tokens)
            syntactic.start()


if __name__ == '__main__':
    translator = Translator()
    print("########## START PROGRAM ##########")
    translator.run_interpreter()
    print("########## FINISHED ##########")
