from sys import argv, exit
import AST_visitors
import parser
# ejemplo de uso:
# python3 (A^(A^(A^(A^(A)))_B)/E^F_G+H)-I"  [opcional:] -o cadenalarga.svg
# por defecto manda a output.svg sino

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

    if len(argv) == 0:
        print("Parámetros válidos: <expresión>  [opcional: -o <nombre del output svg>]")
        exit(1)

    ast_with_attributes = generar(argv[1])
    result = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{}\" height=\"{}\" version=\"1.1\" style=\"background: white\">\n<g transform=\"scale(40) translate(1,1)\" font-family=\"Courier\">\n".format(ast_with_attributes.a*50+80, (ast_with_attributes.h1+ast_with_attributes.h2)*40+80, ast_with_attributes.h1)
    result += ast_with_attributes.svg
    result += "</g>\n</svg>\n"


    file = argv[3] if len(argv) > 3 and argv[2] == "-o" else "output.svg"
    output_file = open(file, "w")
    output_file.write(result)
    output_file.close()



    print(result)
