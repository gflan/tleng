from sys import argv
import AST_visitors
import parser

# para testear atributos
def generar(input):
    ast = parser.ast_generate(input)

    ast.accept(AST_visitors.EscaleVisitor(1))
    ast.accept(AST_visitors.WidthVisitor())
    ast.accept(AST_visitors.HVisitor())
    ast.accept(AST_visitors.XVisitor(0))
    ast.accept(AST_visitors.YVisitor(0))
    ast.accept(AST_visitors.SVGRendererVisitor())

    return ast

if __name__ == "__main__":
    ast_with_attributes = generar(argv[1])
    print(ast_with_attributes.svg)
