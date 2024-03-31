from manim import *


class Thumbnail(Scene):
    def construct(self):
        # Title
        title = Tex(r"\underline{Neutron scattering}", font_size=70).to_edge(UP).shift(DOWN * 0.25)
        # Friendly neutron
        neutron_sprite = ImageMobject("assets/NeutronSprite.png").scale(0.7).to_edge(LEFT).shift(UP + RIGHT)
        i1 = ImageMobject("assets/scatter_angle.png").scale(0.5).next_to(neutron_sprite, DOWN).shift(DOWN*0.5).rotate(10 * DEGREES)
        i2 = ImageMobject("assets/leth.png").scale(1.5).to_edge(DOWN).shift(RIGHT * 1.0)
        i3 = ImageMobject("assets/scatter_sim.png").scale(0.8).next_to(i2, UP).shift(RIGHT * 1.5).rotate(-5 * DEGREES)

        self.add(title)
        self.add(neutron_sprite)
        self.add(i1)
        self.add(i2)
        self.add(i3)
