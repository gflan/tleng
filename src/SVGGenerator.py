import parser

class SVGGenerator(object):
    def __init__(self, input_str):
        self.input_str = input_str

    def generate(self, ):
        ast = parser.ast_generate(self.input_str)
        return ''