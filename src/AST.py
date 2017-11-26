class Expr:

    def evaluate(self):
        raise NotImplementedError


class Start(Expr):

    def __init__(self, child):
        self.child = child

    def evaluate(self):
        res = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"200\" height=\"100\" version=\"1.1\"><g transform=\"scale(40) translate(0, .62)\" font-family=\"Courier\">"
        res += self.child.evaluate()
        res += "</g></svg>"
        return res

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

    def evaluate(self):
        res = "<text x=\".69\" y=\".53\" font-size=\"1\">"
        res += self.character;
        res += "</text>"
        return res

# A ^ B ó A _ B
class BinOp(Expr):

    def evaluate(self):
        return ""


# A B
class Concat(Expr):
    def __init__(self, leftExpression, rightExpression):
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression

    def evaluate(self):
        return ""


# ()
class GroupedPar(Expr):

    def evaluate(self):
        return ""


# {}
class GroupedBrkt(Expr):
    def evaluate(self):
        return ""
