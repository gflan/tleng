class Expr: pass

class LambdaExpr(Expr):
    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, LambdaExpr)

    def __str__(self):
        return "LambdaExpr"

    def accept(self, visitor):
        visitor.visitLambda(self)

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

    def __str__(self):
        return "Chr({0})".format(self.character)

    def accept(self, visitor):
        visitor.visitChr(self)

class DivExpr(Expr):
    def __init__(self, leftExpr, rightExpr):
        self.leftExpr = leftExpr
        self.rightExpr = rightExpr

    def __eq__(self, other):
        if not isinstance(other, DivExpr):
            return False

        return self.leftExpr == other.leftExpr and self.rightExpr == other.rightExpr
    def __str__(self):
        return "DivExpr({0},{1})".format(self.leftExpr, self.rightExpr)

    def accept(self, visitor):
        visitor.visitDiv(self)

# A B
class Concat(Expr):
    def __init__(self, leftExpression, rightExpression):
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression

    def __eq__(self, other):
        if not isinstance(other, Concat):
            return False
        return self.leftExpression == other.leftExpression and self.rightExpression == other.rightExpression

    def __str__(self):
        return "Concat({0},{1})".format(self.leftExpression, self.rightExpression)

    def accept(self, visitor):
        visitor.visitConcat(self)

class SuperSub(Expr):
    def __init__(self, mainExpr, superExpr, subExpr):
        self.mainExpr = mainExpr
        self.superExpr = superExpr
        self.subExpr = subExpr

    def __eq__(self, other):
        if not isinstance(other, SuperSub):
            return False

        comp = True
        comp = comp and (self.mainExpr == other.mainExpr)
        comp = comp and (self.superExpr == other.superExpr)
        comp = comp and (self.subExpr == other.subExpr)

        return comp

    def __str__(self):
        return "SuperSub({0}, {1}, {2})".format(str(self.mainExpr), str(self.superExpr), str(self.subExpr))

    def accept(self, visitor):
        visitor.visitSuperSub(self)

class SubSuper(Expr):
    def __init__(self, mainExpr, superExpr, subExpr):
        self.mainExpr = mainExpr
        self.superExpr = superExpr
        self.subExpr = subExpr

    def __eq__(self, other):
        if not isinstance(other, SubSuper):
            return False

        comp = True
        comp = comp and (self.mainExpr == other.mainExpr)
        comp = comp and (self.superExpr == other.superExpr)
        comp = comp and (self.subExpr == other.subExpr)

        return comp

    def __str__(self):
        return "SubSuper({0}, {1}, {2})".format(str(self.mainExpr), str(self.superExpr), str(self.subExpr))

    def accept(self, visitor):
        visitor.visitSubSuper(self)

class SuperSuffix(Expr):
    def __init__(self, expr):
        self.expr = expr

    def __eq__(self, other):
        if not isinstance(other, SuperSuffix):
            return False
        return other.expr == self.expr

    def __str__(self):
        return "SuperSuffix({0})".format(self.expr)

    def accept(self, visitor):
        visitor.visitSuperSuffix(self)

class SubSuffix(Expr):
    def __init__(self, expr):
        self.expr = expr

    def __eq__(self, other):
        if not isinstance(other, SubSuffix):
            return False
        return other.expr == self.expr

    def __str__(self):
        return "SubSuffix({0})".format(self.expr)

    def accept(self, visitor):
        visitor.visitSubSuffix(self)

# ()
class GroupedPar(Expr):
    def __init__(self, expr):
        self.expr = expr

    def __eq__(self, other):
        if not isinstance(other, GroupedPar):
            return False
        return self.expr == other.expr

    def __str__(self):
        return "GroupedPar({0})".format(self.expr)

    def accept(self, visitor):
        visitor.visitGroupedPar(self)
