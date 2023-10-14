from manim import *

CHANNEL_TITLE = Tex("The ", "Fast ", "Neutron").to_edge(UP)
CHANNEL_DESCRIPTION = Tex("A channel all about nuclear science and engineering").next_to(CHANNEL_TITLE, DOWN * 2)
VIDEO_TITLE = Tex("1: The Basics").to_edge(DOWN)

TABLE_OF_CONTENTS = [
    "Atoms",
    "Strong nuclear force",
    "Nuclear binding energy",
    "Fission and Fusion"
]

class TitleCard(Scene):
    def construct(self):
        # Mascot
        neutron_sprite = ImageMobject("assets/NeutronSprite.png")
        # Text
        animations = [
            FadeIn(neutron_sprite),
            Wait(),
            FadeIn(CHANNEL_TITLE[0], shift=DOWN),
            FadeIn(CHANNEL_TITLE[1], shift=DOWN),
            FadeIn(CHANNEL_TITLE[2], shift=DOWN),
            Wait(2),
            FadeIn(CHANNEL_DESCRIPTION, shift=UP),
            Wait(3),
            FadeIn(VIDEO_TITLE, shift=UP)
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))

class TableOfContents(Scene):
    def construct(self):
        # Make list of Tex items
        tex_items = list()
        for i, str in enumerate(TABLE_OF_CONTENTS):
            tex = Tex(f"{i + 1}: {str}")
            if i == 0:
                tex.to_corner(LEFT + UP)
            else:
                tex.next_to(tex_items[i-1], DOWN * 2)
                tex.align_to(tex_items[i-1], LEFT)
            tex_items.append(tex)
        # Animate the list
        animations = list()
        for str in tex_items:
            animations += [
                Write(str),
                Wait()
            ]
        # Execute
        self.play(AnimationGroup(*animations, lag_ratio=0.5))

