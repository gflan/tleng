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
#
#       Posible estructura TODO Completar
# E

SYNTAX_ERROR_IN_INPUT_ERROR_MESSAGE = "Syntax error in input!"

precedence = (
           ('left', '/'),
           ('left', 'CONCAT'),
           ('nonassoc', '^'),
           ('nonassoc', '_'),
)

start = 'start'

def p_start(p):
    '''start : expression '''
    p[0] = Start(p[1])

def p_expression_chr(p):
    '''expression : CHR '''
    p[0] = Chr(p[1])

def p_expression_concat(p):
    '''expression : expression expression %prec CONCAT'''
    # %prec asocia la precedencia de la producción a la del pseudosimbolo CONCAT
    p[0] = Concat(p[1], p[2])

def p_expression_binop(p):
    '''expression : expression '^' expression
                  | expression '_' expression
                  | expression '/' expression'''
    p[0] = p[1]

def p_expression_grouped_par(p):
    '''expression : '(' expression ')' '''
    p[0] = p[1]


def p_expression_grouped_brkt(p):
    '''expression : '{' expression '}' '''
    p[0] = p[1]


def p_error(p):
    raise ValueError(SYNTAX_ERROR_IN_INPUT_ERROR_MESSAGE)
