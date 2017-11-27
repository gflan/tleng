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
