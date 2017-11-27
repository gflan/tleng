class StoreTestObjectFactory(object):
    def __init__(self):
        pass

    def svg_add_header_footer(self, main_svg):
        return """<?xml version="1.0"?>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
<g transform="scale(40) translate(0, .62)" font-family=
"Courier">
{0}
</g>
</svg>""".format(main_svg)

    def character_svg(self):
        return self.svg_add_header_footer("""<text x="0" y="0" font-size="1">a</text>""")
    def two_characters_svg(self):
        return self.svg_add_header_footer("""<text x="0" y="0" font-size="1">aa</text>""")

    def a_div_b_svg(self):
        return self.svg_add_header_footer("""<text x="0" y="0" font-size="1">a</text>
<line x1="0" y1=".15" x2="0.6" y2=".15"
stroke-width="0.03" stroke="black"/>
<text x="0" y="1" font-size="1">b</text>""")