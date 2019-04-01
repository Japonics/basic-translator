import re

from expressions import EXPRESSIONS

SINGLE_OPERATOR_REGEX = "\+|\-|\*|\/|\(|\)|\-{1}"
INTEGER_NUMBERS_REGEX = "([\d]+)"
FLOAT_NUMBERS_REGEX = "(([0-9]{1,})\.([0-9]{1,}))"
VARIABLES_REGEX = "(([a-zA-Z]{1,})([a-zA-Z0-9]{1,}))|([a-zA-Z]{1,})"

GENERAL_REGEX = "((-?(?:\d+(?:\.\d+)?))|(\+|\-|\*|\/|\(|\)|\-{1})|(([a-zA-Z]{1,})([a-zA-Z0-9]{1,}))|([a-zA-Z]{1,})|([-+\/*()])|(-?\d+))"


class LexicalInterpreterRegex:

    def __init__(self, word_to_analyze):
        self.word = word_to_analyze
        self.regex_expressions = [
            GENERAL_REGEX
        ]
        self.tokens = {}

    def analyze(self):
        for regex_expression in self.regex_expressions:
            regex_matcher = re.compile(regex_expression)
            for match_result in regex_matcher.finditer(self.word):
                self.tokens[match_result.start()] = match_result.group()

        sorted_tokens = sorted(self.tokens)
        tokens_result = []
        for position in sorted_tokens:
            tokens_result.append(self.tokens[position])

        return tokens_result


if __name__ == '__main__':
    to_analyze = EXPRESSIONS

    for word in to_analyze:

        print("Word to analyze: {}".format(word))

        interpreter = LexicalInterpreterRegex(word)
        tokens = interpreter.analyze()
        for token in tokens:
            print(token)
