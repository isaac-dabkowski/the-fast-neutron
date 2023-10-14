from manim import *


class Proton(ThreeDScene):
    def construct(self):
        # Create proton
        proton = Circle(
            radius=1.0,
            color=RED,
        )
        proton.set_fill(RED, opacity=0.5)
        self.play(Create(proton))
        self.play(Wait())

        # Move proton to right and display some info
        self.play(proton.animate.move_to(RIGHT * 3))
        tex1 = Tex(r"\underline{Proton}").to_corner(LEFT + UP)
        tex2 = Tex(r"Mass: $1.673\cdot10^{-27}$ kg").next_to(tex1, DOWN).align_to(tex1, LEFT)
        tex3 = Tex(r"Charge: +1 e").next_to(tex2, DOWN).align_to(tex1, LEFT)
        animations = [
            Write(tex1),
            Wait(),
            Write(tex2),
            Wait(),
            Write(tex3)
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))


