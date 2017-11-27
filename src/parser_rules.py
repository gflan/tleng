import ply.yacc as yacc
from tokrules import tokens
from AST import *

#   La idea acá es definir las producciones de la gramática y cómo se va
#   sintetizando el atributo correspondiente "p" a cada una
#   El atributo a sintetizar en teoría es el AST de la expresión
#
#   def p_expression_plus(p):
#       'expression : expression PLUS term'
#       #   ^            ^        ^    ^
#       #  p[0]         p[1]     p[2] p[3]
#
#       p[0] = p[1] + p[3]
#
#   Tambien se pueden condensar varias en una sola fn:
#   def p_binary_operators(p):
#       '''expression : expression PLUS term
#                     | expression MINUS term
#          term       : term TIMES factor
#                     | term DIVIDE factor'''
#       if p[2] == '+':
#           p[0] = p[1] + p[3]
#       elif p[2] == '-':
#           p[0] = p[1] - p[3]
#       elif p[2] == '*':
#           p[0] = p[1] * p[3]
#       elif p[2] == '/':
#           p[0] = p[1] / p[3]
#
#   Para los literales (en nuestro caso +,^,_ no son tokens sino literales):
#   def p_binary_operators(p):
#       '''expression : expression '+' term
#                     | expression '-' term
#          term       : term '*' factor
#                     | term '/' factor'''
#        p[0] = blablabla
#   ------------------------
#   El orden de precedencia se declara por "niveles" de menor a mayor:
#       precedence = (
#           ('nonassoc', 'LESSTHAN', 'GREATERTHAN'),  # Nonassociative operators
#           ('left', 'PLUS', 'MINUS'),
#           ('left', 'TIMES', 'DIVIDE'),
#           ('right', 'UMINUS'),
#       )
#   (NOTA: hay que ver si se puede hacer esto para los literales, sino va a haber
#   que redefinir como tokens normales)
#
#   ------------------------
#   Para el AST:
#
#   class Expr: pass
#
#   class BinOp(Expr):
#       def __init__(self,left,op,right):
#           self.type = "binop"
#           self.left = left
#           self.right = right
#           self.op = op
#
#   class Number(Expr):
#       def __init__(self,value):
#           self.type = "number"
#           self.value = value
#
#   def p_expression_binop(p):
#       '''expression : expression PLUS expression
#                     | expression MINUS expression
#                     | expression TIMES expression
#                     | expression DIVIDE expression'''
#
#       p[0] = BinOp(p[1],p[2],p[3])
#
#   def p_expression_group(p):
#       'expression : LPAREN expression RPAREN'
#       p[0] = p[2]
#
#   def p_expression_number(p):
#       'expression : NUMBER'
#       p[0] = Number(p[1])


SYNTAX_ERROR_IN_INPUT_ERROR_MESSAGE = "Syntax error in input!"

precedence = (

    ('left', 'CONCAT'),

    ('left', 'DIVIDE'),
    ('nonassoc', '^'),
        ('nonassoc', '_'),

)

def p_unary(p):
    '''expression : unary_exp'''
    p[0] = p[1]

def p_expression_chr(p):
    '''unary_exp : CHR'''
    p[0] = Chr(p[1])

def p_expression_concat(p):
    '''expression : expression expression %prec CONCAT'''
    # %prec asocia la precedencia de la producción a la del pseudosimbolo CONCAT
    p[0] = Concat(p[1], p[2])

def p_expression_div(p):
    '''expression : expression DIVIDE expression'''
    p[0] = DivExpr(p[1], p[3])

def p_expression_super(p):
    '''expression : unary_exp '^' unary_exp subexp'''
    p[0] = SuperSub(p[1], p[3], p[4])

def p_expression_sub(p):
    '''expression : unary_exp '_' unary_exp superexp'''
    p[0] = SubSuper(p[1], p[3], p[4])

def p_superexp_lambda(p):
    '''superexp : lambda'''
    p[0] = LambdaExpr()

def p_superexp_expr(p):
    '''superexp : '^' unary_exp'''
    p[0] = SuperSuffix(p[2])

def p_subexp_lambda(p):
    '''subexp : lambda'''
    p[0] = LambdaExpr()

def p_subexp_expr(p):
    '''subexp : '_' unary_exp'''
    p[0] = SubSuffix(p[2])

def p_expression_grouped_par(p):
    '''unary_exp : '(' expression ')' '''
    p[0] = GroupedPar(p[2])

def p_expression_grouped_brkt(p):
    '''unary_exp : '{' expression '}' '''
    # Curly Brackets no aparecen en el AST
    p[0] = p[2]

def p_lambda(p):
    '''lambda :'''

def p_error(p):
    raise ValueError(SYNTAX_ERROR_IN_INPUT_ERROR_MESSAGE)
