import unittest
from SVGGenerator import *
from StoreTestObjectFactory import *

class SVGGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.test_object_factory = StoreTestObjectFactory()

    def test_a_character(self):
        svg_generator = SVGGenerator('a')
        svg = svg_generator.generate()
        self.assertEqual(svg, self.test_object_factory.character_svg())


if __name__ == '__main__':
    unittest.main()
