from sys import argv
import AST_visitors
import parser

# para testear atributos
def generar(input):
    ast = parser.ast_generate(input)
    ve = AST_visitors.EscaleVisitor(1)
    vw = AST_visitors.WidthVisitor()
    vh = AST_visitors.HVisitor()
    vx = AST_visitors.XVisitor(0)
    vy = AST_visitors.YVisitor(0)
    ast.accept(ve)
    ast.accept(vw)
    ast.accept(vh)
    ast.accept(vx)
    ast.accept(vy)
    ast.accept(AST_visitors.PrintVisitor())
    return ast

if __name__ == "__main__":
    generar(argv[1])
