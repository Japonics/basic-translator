import re

from expressions import EXPRESSIONS

INVALID_EXPRESSIONS_REGEX = [
    "[^a-zA-Z0-9\*\+\-\(\)\/\. ]{1}",
    "(([a-zA-Z0-9]{1,})\.([a-zA-Z0-9]{1,})\.([a-zA-Z0-9]{1,}))",
    "([\.]{2,})"
]

GENERAL_REGEX = "(((?:\d+(?:\.\d+)?))|(\+|\-|\*|\/|\(|\)|\-{1})|(([a-zA-Z]{1,})([a-zA-Z0-9]{1,}))|([a-zA-Z]{1,})|([-+\/*()])|(-?\d+))"


class LexicalInterpreterRegex:

    def __init__(self, word_to_analyze):
        self.word = word_to_analyze
        self.regex_expressions = [
            GENERAL_REGEX
        ]
        self.tokens = {}

    def analyze(self):
        for invalid_expression_regex in INVALID_EXPRESSIONS_REGEX:
            invalid_expression = re.compile(invalid_expression_regex)
            for invalid_char in invalid_expression.finditer(self.word):
                print("Invalid expression: {} at {} position".format(self.word, invalid_char.start()))
                self.word = "".format(str(self.word)[:invalid_char.start()], str(self.word)[invalid_char.end():])
                print(self.word)

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
        if tokens is not None:
            for token in tokens:
                print(token)

