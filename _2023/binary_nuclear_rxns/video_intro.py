from manim import *

CHANNEL_TITLE = "The Fast Neutron"
CHANNEL_DESCRIPTION = "A channel all about nuclear science and engineering"
VIDEO_TITLE = "4: Binary nuclear reactions"

TABLE_OF_CONTENTS = [
    "Binary nuclear reactions",
    "Kinematic thresholds",
    "Coulombic thresholds"
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
        # Write title
        title = Tex(f"\\underline{{{VIDEO_TITLE}}}").to_edge(UP).shift(DOWN * 0.2)
        self.play(Write(title))
        # Create a box which will hold a video insert which we will add in Davinci Resolve during editing
        video_insert_box = Rectangle(color=YELLOW, width=5, height=3).shift(RIGHT * 4)
        video_insert_tex = Tex("Last video...").next_to(video_insert_box, UP)
        self.play(Write(video_insert_tex), DrawBorderThenFill(video_insert_box))
        self.wait()
        # Make list of Tex items
        toc = VGroup()
        for i, str in enumerate(TABLE_OF_CONTENTS):
            tex = Tex(f"{i + 1}: {str}", font_size=40)
            toc.add(tex)
        toc.arrange(DOWN, buff=LARGE_BUFF, center=False, aligned_edge=LEFT).next_to(title, DOWN).to_edge(LEFT).shift(RIGHT + DOWN * 0.2)

        # Animate the table of contents
        animations = list()
        for line in toc:
            animations += [
                Write(line),
                Wait()
            ]
        self.play(AnimationGroup(*animations, lag_ratio=1.0))
        self.wait()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

