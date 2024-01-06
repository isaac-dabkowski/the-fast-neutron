from manim import *


class Thumbnail(Scene):
    def construct(self):
        # Title
        title = Tex(r"\underline{Binary nuclear reactions}", font_size=70).to_edge(UP).shift(DOWN * 0.25)
        # Friendly neutron
        neutron_sprite = ImageMobject("assets/NeutronSprite.png").scale(0.7).to_edge(LEFT).shift(UP + RIGHT)
        i1 = ImageMobject("assets/BNR_diagram.png").scale(1.6).shift(RIGHT * 1.8 + UP)
        i2 = ImageMobject("assets/eqns.png").scale(1.1).to_edge(DOWN)
        i3 = ImageMobject("assets/react.png").scale(1.2).next_to(i2, UP)

        self.add(title)
        self.add(neutron_sprite)
        self.add(i1)
        self.add(i2)
        self.add(i3)
