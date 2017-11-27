import unittest
from SVGGenerator import *
from StoreTestObjectFactory import *

class SVGGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.test_object_factory = StoreTestObjectFactory()

    def test_a_character(self):
        svg_generator = SVGGenerator('a')
        svg = svg_generator.generate()
        print(svg)
        print(self.test_object_factory.character_svg())
        self.assertEqual(svg, self.test_object_factory.character_svg())

    def test_two_characters(self):
        svg_generator = SVGGenerator('aa')
        svg = svg_generator.generate()
        self.assertEqual(svg, self.test_object_factory.two_characters_svg())

    def test_a_div_b(self):
        svg_generator = SVGGenerator('aa')
        svg = svg_generator.generate()
        self.assertEqual(svg, self.test_object_factory.a_div_b_svg())


if __name__ == '__main__':
    unittest.main()
