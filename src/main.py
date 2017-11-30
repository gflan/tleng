#!/usr/bin/python3
from sys import argv, exit
import argparse

from ply.lex import lex
import tokrules

from ply.yacc import yacc
import parser_rules

import AST_visitors
# ejemplo de uso:
# python3 main.py "(A^(A^(A^(A^(A)))_B)/E^F_G+H)-I"  [opcional:] -o cadenalarga.svg
# por defecto manda a output.svg sino

def ast_generate(input_str):
    lexer = lex(module=tokrules)
    parser = yacc(module=parser_rules)
    ast = parser.parse(input_str, lexer)
    return ast

def generar(input):
    ast = ast_generate(input)
    # print(ast)
    ast.accept(AST_visitors.EscaleVisitor(1))
    ast.accept(AST_visitors.WidthVisitor())
    ast.accept(AST_visitors.HVisitor())
    ast.accept(AST_visitors.XVisitor(0))
    ast.accept(AST_visitors.YVisitor(ast.h1))
    ast.accept(AST_visitors.SVGRendererVisitor())

    return ast

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='Parsea y genera SVG. Lo podes mandar a un archivo')
    argparser.add_argument('expression', type=str,
                        help='Expresion para parsear')

    argparser.add_argument('--output', '-o', dest='output_filename', default='output.svg', type=str,
                        help="Archivo output svg")

    argparser.add_argument('--print-svg', '-p', dest='print_svg', action='store_const',
                    const=True, default=False,
                    help='Imprimir svg')

    args = argparser.parse_args()

    ast_with_attributes = generar(args.expression)
    result = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{}\" height=\"{}\" version=\"1.1\" style=\"background: white\">\n<g transform=\"scale(40) translate(1,1)\" font-family=\"Courier\">\n".format(ast_with_attributes.a*50+80, (ast_with_attributes.h1+ast_with_attributes.h2)*40+80, ast_with_attributes.h1)
    result += ast_with_attributes.svg
    result += "</g>\n</svg>\n"

    output_file = open(args.output_filename, "w")
    output_file.write(result)
    output_file.close()

    if args.print_svg:
        print(result)
