from manim import *


class Proton(Scene):
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
        tex2 = Tex(r"Mass: $1.673\times10^{-27}$ kg").next_to(tex1, DOWN).align_to(tex1, LEFT)
        tex3 = Tex(r"Charge: +1 e").next_to(tex2, DOWN).align_to(tex1, LEFT)
        animations = [
            Write(tex1),
            Wait(),
            Write(tex2),
            Wait(),
            Write(tex3)
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))


class ProtonDELETE(Scene):
    def construct(self):
        # Reconstruct scene
        proton = Circle(
            radius=1.0,
            color=RED,
        ).move_to(RIGHT * 3)
        proton.set_fill(RED, opacity=0.5)

        tex1 = Tex(r"\underline{Proton}").to_corner(LEFT + UP)
        tex2 = Tex(
            r"Mass: $1.673\times10^{-27}$ kg").next_to(tex1, DOWN).align_to(tex1, LEFT)
        tex3 = Tex(r"Charge: +1 e").next_to(tex2, DOWN).align_to(tex1, LEFT)
        self.add(proton, tex1, tex2, tex3)
        self.play(FadeOut(VGroup(*self.mobjects)))


class Neutron(Scene):
    def construct(self):
        # Create neutron
        neutron = Circle(
            radius=1.0,
            color=GREEN,
        )
        neutron.set_fill(GREEN, opacity=0.5)
        self.play(Create(neutron))
        self.play(Wait())

        # Move neutron to right and display some info
        self.play(neutron.animate.move_to(RIGHT * 3))
        tex1 = Tex(r"\underline{Neutron}").to_corner(LEFT + UP)
        tex2 = Tex(r"Mass: $1.675\times10^{-27}$ kg").next_to(tex1, DOWN).align_to(tex1, LEFT)
        tex3 = Tex(r"Charge: 0 e").next_to(tex2, DOWN).align_to(tex1, LEFT)
        animations = [
            Write(tex1),
            Wait(),
            Write(tex2),
            Wait(),
            Write(tex3)
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))


class NeutronDELETE(Scene):
    def construct(self):
        # Create neutron
        neutron = Circle(
            radius=1.0,
            color=GREEN,
        ).move_to(RIGHT * 3)
        neutron.set_fill(GREEN, opacity=0.5)
        tex1 = Tex(r"\underline{Neutron}").to_corner(LEFT + UP)
        tex2 = Tex(
            r"Mass: $1.675\times10^{-27}$ kg").next_to(tex1, DOWN).align_to(tex1, LEFT)
        tex3 = Tex(r"Charge: 0 e").next_to(tex2, DOWN).align_to(tex1, LEFT)
        self.add(neutron, tex1, tex2, tex3)
        self.play(FadeOut(VGroup(*self.mobjects)))


class Electron(Scene):
    def construct(self):
        # Create electron
        electron = Circle(
            radius=0.35,
            color=BLUE,
        )
        electron.set_fill(BLUE, opacity=0.5)
        self.play(Create(electron))
        self.play(Wait())

        # Move electron to right and display some info
        self.play(electron.animate.move_to(RIGHT * 3))
        tex1 = Tex(r"\underline{Electron}").to_corner(LEFT + UP)
        tex2 = Tex(r"Mass: $9.109\times10^{-31}$ kg").next_to(tex1, DOWN).align_to(tex1, LEFT)
        tex3 = Tex(r"Charge: -1 e").next_to(tex2, DOWN).align_to(tex1, LEFT)
        animations = [
            Write(tex1),
            Wait(),
            Write(tex2),
            Wait(),
            Write(tex3)
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))


class ElectronDELETE(Scene):
    def construct(self):
        # Reconstuct scene
        electron = Circle(
            radius=1.0,
            color=BLUE,
        ).move_to(RIGHT * 3)
        electron.set_fill(BLUE, opacity=0.5)
        tex1 = Tex(r"\underline{Electron}").to_corner(LEFT + UP)
        tex2 = Tex(
            r"Mass: $9.109\times10^{-31}$ kg").next_to(tex1, DOWN).align_to(tex1, LEFT)
        tex3 = Tex(r"Charge: -1 e").next_to(tex2, DOWN).align_to(tex1, LEFT)
        self.add(electron, tex1, tex2, tex3)
        self.play(FadeOut(VGroup(*self.mobjects)))


class KgToMeV(Scene):
    def construct(self):
        # Make proton and associated text
        proton = Circle(
            radius=1.0,
            color=RED,
        )
        proton.set_fill(RED, opacity=0.5)
        proton.shift(UP)
        proton.to_edge(LEFT)
        proton.shift(RIGHT)
        tex_p1 = Tex(r"\underline{Proton}").next_to(proton, UP)
        tex_p2 = Tex(r"$1.673\text{e-}27$ kg").next_to(proton, DOWN)
        # Make neutron and associated text
        neutron = Circle(
            radius=1.0,
            color=GREEN,
        )
        neutron.set_fill(GREEN, opacity=0.5)
        neutron.shift(UP)
        tex_n1 = Tex(r"\underline{Neutron}").next_to(neutron, UP)
        tex_n2 = Tex(r"$1.675\text{e-}27$ kg").next_to(neutron, DOWN)
        # Make electron and associated text
        electron = Circle(
            radius=0.35,
            color=BLUE,
        )
        electron.set_fill(BLUE, opacity=0.5)
        electron.shift(UP)
        electron.to_edge(RIGHT)
        electron.shift(LEFT)
        tex_e1 = Tex(r"\underline{Electron}").next_to(electron, UP).align_to(tex_p1, DOWN)
        tex_e2 = Tex(r"$9.109\text{e-}31$ kg").next_to(electron, DOWN).align_to(tex_p2, DOWN)
        # Populate screen
        self.play(
            Create(proton),
            Write(tex_p1),
            Create(neutron),
            Write(tex_n1),
            Create(electron),
            Write(tex_e1)
        )
        self.wait(3)
        self.play(
            Write(tex_p2),
            Write(tex_n2),
            Write(tex_e2)
        )
        self.wait(2)

        # Show Einstein
        einstein_pic = ImageMobject("assets/Einstein.jpg").scale(0.25).shift(UP * 0.5)
        einstein_border = SurroundingRectangle(
            einstein_pic,
            color=YELLOW,
            buff=0.0
        )
        self.play(FadeIn(einstein_pic), FadeIn(einstein_border))
        self.wait(3)
        # Show E=mc2
        tex_emc = Tex(r"$E=mc^{2}$").to_edge(DOWN)
        self.play(Write(tex_emc))
        self.wait(3)
        # Remove einstein
        self.play(FadeOut(einstein_pic), FadeOut(einstein_border))
        self.wait()

        # Remove neutron and electron
        not_proton_grp = VGroup(
            neutron,
            tex_n1,
            tex_n2,
            electron,
            tex_e1,
            tex_e2
        )
        self.play(FadeOut(not_proton_grp))

        # Set up MeV calculation
        line = Line(start=[tex_p2.get_right()[0] + 0.5, -10, 0], end=[tex_p2.get_right()[0] + 0.5, 10, 0])
        tex_emp1 = Tex(r"$E=m_{p}c^{2}$").shift(LEFT).align_to(tex_p1, DOWN)
        self.play(Transform(tex_emc, tex_emp1), FadeIn(line))
        self.wait(2)
        tex_emp2 = Tex(r"$E=(1.673\text{e-}27\text{ kg})c^{2}$").shift(LEFT).next_to(tex_emp1, DOWN).align_to(tex_emp1, LEFT)
        self.play(Transform(tex_emp1.copy(), tex_emp2))
        self.wait(2)
        tex_emp3 = Tex(r"$E=1.503\text{e-}10\text{ J}$").shift(LEFT).next_to(tex_emp2, DOWN).align_to(tex_emp1, LEFT)
        self.play(Transform(tex_emp2.copy(), tex_emp3))
        self.wait(2)
        tex_j_to_mev = Tex(r"$1\text{ J}=6.242\text{e+}18\text{ eV}$").to_edge(DOWN).align_to(tex_emp1, LEFT)
        tex_j_to_mev_box = SurroundingRectangle(tex_j_to_mev, color=YELLOW, buff=SMALL_BUFF)
        self.play(Write(tex_j_to_mev), FadeIn(tex_j_to_mev_box))

        # eV animation
        left_line = Line(
            start=[tex_j_to_mev.get_right()[0] + 0.75, tex_j_to_mev.get_right()[1], 0],
            end=[tex_j_to_mev.get_right()[0] + 0.75, -1.5, 0]
        )
        right_line = Line(
            start=[tex_j_to_mev.get_right()[0] + 4.0, tex_j_to_mev.get_right()[1], 0],
            end=[tex_j_to_mev.get_right()[0] + 4.0, -1.5, 0]
        )
        eV_animation_background = Rectangle(
            width=(right_line.get_x() - left_line.get_x()),
            height=left_line.height,
            stroke_width=0.0
        ).set_fill(color=[RED,YELLOW], opacity=0.3)
        eV_animation_background.next_to(left_line, RIGHT, buff=0.0)
        left_line_label = Tex("0 V", color=YELLOW).next_to(left_line, UP)
        right_line_label = Tex("1 V", color=RED).next_to(right_line, UP)
        e_dot = Dot(
            [left_line.get_left()[0], left_line.get_center()[1], 0],
            radius=0.15,
            color=BLUE
        )
        self.play(FadeIn(eV_animation_background), FadeIn(left_line), FadeIn(right_line), Write(left_line_label), Write(right_line_label))
        self.wait(2)
        eV_label = VGroup(
            Tex(r"$KE_{e}$ = "),
            DecimalNumber(
                0,
                show_ellipsis=False,
                num_decimal_places=2,
                include_sign=False,
            ),
            Tex(r" eV")
        ).arrange(RIGHT)
        eV_label.set_y(tex_p2.get_center()[2])
        eV_label.set_x((left_line.get_center()[0] + right_line.get_center()[0]) / 2)
        self.wait(2)
        eV_label[1].add_updater(
            lambda m: m.set_value(
                (e_dot.get_x() - left_line.get_x()) / (right_line.get_x() - left_line.get_x()))
        )
        self.play(Write(eV_label))
        self.wait(2)
        self.play(
            e_dot.animate.shift([right_line.get_x() - left_line.get_x(), 0, 0]),
            rate_func=rate_functions.rush_into,
            run_time=4,
        )
        self.wait(4)
        e_dot.set_x(left_line.get_x())
        self.play(
            e_dot.animate.shift(
                [right_line.get_x() - left_line.get_x(), 0, 0]),
            rate_func=rate_functions.rush_into,
            run_time=4,
        )
        self.wait(3)

        # Clear eV animation
        self.play(
            FadeOut(left_line),
            FadeOut(left_line_label),
            FadeOut(right_line),
            FadeOut(right_line_label),
            FadeOut(eV_animation_background),
            FadeOut(eV_label),
            FadeOut(e_dot)
        )
        self.wait(2)
        tex_emp4 = Tex(r"$E=9.383\text{e+}8\text{ eV}$").shift(LEFT).next_to(tex_emp3, DOWN).align_to(tex_emp1, LEFT)
        self.play(Transform(tex_emp3.copy(), tex_emp4))
        self.wait(3)
        tex_emp5 = Tex(r"$E=938.3\text{ MeV}$").shift(LEFT).next_to(tex_emp4, DOWN).align_to(tex_emp1, LEFT)
        self.play(Transform(tex_emp4.copy(), tex_emp5))
        self.wait(3)
        tex_p2 = Tex(r"$m_{p}=\frac{938.3\text{ MeV}}{c^{2}}$").shift(LEFT).next_to(tex_emp5, DOWN).align_to(tex_emp1, LEFT)
        self.play(Transform(tex_emp5.copy(), tex_p2))
        self.wait(5)

        # Shift results onto proton
        tex_emp_final = Tex(r"$938.3\text{ MeV}$").next_to(proton, DOWN)
        # So janky??
        proton_grp = VGroup(
            proton,
            tex_p1,
            tex_p2
        )
        animations = list()
        for obj in self.mobjects:
            if obj not in proton_grp:
                animations.append(
                    FadeOut(obj)
                )
        animations.append(Transform(tex_p2, tex_emp_final))
        self.play(AnimationGroup(*animations))

        # Bring back neutron and electron with results
        tex_n2 = Tex(r"$939.6\text{ MeV}$").next_to(neutron, DOWN)
        tex_e2 = Tex(r"$0.511\text{ MeV}$").next_to(electron, DOWN).align_to(tex_p2, DOWN)
        self.play(
            FadeIn(neutron),
            FadeIn(tex_n1),
            FadeIn(tex_n2),
            FadeIn(electron),
            FadeIn(tex_e1),
            FadeIn(tex_e2)
        )

