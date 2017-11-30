import ply.yacc as yacc
from tokrules import tokens
from AST import *

SYNTAX_ERROR_IN_INPUT_ERROR_MESSAGE = "Syntax error in input!"

precedence = (
    ('left', 'DIV'),

    ('left', '{', '('),

    ('left', 'CHR'),

    ('left', 'CONCAT'),

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
    '''expression : expression DIVIDE expression %prec DIV'''
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
