from manim import *


class Thumbnail(Scene):
    def construct(self):
        # Title
        title = Tex(r"\underline{Cross sections}", font_size=70).to_edge(UP).shift(DOWN * 0.25)
        # Friendly neutron
        images = [
            ImageMobject("assets/NeutronSprite.png").scale(0.7).to_edge(LEFT).shift(UP + RIGHT),
            ImageMobject("assets/beam.png").scale(0.5).to_edge(LEFT).shift(DOWN * 2.5),
            ImageMobject("assets/geom.png").scale(0.9).to_edge(DOWN).shift(RIGHT * 1.0),
            ImageMobject("assets/uplot.png").scale(0.65).next_to(title, DOWN).to_edge(RIGHT),
            ImageMobject("assets/uplot.png").scale(0.65).next_to(title, DOWN).to_edge(RIGHT),
            ImageMobject("assets/form.png").scale(1.5).next_to(title, DOWN).shift(LEFT + DOWN * 0.5).rotate(7 * DEGREES),
            ImageMobject("assets/form2.png").scale(1.1).to_corner(DR).shift(UP * 0.5).rotate(-7 * DEGREES)
        ]
        for img in images:
            self.add(img)
        self.add(title)
