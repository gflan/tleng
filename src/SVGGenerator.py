import parser

class SVGGenerator(object):
    def __init__(self, input_str):
        self.input_str = input_str

    def generate(self):
        ast = parser.ast_generate(self.input_str)
        return """<?xml version="1.0"?>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
<g transform="scale(40) translate(0, .62)" font-family=
"Courier">
<text x="0" y="0" font-size="1">{0}</text>
</g>
</svg>""".format(self.input_str)