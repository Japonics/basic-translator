import re

from expressions import EXPRESSIONS

SINGLE_OPERATOR_REGEX = "\+|\-|\*|\/|\(|\)|\-{1}"

# TODO
# add regex for variable
# add regex for number


class LexicalInterpreterRegex:

    def __init__(self, word_to_analyze):
        self.word = word_to_analyze
        self.regex_expressions = [
            SINGLE_OPERATOR_REGEX
        ]
        self.tokens = {}

    def analyze(self):
        for regex_expression in self.regex_expressions:
            regex_matcher = re.compile(regex_expression)
            for match_result in regex_matcher.finditer(self.word):
                self.tokens[match_result.start()] = match_result.group()
        print(self.tokens)
        return []


if __name__ == '__main__':
    to_analyze = EXPRESSIONS

    for word in to_analyze:

        print("Word to analyze: {}".format(word))

        interpreter = LexicalInterpreterRegex(word)
        tokens = interpreter.analyze()
        for token in tokens:
            print(token)
