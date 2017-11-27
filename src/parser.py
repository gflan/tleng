#!/usr/bin/python3
from sys import argv

from ply.lex import lex
import tokrules

from ply.yacc import yacc
import parser_rules
from SVGGenerator import *

def ast_generate(input_str):
    lexer = lex(module=tokrules)
    parser = yacc(module=parser_rules)
    ast = parser.parse(input_str, lexer)
    return ast
    # TODO hacer lo que haga falta con el arbol para que genere el SVG
    # ast.accept(EscaleVisitor(1))


if __name__ == "__main__":

    # "This result return is the value assigned to p[0] in the starting grammar rule."
    # ast es de tipo Expr (def @ parser_rules)
    print(SVGGenerator(argv[1]).generate())
