class Expr: pass


# a
class Chr(Expr):

    non_character_error_description = "Character should have length one"

    def __init__(self, character):
        if len(character) != 1:
            raise ValueError(Chr.non_character_error_description)
        self.character = character

    def __eq__(self, other):
        if isinstance(other, Chr):
            return other.character == self.character
        else:
            return False

# A ^ B ó A _ B
class BinOp(Expr): pass


# A B
class Concat(Expr):
    def __init__(self, leftExpression, rightExpression):
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression


# ()
class GroupedPar(Expr): pass


# {}
class GroupedBrkt(Expr): pass
