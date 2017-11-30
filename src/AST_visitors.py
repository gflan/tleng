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
        expr.e = self.e
        expr.leftExpr.accept(self)
        expr.rightExpr.accept(self)

    def visitConcat(self, expr):
        expr.e = self.e
        expr.leftExpression.accept(self)
        expr.rightExpression.accept(self)

    def visitSubSuper(self, expr):
        expr.e = self.e
        expr.mainExpr.accept(self)
        expr.superExpr.accept(EscaleVisitor(0.7*self.e))
        expr.subExpr.accept(EscaleVisitor(0.7*self.e))

    def visitSuperSub(self, expr):
        expr.e = self.e
        expr.mainExpr.accept(self)
        expr.superExpr.accept(EscaleVisitor(0.7*self.e))
        expr.subExpr.accept(EscaleVisitor(0.7*self.e))

    def visitSuperSuffix(self, supersuffix_expr):
        supersuffix_expr.e = self.e
        supersuffix_expr.expr.accept(self)

    def visitSubSuffix(self, subsuffix_expr):
        subsuffix_expr.e = self.e
        subsuffix_expr.expr.accept(self)

    def visitGroupedPar(self, grouped_expr):
        grouped_expr.e = self.e
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
        expr.a = expr.mainExpr.a + max(expr.superExpr.a, expr.subExpr.a)

    def visitSuperSub(self, expr):
        expr.mainExpr.accept(self)
        expr.superExpr.accept(self)
        expr.subExpr.accept(self)
        expr.a = expr.mainExpr.a + max(expr.superExpr.a, expr.subExpr.a)

    def visitSuperSuffix(self, supersuffix_expr):
        supersuffix_expr.expr.accept(self)
        supersuffix_expr.a = supersuffix_expr.expr.a

    def visitSubSuffix(self, subsuffix_expr):
        subsuffix_expr.expr.accept(self)
        subsuffix_expr.a = subsuffix_expr.expr.a

    def visitGroupedPar(self, grouped_expr):
        grouped_expr.expr.accept(self)
        grouped_expr.a = grouped_expr.expr.a + grouped_expr.e * 2 * 0.6 # contar ()

class HVisitor(Visitor):

    def __init__(self): pass

    def visitLambda(self, expr):
        expr.h1 = 0
        expr.h2 = 0
        expr.h = 0

    def visitChr(self, expr):
        expr.h1 = expr.e
        expr.h2 = 0
        expr.h = expr.e

    def visitDiv(self, expr):
        expr.leftExpr.accept(self)
        expr.rightExpr.accept(self)
        expr.h1 = expr.leftExpr.h1 + expr.leftExpr.h2 + expr.e*0.6
        expr.h2 = expr.rightExpr.h1 + expr.rightExpr.h2 - expr.e*0.6
        expr.h = expr.h1 + expr.h2

    def visitConcat(self, expr):
        expr.leftExpression.accept(self)
        expr.rightExpression.accept(self)
        expr.h1 = max(expr.leftExpression.h1, expr.rightExpression.h1)
        expr.h2 = max(expr.leftExpression.h2, expr.rightExpression.h2)
        expr.h = expr.h1 + expr.h2

    def visitSubSuper(self, expr):
        expr.mainExpr.accept(self)
        expr.superExpr.accept(self)
        expr.subExpr.accept(self)

        super_h1 = 0 if isinstance(expr.superExpr, LambdaExpr) else expr.mainExpr.h1*0.45 + expr.mainExpr.e + expr.superExpr.h1 - expr.superExpr.e
        #sumamos el h1 hasta el 'y' del superindice con su h1 y le restamos su escala (que sino se suma dos veces)

        expr.h1 = max(expr.mainExpr.h1, super_h1)

        sub_h2 = expr.subExpr.h2 + expr.subExpr.e + (expr.mainExpr.h1 + expr.mainExpr.h2)*0.25 - expr.mainExpr.e*0.7 # en un dibujo se ve bien, notar el 0.7 porque los char del mainExpr no miden toda la escala de largo sino que solo el 70% y el restante es espacio vacio
        expr.h2 = max(expr.mainExpr.h2, sub_h2)
        expr.h = expr.h1 + expr.h2

    def visitSuperSub(self, expr):
        expr.mainExpr.accept(self)
        expr.superExpr.accept(self)
        expr.subExpr.accept(self)

        sub_h2 = 0 if isinstance(expr.subExpr, LambdaExpr) else expr.subExpr.h2 + expr.subExpr.e + (expr.mainExpr.h1 + expr.mainExpr.h2)*0.25 - expr.mainExpr.e*0.7

        expr.h2 = max(expr.mainExpr.h2, sub_h2)
        super_h1 = expr.mainExpr.h1*0.45 + expr.mainExpr.e + expr.superExpr.h1 - expr.superExpr.e
        expr.h1 = max(expr.mainExpr.h1, super_h1)
        expr.h = expr.h1 + expr.h2

    def visitSuperSuffix(self, supersuffix_expr):
        supersuffix_expr.expr.accept(self)
        supersuffix_expr.h1 = supersuffix_expr.expr.h1
        supersuffix_expr.h2 = supersuffix_expr.expr.h2
        supersuffix_expr.h = supersuffix_expr.h1 + supersuffix_expr.h2

    def visitSubSuffix(self, subsuffix_expr):
        subsuffix_expr.expr.accept(self)
        subsuffix_expr.h1 = subsuffix_expr.expr.h1
        subsuffix_expr.h2 = subsuffix_expr.expr.h2
        subsuffix_expr.h = subsuffix_expr.h1 + subsuffix_expr.h2

    def visitGroupedPar(self, grouped_expr):
        grouped_expr.expr.accept(self)
        grouped_expr.h1 = grouped_expr.expr.h1
        grouped_expr.h2 = grouped_expr.expr.h2
        grouped_expr.h = grouped_expr.expr.h

class XVisitor(Visitor):

    def __init__(self, pos):
        self.pos = pos

    def visitLambda(self, expr): pass

    def visitChr(self, expr):
        expr.x = self.pos

    def visitDiv(self, expr):
        divwidth = max(expr.leftExpr.a, expr.rightExpr.a)
        #ambos centrados respecto de la linea de división
        expr.leftExpr.accept(XVisitor(self.pos + (divwidth - expr.leftExpr.a)/2))
        expr.rightExpr.accept(XVisitor(self.pos + (divwidth - expr.rightExpr.a)/2))
        expr.x = self.pos

    def visitConcat(self, expr):
        expr.leftExpression.accept(self)
        expr.rightExpression.accept(XVisitor(self.pos + expr.leftExpression.a))
        expr.x = self.pos

    def visitSubSuper(self, expr):
        expr.mainExpr.accept(self)
        expr.subExpr.accept(XVisitor(self.pos + expr.mainExpr.a))
        expr.superExpr.accept(XVisitor(self.pos + expr.mainExpr.a))
        expr.x = self.pos

    def visitSuperSub(self, expr):
        expr.mainExpr.accept(self)
        expr.superExpr.accept(XVisitor(self.pos + expr.mainExpr.a))
        expr.subExpr.accept(XVisitor(self.pos + expr.mainExpr.a))
        expr.x = self.pos

    def visitSuperSuffix(self, supersuffix_expr):
        supersuffix_expr.expr.accept(self)
        supersuffix_expr.x = self.pos

    def visitSubSuffix(self, subsuffix_expr):
        subsuffix_expr.expr.accept(self)
        subsuffix_expr.x = self.pos

    def visitGroupedPar(self, grouped_expr):
        grouped_expr.expr.accept(XVisitor(self.pos + 0.6*grouped_expr.e)) # dejar espacio para '('
        grouped_expr.x = self.pos

class YVisitor(Visitor):

    def __init__(self, pos):
        self.pos = pos

    def visitLambda(self, expr): pass

    def visitChr(self, expr):
        expr.y = self.pos

    def visitDiv(self, expr):
        expr.leftExpr.accept(YVisitor(self.pos - expr.leftExpr.h2 - expr.e*0.6))
        expr.rightExpr.accept(YVisitor(self.pos + expr.rightExpr.h1 - expr.e*0.6))
        expr.y = self.pos

    def visitConcat(self, expr):
        expr.leftExpression.accept(self)
        expr.rightExpression.accept(self)
        expr.y = self.pos

    def visitSubSuper(self, expr):
        expr.mainExpr.accept(self)
        expr.subExpr.accept(YVisitor(self.pos + (expr.mainExpr.h1 + expr.mainExpr.h2)*0.25)) #parece ser la fórmula que usaron en el ejemplo del enunciado
        expr.superExpr.accept(YVisitor(self.pos - expr.mainExpr.h1*0.45)) #visto en clase
        expr.y = self.pos

    def visitSuperSub(self, expr):
        expr.mainExpr.accept(self)
        expr.subExpr.accept(YVisitor(self.pos + (expr.mainExpr.h1 + expr.mainExpr.h2)*0.25))
        expr.superExpr.accept(YVisitor(self.pos - expr.mainExpr.h1*0.45))
        expr.y = self.pos

    def visitSuperSuffix(self, supersuffix_expr):
        supersuffix_expr.expr.accept(self)
        supersuffix_expr.y = self.pos

    def visitSubSuffix(self, subsuffix_expr):
        subsuffix_expr.expr.accept(self)
        subsuffix_expr.y = self.pos

    def visitGroupedPar(self, grouped_expr):
        if isinstance(grouped_expr.expr, DivExpr):
            grouped_expr.expr.accept(YVisitor(self.pos - 0.3 * grouped_expr.expr.e))
        else:
            grouped_expr.expr.accept(self)

        grouped_expr.y = self.pos

class SVGRendererVisitor(Visitor) :

    def __init__(self): pass

    def visitLambda(self, expr):
        expr.svg = ""

    def visitChr(self, expr):
        expr.svg = "<text x=\"{}\" y=\"{}\" font-size=\"{}\">{}</text> \n".format(expr.x, expr.y, expr.e, expr.character)

    def visitDiv(self, expr):
        expr.leftExpr.accept(self)
        expr.rightExpr.accept(self)
        expr.svg = expr.leftExpr.svg
        expr.svg += "<line x1=\"{}\" y1=\"{}\" x2=\"{}\" y2=\"{}\" stroke-width=\"0.03\" stroke=\"black\"/>".format(expr.x, expr.y-expr.e*0.45, expr.x + expr.a, expr.y-expr.e*0.45)
        expr.svg += expr.rightExpr.svg

    def visitConcat(self, expr):
        expr.leftExpression.accept(self)
        expr.rightExpression.accept(self)
        expr.svg = expr.leftExpression.svg + expr.rightExpression.svg

    def visitSubSuper(self, expr):
        expr.mainExpr.accept(self)
        expr.superExpr.accept(self)
        expr.subExpr.accept(self)
        expr.svg = expr.mainExpr.svg + expr.subExpr.svg + expr.superExpr.svg

    def visitSuperSub(self, expr):
        expr.mainExpr.accept(self)
        expr.superExpr.accept(self)
        expr.subExpr.accept(self)
        expr.svg = expr.mainExpr.svg + expr.superExpr.svg + expr.subExpr.svg

    def visitSuperSuffix(self, supersuffix_expr):
        supersuffix_expr.expr.accept(self)
        supersuffix_expr.svg = supersuffix_expr.expr.svg

    def visitSubSuffix(self, subsuffix_expr):
        subsuffix_expr.expr.accept(self)
        subsuffix_expr.svg = subsuffix_expr.expr.svg

    def visitGroupedPar(self, grouped_expr):
        grouped_expr.expr.accept(self)
        times_scale = grouped_expr.h/grouped_expr.e
        grouped_expr.svg = "<text x=\"0\" y=\"0\" font-size=\"{}\" transform=\"translate({},{}) scale(1,{})\">(</text> \n".format(grouped_expr.e, grouped_expr.x, grouped_expr.y-(times_scale-1)*0.2*grouped_expr.e, times_scale)

        grouped_expr.svg += grouped_expr.expr.svg

        grouped_expr.svg += "<text x=\"0\" y=\"0\" font-size=\"{}\" transform=\"translate({},{}) scale(1,{})\">)</text> \n".format(grouped_expr.e, grouped_expr.x + grouped_expr.a - 0.6*grouped_expr.e, grouped_expr.y-(times_scale-1)*0.2*grouped_expr.e, times_scale)
