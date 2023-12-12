from manim import *


class Thumbnail(Scene):
    def construct(self):
        # Title
        title = Tex(r"\underline{Nuclear Decay - Part 1}", font_size=70).to_edge(UP).shift(DOWN * 0.25)
        # Friendly neutron
        neutron_sprite = ImageMobject("assets/NeutronSprite.png").scale(0.7).to_edge(LEFT).shift(UP)
        # Chart of nuclides
        chart = ImageMobject("assets/chart.png").scale(1.1).to_edge(RIGHT)
        # Beta decay
        beta = ImageMobject("assets/betadecay.png").next_to(chart, DOWN)
        # Beta plot
        betaplot = ImageMobject("assets/betachart.png").to_corner(DOWN + LEFT)

        self.add(title)
        self.add(neutron_sprite)
        self.add(chart)
        self.add(beta)
        self.add(betaplot)
