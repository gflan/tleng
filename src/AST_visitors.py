from AST import *
from copy import copy

class Visitor: pass

class EscaleVisitor(Visitor):

    def __init__(self, escale):
        self.e = escale

    def visitLambda(self, expr):
        pass

    def visitChr(self, expr):
        expr.e = self.e

    def visitDiv(self, expr):
        expr.leftExpr.accept(self)
        expr.rightExpr.accept(self)

    def visitConcat(self, expr):
        expr.leftExpression.accept(self)
        expr.rightExpression.accept(self)

    def visitSubSuper(self, expr):
        expr.mainExpr.accept(self)
        expr.superExpr.accept(EscaleVisitor(0.7*self.e))
        expr.subExpr.accept(EscaleVisitor(0.7*self.e))

    def visitSuperSub(self, expr):
        expr.mainExpr.accept(self)
        expr.superExpr.accept(EscaleVisitor(0.7*self.e))
        expr.subExpr.accept(EscaleVisitor(0.7*self.e))

    def visitSuperSuffix(self, supersuffix_expr):
        supersuffix_expr.expr.accept(self)

    def visitSubSuffix(self, subsuffix_expr):
        subsuffix_expr.expr.accept(self)

    def visitGroupedPar(self, grouped_expr):
        grouped_expr.expr.accept(self)

class WidthVisitor(Visitor):

    def __init__(self): pass

    def visitLambda(self, expr):
        expr.a = 0

    def visitChr(self, expr):
        expr.a = 0.6 * expr.e

    def visitDiv(self, expr):
        expr.leftExpr.accept(self)
        expr.rightExpr.accept(self)
        expr.a = max(expr.leftExpr.a, expr.rightExpr.a)

    def visitConcat(self, expr):
        expr.leftExpression.accept(self)
        expr.rightExpression.accept(self)
        expr.a = expr.leftExpression.a + expr.rightExpression.a

    def visitSubSuper(self, expr):
        expr.mainExpr.accept(self)
        expr.superExpr.accept(self)
        expr.subExpr.accept(self)
        expr.a = expr.mainExpr.a + expr.superExpr.a + expr.subExpr.a

    def visitSuperSub(self, expr):
        expr.mainExpr.accept(self)
        expr.superExpr.accept(self)
        expr.subExpr.accept(self)
        expr.a = expr.mainExpr.a + expr.superExpr.a + expr.subExpr.a

    def visitSuperSuffix(self, supersuffix_expr):
        supersuffix_expr.expr.accept(self)
        supersuffix_expr.a = supersuffix_expr.expr.a

    def visitSubSuffix(self, subsuffix_expr):
        subsuffix_expr.expr.accept(self)
        subsuffix_expr.a = subsuffix_expr.expr.a

    def visitGroupedPar(self, grouped_expr):
        grouped_expr.expr.accept(self)
        grouped_expr.a = grouped_expr.expr.a


class H1Visitor(Visitor): pass
    #
    # def __init__(self): pass
    #
    # def visitLambda(self, expr):
    #     expr.h1 = 0
    #
    # def visitChr(self, expr):
    #     expr.h1 = 0.6 * expr.e
    #
    # def visitDiv(self, expr): pass
    #     # expr.leftExpr.accept(self)
    #     # expr.rightExpr.accept(self)
    #     # expr.a = max(expr.leftExpr.a, expr.rightExpr.a)
    #
    # def visitConcat(self, expr):
    #     expr.leftExpression.accept(self)
    #     expr.rightExpression.accept(self)
    #     expr.h1 = max(expr.leftExpression.h1, expr.rightExpression.h1)
    #
    # def visitSubSuper(self, expr): pass
    #     # expr.mainExpr.accept(self)
    #     # expr.superExpr.accept(self)
    #     # expr.subExpr.accept(self)
    #     # expr.h1 = max(expr.superExpr.h1, expr.subExpr.h1)
    #
    # def visitSuperSub(self, expr): pass
    #     # expr.mainExpr.accept(self)
    #     # expr.superExpr.accept(self)
    #     # expr.subExpr.accept(self)
    #     # expr.h1 =
    # def visitSuperSuffix(self, supersuffix_expr):
    #     supersuffix_expr.expr.accept(self)
    #     supersuffix_expr.h1 = supersuffix_expr.expr.h1
    #
    # def visitSubSuffix(self, subsuffix_expr):
    #     subsuffix_expr.expr.accept(self)
    #     subsuffix_expr.h1 = 0
    #
    # def visitGroupedPar(self, grouped_expr):
    #     grouped_expr.expr.accept(self)
    #     grouped_expr.h1 = grouped_expr.expr.h1

class H2Visitor(Visitor): pass

class XVisitor(Visitor):

    def __init__(self, pos):
        self.pos = pos

    def visitLambda(self, expr): pass

    def visitChr(self, expr):
        expr.x = self.x

    def visitDiv(self, expr):
        expr.leftExpr.accept(self)
        expr.rightExpr.accept(self)

    def visitConcat(self, expr):
        expr.leftExpression.accept(self)
        expr.rightExpression.accept(XVisitor(self.x + expr.a))

    def visitSubSuper(self, expr):
        expr.mainExpr.accept(self)
        expr.subExpr.accept(XVisitor(self.x + expr.mainExpr.a)) # Quizá deberíamos mover por constante < 1
        expr.superExpr.accept(XVisitor(self.x + expr.mainExpr.a + expr.subExpr.a)) # Idem

    def visitSuperSub(self, expr):
        expr.mainExpr.accept(self)
        expr.superExpr.accept(XVisitor(self.x + expr.mainExpr.a)) # Quizá deberíamos mover por constante < 1
        expr.subExpr.accept(XVisitor(self.x + expr.mainExpr.a + expr.superExpr.a)) # Idem

    def visitSuperSuffix(self, supersuffix_expr):
        supersuffix_expr.expr.accept(self)

    def visitSubSuffix(self, subsuffix_expr):
        subsuffix_expr.expr.accept(self)

    def visitGroupedPar(self, grouped_expr):
        grouped_expr.expr.accept(self)


class YVisitor(Visitor): pass

