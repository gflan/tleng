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
        expr.leftExpr.accept(copy(self))
        expr.rightExpr.accept(copy(self))

    def visitConcat(self, expr):
        expr.leftExpression.accept(copy(self))
        expr.rightExpression.accept(copy(self))

    def visitSubSuper(self, expr):
        expr.mainExpr.accept(copy(self))
        expr.superExpr.accept(EscaleVisitor(0.7*self.e))
        expr.subExpr.accept(EscaleVisitor(0.7*self.e))

    def visitSuperSub(self, expr):
        expr.mainExpr.accept(copy(self))
        expr.superExpr.accept(EscaleVisitor(0.7*self.e))
        expr.subExpr.accept(EscaleVisitor(0.7*self.e))

    def visitSuperSuffix(self, supersuffix_expr):
        supersuffix_expr.expr.accept(copy(self))

    def visitSubSuffix(self, subsuffix_expr):
        subsuffix_expr.expr.accept(copy(self))

    def visitGroupedPar(self, grouped_expr):
        grouped_expr.expr.accept(copy(self))

class WidthVisitor(Visitor):

    def __init__(self): pass

    def visitLambda(self, expr):
        expr.a = 0

    def visitChr(self, expr):
        expr.a = 0.6 * expr.e

    def visitDiv(self, expr):
        expr.leftExpr.accept(copy(self))
        expr.rightExpr.accept(copy(self))
        expr.a = max(expr.leftExpr.a, expr.rightExpr.a)

    def visitConcat(self, expr):
        expr.leftExpression.accept(copy(self))
        expr.rightExpression.accept(copy(self))
        expr.a = expr.leftExpression.a + expr.rightExpression.a

    def visitSubSuper(self, expr):
        expr.mainExpr.accept(copy(self))
        expr.superExpr.accept(copy(self))
        expr.subExpr.accept(copy(self))
        expr.a = expr.mainExpr.a + expr.superExpr.a + expr.subExpr.a

    def visitSuperSub(self, expr):
        expr.mainExpr.accept(copy(self))
        expr.superExpr.accept(copy(self))
        expr.subExpr.accept(copy(self))
        expr.a = expr.mainExpr.a + expr.superExpr.a + expr.subExpr.a

    def visitSuperSuffix(self, supersuffix_expr):
        supersuffix_expr.expr.accept(copy(self))
        supersuffix_expr.a = supersuffix_expr.expr.a

    def visitSubSuffix(self, subsuffix_expr):
        subsuffix_expr.expr.accept(copy(self))
        subsuffix_expr.a = subsuffix_expr.expr.a

    def visitGroupedPar(self, grouped_expr):
        grouped_expr.expr.accept(copy(self))
        grouped_expr.a = grouped_expr.expr.a