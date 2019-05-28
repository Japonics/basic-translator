import re
from typing import Dict

from expressions import EXPRESSIONS
from lexical.token_word import TokenWord, TokenWordTypes

SINGLE_OPERATOR_REGEX = "\+|\-|\*|\/|\-{1}"
PARENTHESIS_OPERATOR_REGEX = "\(|\){1}"
INTEGER_NUMBERS_REGEX = "([\d]+)"
FLOAT_NUMBERS_REGEX = "(([0-9]{1,})\.([0-9]{1,}))"
VARIABLES_REGEX = "(([a-zA-Z]{1,})([a-zA-Z0-9]{1,}))|([a-zA-Z]{1,})"

INVALID_EXPRESSIONS_REGEX = [
    "[^a-zA-Z0-9\*\+\-\(\)\/\. ]{1}",
    "(([a-zA-Z0-9]{1,})\.([a-zA-Z0-9]{1,})\.([a-zA-Z0-9]{1,}))",
    "([\.]{2,})",
    "(\+|\-|\*|\/|\-){2,}"
]

GENERAL_REGEX = "(((?:\d+(?:\.\d+)?))|(\+|\-|\*|\/|\(|\)|\-{1})|(([a-zA-Z]{1,})([a-zA-Z0-9]{1,}))|([a-zA-Z]{1,})|([-+\/*()])|(-?\d+))"


class LexicalInterpreterRegex:

    def __init__(self, word_to_analyze):
        self.word = word_to_analyze
        self.regex_expressions = [
            GENERAL_REGEX
        ]
        self.tokens: Dict[int, TokenWord] = {}

    def analyze(self):
        for invalid_expression_regex in INVALID_EXPRESSIONS_REGEX:
            invalid_expression = re.compile(invalid_expression_regex)
            for invalid_char in invalid_expression.finditer(self.word):
                print("Invalid expression: {} at {} position".format(self.word, invalid_char.start()))
                self.word = "{}{}".format(str(self.word)[:invalid_char.start()], str(self.word)[invalid_char.end():])

        for regex_expression in self.regex_expressions:
            regex_matcher = re.compile(regex_expression)
            for match_result in regex_matcher.finditer(self.word):
                self.tokens[match_result.start()] = LexicalInterpreterRegex.create_token(match_result.group())

        sorted_tokens = sorted(self.tokens)
        tokens_result = []
        for position in sorted_tokens:
            tokens_result.append(self.tokens[position])

        return tokens_result

    @staticmethod
    def create_token(token_value: str) -> TokenWord:

        if re.compile(SINGLE_OPERATOR_REGEX).match(token_value):
            return TokenWord(token_value, TokenWordTypes.OPERATOR)
        if re.compile(PARENTHESIS_OPERATOR_REGEX).match(token_value):
            return TokenWord(token_value, TokenWordTypes.PARENTHESIS)
        if re.compile(FLOAT_NUMBERS_REGEX).match(token_value):
            return TokenWord(token_value, TokenWordTypes.FLOAT)
        if re.compile(INTEGER_NUMBERS_REGEX).match(token_value):
            return TokenWord(token_value, TokenWordTypes.INTEGER)
        if re.compile(VARIABLES_REGEX).match(token_value):
            return TokenWord(token_value, TokenWordTypes.VARIABLE)

        raise Exception("Unknown token")


if __name__ == '__main__':
    to_analyze = EXPRESSIONS

    for word in to_analyze:

        print()
        print("Word to analyze: {}".format(word))

        interpreter = LexicalInterpreterRegex(word)
        tokens = interpreter.analyze()
        for token in tokens:
            print("{} is {}".format(token.token, token.type))
