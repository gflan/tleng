#!/usr/bin/python3
from sys import argv

from ply.lex import lex
import tokrules

from ply.yacc import yacc
import parser_rules


def generate(input_str):
    lexer = lex(module=tokrules)
    parser = yacc(module=parser_rules)
    ast = parser.parse(input_str, lexer)
    print(ast)
    # TODO hacer lo que haga falta con el arbol para que genere el SVG


if __name__ == "__main__":

    # "This result return is the value assigned to p[0] in the starting grammar rule."
    # ast es de tipo Expr (def @ parser_rules)
    generate(argv[1])
