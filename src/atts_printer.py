from sys import argv
import AST_visitors
import parser

# para testear atributos
def generar(input):
    ast = parser.ast_generate(input)
    # print(ast)
    ast.accept(AST_visitors.EscaleVisitor(1))
    ast.accept(AST_visitors.WidthVisitor())
    ast.accept(AST_visitors.HVisitor())
    ast.accept(AST_visitors.XVisitor(0))
    ast.accept(AST_visitors.YVisitor(ast.h1))
    ast.accept(AST_visitors.SVGRendererVisitor())

    return ast

if __name__ == "__main__":
    ast_with_attributes = generar(argv[1])
    # ast_with_attributes = generar("(A^{A^{A^{A^{A}}}}/E^F_G+H)-I")
    result = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"2000\" height=\"1000\" version=\"1.1\">\n<g transform=\"scale(40)\" font-family=\"Courier\">\n"
    result += ast_with_attributes.svg
    result += "</g>\n</svg>\n"
    print(result)
