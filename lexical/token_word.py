from enum import Enum


class TokenWordTypes(Enum):
    OPERATOR = "OPERATOR"
    PARENTHESIS = "PARENTHESIS"
    NUMBER = "NUMBER"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    VARIABLE = "VARIABLE"


class TokenWord(object):

    def __init__(self, word: str, word_type: TokenWordTypes):
        self.token = word
        self.type = word_type


