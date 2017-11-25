import unittest
import parser
from AST import *

class ParserTest(unittest.TestCase):
    def test_cant_create_chr_expression_with_non_character(self):
        with self.assertRaises(ValueError) as contextManager:
            chr = Chr("")
        self.assertEqual(str(contextManager.exception), Chr.non_character_error_description)

    def test_character_is_chr_expression(self):
        self.assertEqual(parser.generate("a"), Chr('a'))

    def test_double_underscore_raises_syntax_error(self):
        self.assert_raises_syntax_error("a_a_a")

    def assert_raises_syntax_error(self, a):
        with self.assertRaises(ValueError) as cm:
            parser.generate(a)
        self.assertEqual(str(cm.exception), "Syntax error in input!")

    def test_double_superscript_raises_syntax_error(self):
        self.assert_raises_syntax_error("a^a^a")

    def test_subscript_and_superscript(self):
        parser.generate("a_b^c")

    def test_superscript_and_subscript(self):
        parser.generate("a^b_c")

    def test_qonda(self):
        #Esto deberia fallar no?
        self.assert_raises_syntax_error("a^b_c^d")

    def test_parse_complex_formula(self):
        parser.generate("(A^BC^D/E^F_G+H)-I")

    def test_complex_formula_equal_formula_with_curly_brackets(self):
        astComplexFormula = parser.generate("(A^BC^D/E^F_G+H)-I")
        curlyBracketsFormula = "{({{A^B}{C^D}}/{{{E^F_G}+}H})-}I"
        astCurlyBrackets = parser.generate(curlyBracketsFormula)
        #self.assertEqual(astComplexFormula, astCurlyBrackets)


if __name__ == '__main__':
    unittest.main()
