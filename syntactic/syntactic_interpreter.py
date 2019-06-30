from typing import List
from lexical.token_word import TokenWord, TokenWordTypes


class SyntacticInterpreter:

    def __init__(self, tokens: List[TokenWord]):
        self.tokens = tokens

    def start(self):
        try:
            self.is_w(self.tokens, True)
        except Exception as e:
            print("Error {0}".format(str(e)))

    def is_w(self, tokens: List[TokenWord], first: bool = False):
        # W = W + S
        # W = W - S
        # W = S

        try:
            close_parenthesis_index = self.find_token_and_get_index(")", TokenWordTypes.PARENTHESIS, tokens)
            if close_parenthesis_index is None:
                close_parenthesis_index = 0

            index = self.find_token_and_get_index("+", TokenWordTypes.OPERATOR, tokens, close_parenthesis_index)
            if index is not None:
                if self.is_w(tokens[0:index]) and self.is_s(tokens[:index:-1]):
                    if first:
                        print("W = W + S")
                        print("W => {}".format(self.join_tokens(tokens[0:index:])))
                        print("S => {}".format(self.join_tokens(tokens[:index:-1])))
                    return True

            index = self.find_token_and_get_index("-", TokenWordTypes.OPERATOR, tokens, close_parenthesis_index)
            if index is not None:
                if self.is_w(tokens[0:index:]) and self.is_s(tokens[:index:-1]):
                    if first:
                        print("W = W - S")
                        print("W => {}".format(self.join_tokens(tokens[0:index])))
                        print("S => {}".format(self.join_tokens(tokens[:index:-1])))
                    return True

            if self.is_s(tokens):
                if first:
                    print("W = S")
                    print("S => {}".format(self.join_tokens(tokens)))
                return True
        except IndexError:
            raise Exception("Wrong tokens: {}".format(self.join_tokens(tokens)))

        raise Exception("Wrong tokens: {}".format(self.join_tokens(tokens)))

    def is_s(self, tokens: List[TokenWord]):
        # S = S * C
        # S = S / C
        # S = C

        try:
            close_parenthesis_index = self.find_token_and_get_index(")", TokenWordTypes.PARENTHESIS, tokens)
            if close_parenthesis_index is None:
                close_parenthesis_index = 0

            index = self.find_token_and_get_index("*", TokenWordTypes.OPERATOR, tokens, close_parenthesis_index)
            if index is not None:
                if self.is_s(tokens[0:index]) and self.is_c(tokens[:index:]):
                    return True
                elif self.is_c(tokens[0:index]) and self.is_s(tokens[:index:]):
                    return True

            index = self.find_token_and_get_index("/", TokenWordTypes.OPERATOR, tokens, close_parenthesis_index)
            if index is not None:
                if self.is_s(tokens[0:index]) and self.is_c(tokens[:index:-1]):
                    return True
                elif self.is_c(tokens[0:index]) and self.is_s(tokens[:index:]):
                    return True

            if self.is_c(tokens):
                return True
        except IndexError:
            raise Exception("Wrong tokens: {}".format(self.join_tokens(tokens)))

        raise Exception("Wrong tokens: {}".format(self.join_tokens(tokens)))

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

        raise Exception("Wrong tokens: {}".format(self.join_tokens(tokens)))

    def find_token_and_get_index(self, token_value: str, token_type: TokenWordTypes, tokens: List[TokenWord], from_pos: int = 0):
        for index in range(from_pos, len(tokens)):
            token = tokens[index]
            if token.token == token_value and token.type == token_type:
                return index

        return None

    def join_tokens(self, tokens: List[TokenWord]) -> str:
        result = ""
        for token in tokens:
            result = result + " " + token.token
        return result