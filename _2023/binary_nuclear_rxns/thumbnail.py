from manim import *


class Thumbnail(Scene):
    def construct(self):
        # Title
        title = Tex(r"\underline{Nuclear Decay - Part 2}", font_size=70).to_edge(UP).shift(DOWN * 0.25)
        # Friendly neutron
        neutron_sprite = ImageMobject("assets/NeutronSprite.png").scale(0.7).to_edge(LEFT).shift(UP * 2)
        i1 = ImageMobject("assets/bigplot.png").scale(1.6).shift(DOWN + RIGHT * 1.8)
        i2 = ImageMobject("assets/half_life.png").scale(2).next_to(i1, UP).shift(DOWN * 0.7 + RIGHT)
        i3 = ImageMobject("assets/decay_diagram.png").scale(1.3).to_corner(DOWN + LEFT).shift(LEFT * 0.3 + UP * 0.3)

        self.add(title)
        self.add(neutron_sprite)
        self.add(i1)
        self.add(i2)
        self.add(i3)
