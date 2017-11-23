#!/usr/bin/python3
from sys import stdin, argv
from ply.lex import lex
import tokrules

if __name__ == "__main__":
    # si hace falta lo metemos a archivo, por ahora solo para testear
    # ej: python3 lexer.py "A+B^{C}"

    expr = argv[1]
    lexer = lex(module=tokrules)
    lexer.input(expr)

    for tok in lexer:
        print(tok)
