from typing import List
from lexical.token_word import TokenWord, TokenWordTypes


class SyntacticInterpreter:

    def __init__(self, tokens: List[TokenWord]):
        self.tokens = tokens

    def start(self):
        try:
            self.is_w(self.tokens)
        except Exception as e:
            print("Error {0}".format(str(e)))

    def is_w(self, tokens: List[TokenWord]):
        # W = W + S
        # W = W - S
        # W = S

        index = self.find_token_and_get_index("+", TokenWordTypes.OPERATOR, tokens)
        if index is not None:
            if self.is_w(tokens[0:index]) and self.is_s(tokens[:index:]):
                print("W = W + S")
                return True

        index = self.find_token_and_get_index("-", TokenWordTypes.OPERATOR, tokens)
        if index is not None:
            if self.is_w(tokens[0:index:]) and self.is_s(tokens[:index:]):
                print("W = W - S")
                return True

        if self.is_s(tokens):
            print("W = S")
            return True

        raise Exception("Wrong tokens is_w")

    def is_s(self, tokens: List[TokenWord]):
        # S = S * C
        # S = S / C
        # S = C

        index = self.find_token_and_get_index("*", TokenWordTypes.OPERATOR, tokens)
        if index is not None:
            if self.is_s(tokens[0:index]) and self.is_c(tokens[:index:]):
                return True

        index = self.find_token_and_get_index("/", TokenWordTypes.OPERATOR, tokens)
        if index is not None:
            if self.is_s(tokens[0:index]) and self.is_c(tokens[:index:]):
                return True

        if self.is_c(tokens):
            return True

        raise Exception("Wrong tokens is_s")


    def is_c(self, tokens: List[TokenWord]):
        # C = liczba
        # C = identyfikator
        # C = (W)

        if len(tokens) == 1:
            c_token = tokens[0]
            if c_token.type == TokenWordTypes.VARIABLE:
                return True
            if c_token.type == TokenWordTypes.OPERATOR:
                return True
            if c_token.type == TokenWordTypes.NUMBER:
                return True
            if c_token.type == TokenWordTypes.FLOAT:
                return True
            if c_token.type == TokenWordTypes.INTEGER:
                return True

        if tokens[0].token == "(" and tokens[-1].token == ")" and self.is_w(tokens[1::-2]):
            return True

        raise Exception("Wrong tokens is_c")

    def find_token_and_get_index(self, token_value: str, token_type: TokenWordTypes, tokens: List[TokenWord]):
        for index in range(0, len(tokens)):
            token = tokens[index]
            if token.token == token_value and token.type == token_type:
                return index

        return None
