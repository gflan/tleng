class Expr: pass


# a
class Chr(Expr):
    def __init__(self, value):
        self.value = value


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
