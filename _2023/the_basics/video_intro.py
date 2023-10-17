from manim import *

CHANNEL_TITLE = "The Fast Neutron"
CHANNEL_DESCRIPTION = "A channel all about nuclear science and engineering"
VIDEO_TITLE = "1: The Basics"

TABLE_OF_CONTENTS = [
    "Introduction to atoms",
    "Strong nuclear force",
    "Nuclear binding energy and the semi-empirical mass formula"
]

class TitleCard(Scene):
    def construct(self):
        # Mascot
        neutron_sprite = ImageMobject("assets/NeutronSprite.png")
        # Text
        channel_title = Tex(CHANNEL_TITLE).copy().to_edge(UP)
        channel_description = Tex(CHANNEL_DESCRIPTION).copy().next_to(channel_title, DOWN * 2)
        video_title = Tex(VIDEO_TITLE).to_edge(DOWN).shift(UP * 0.5)
        animations = [
            Wait(),
            FadeIn(neutron_sprite),
            Wait(),
            Write(channel_title),
            Wait(),
            Write(channel_description),
            Wait(),
            Write(video_title),
            Wait()
        ]
        self.play(AnimationGroup(*animations, lag_ratio=1.0))
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class TableOfContents(Scene):
    def construct(self):
        # Make list of Tex items
        title = Tex(f"\\underline{{{VIDEO_TITLE}}}").to_edge(UP).shift(DOWN * 0.2)
        toc = VGroup()
        for i, str in enumerate(TABLE_OF_CONTENTS):
            tex = Tex(f"{i + 1}: {str}", font_size=40)
            toc.add(tex)
        toc.arrange(DOWN, buff=LARGE_BUFF, center=False, aligned_edge=LEFT).next_to(title, DOWN).to_edge(LEFT).shift(RIGHT + DOWN * 0.2)

        # Animate the table of contents
        animations = [Write(title)]
        for line in toc:
            animations += [
                Write(line),
                Wait()
            ]
        self.play(AnimationGroup(*animations, lag_ratio=1.0))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

