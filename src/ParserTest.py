import unittest
import main
from AST import *
from AST_visitors import *

class ParserTest(unittest.TestCase):
    def test_cant_create_chr_expression_with_non_character(self):
        with self.assertRaises(ValueError) as contextManager:
            chr = Chr("")
        self.assertEqual(str(contextManager.exception), Chr.non_character_error_description)

    def test_character_is_chr_expression(self):
        self.assertEqual(main.ast_generate("a"), Chr('a'))

    def test_double_underscore_raises_syntax_error(self):
        self.assert_raises_syntax_error("a_a_a")

    def assert_raises_syntax_error(self, a):
        with self.assertRaises(ValueError) as cm:
            main.ast_generate(a)
        self.assertEqual(str(cm.exception), "Syntax error in input!")

    def test_double_superscript_raises_syntax_error(self):
        self.assert_raises_syntax_error("a^a^a")

    def test_superscript(self):
        ast = SuperSub(Chr('a'), Chr('b'), LambdaExpr())
        superScriptStr = "a^b"
        self.assert_equal_ast(ast, superScriptStr)

    def assert_equal_ast(self, ast, superScriptStr):
        parsedAst = main.ast_generate(superScriptStr)
        self.assertEqual(parsedAst, ast)

    def test_subscript(self):
        ast = SubSuper(Chr('a'), Chr('b'), LambdaExpr())
        self.assert_equal_ast(ast, "a_b")

    def test_subscript_and_superscript(self):
        ast = SubSuper(Chr('a'), Chr('b'), SuperSuffix(Chr('c')))
        self.assert_equal_ast(ast, "a_b^c")

    def test_superscript_and_subscript(self):
        ast = SuperSub(Chr('a'), Chr('b'), SubSuffix(Chr('c')))
        self.assert_equal_ast(ast, "a^b_c")

    def test_qonda(self):
        #Esto deberia fallar no?
        self.assert_raises_syntax_error("a^b_c^d")
        self.assert_raises_syntax_error("a_b^c_d")

    def test_div(self):
        ast = DivExpr(Chr('a'), Chr('b'))
        self.assert_equal_ast(ast, "a/b")

    def test_div_minus(self):
        ast = DivExpr(Chr('a'), Concat(Concat(Chr('b'), Chr('-')),Chr('c')))
        self.assert_equal_ast(ast, "a/b-c")

    def test_parse_complex_formula(self):
        leftDivAst = Concat(SuperSub(Chr('A'), Chr('B'), LambdaExpr()), SuperSub(Chr('C'), Chr('D'), LambdaExpr()))
        rightDivAst = Concat(Concat(SuperSub(Chr('E'), Chr('F'), SubSuffix(Chr('G'))), Chr('+')), Chr('H'))
        parentesisedAst = GroupedPar(DivExpr(leftDivAst, rightDivAst))
        ast = Concat(Concat(parentesisedAst, Chr('-')), Chr('I'))

        self.assert_equal_ast(ast, "(A^BC^D/E^F_G+H)-I")

    def test_complex_formula_equal_formula_with_curly_brackets(self):
        astComplexFormula = main.ast_generate("(A^BC^D/E^F_G+H)-I")
        curlyBracketsFormula = "{({{A^B}{C^D}}/{{{E^F_G}+}H})-}I"
        astCurlyBrackets = main.ast_generate(curlyBracketsFormula)
        self.assertEqual(astComplexFormula, astCurlyBrackets)

if __name__ == '__main__':
    unittest.main()
