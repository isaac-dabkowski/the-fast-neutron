from manim import *


class Thumbnail(Scene):
    def construct(self):
        # Title
        title = Tex(r"\underline{The Basics of Nuclear Engineering}").to_edge(UP).shift(DOWN * 0.25)
        # Friendly neutron
        neutron_sprite = ImageMobject("assets/NeutronSprite.png").scale(0.7).to_edge(LEFT).shift(UP)
        # Electron graph
        e_graph = ImageMobject("assets/thumbnail_e.png").scale(0.75).to_corner(DOWN + RIGHT).rotate(10 * DEGREES)
        # Atom
        atom = ImageMobject("assets/thumbnail_atom.png").scale(0.6).to_corner(DOWN + LEFT).rotate(-10 * DEGREES)
        # Plot
        plot = ImageMobject("assets/thumbnail_graph.png").scale(0.9).shift(LEFT + DOWN * 0.5)
        # Einstein
        einstein = ImageMobject("assets/thumbnail_einstein.png").scale(0.5).shift(RIGHT * 3.3 + UP * 0.7)

        self.add(title)
        self.add(neutron_sprite)
        self.add(e_graph)
        self.add(atom)
        self.add(plot)
        self.add(einstein)