from manim import *


class AtomsTitleCard(Scene):
    def construct(self):
        section_title = Tex("Introduction to atoms")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class Proton(Scene):
    def construct(self):
        # Create proton
        proton = Circle(
            radius=1.0,
            color=RED,
        )
        proton.set_fill(RED, opacity=0.5)
        self.play(GrowFromCenter(proton))
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
        self.play(AnimationGroup(*animations, lag_ratio=1.0))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class Electron(Scene):
    def construct(self):
        # Create electron
        electron = Circle(
            radius=0.35,
            color=BLUE,
        )
        electron.set_fill(BLUE, opacity=0.5)
        self.play(GrowFromCenter(electron))
        self.play(Wait())

        # Move electron to right and display some info
        self.play(electron.animate.move_to(RIGHT * 3))
        tex1 = Tex(r"\underline{Electron}").to_corner(LEFT + UP)
        tex2 = Tex(
            r"Mass: $9.109\times10^{-31}$ kg").next_to(tex1, DOWN).align_to(tex1, LEFT)
        tex3 = Tex(r"Charge: -1 e").next_to(tex2, DOWN).align_to(tex1, LEFT)
        animations = [
            Write(tex1),
            Wait(),
            Write(tex2),
            Wait(),
            Write(tex3)
        ]
        self.play(AnimationGroup(*animations, lag_ratio=1.0))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class Neutron(Scene):
    def construct(self):
        # Create neutron
        neutron = Circle(
            radius=1.0,
            color=GREEN,
        )
        neutron.set_fill(GREEN, opacity=0.5)
        self.play(GrowFromCenter(neutron))
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
        self.play(AnimationGroup(*animations, lag_ratio=1.0))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


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
            GrowFromCenter(proton),
            Write(tex_p1),
            GrowFromCenter(neutron),
            Write(tex_n1),
            GrowFromCenter(electron),
            Write(tex_e1)
        )
        self.wait()
        self.play(
            Write(tex_p2),
            Write(tex_n2),
            Write(tex_e2)
        )
        self.wait()

        # Show Einstein
        einstein_pic = ImageMobject("assets/Einstein.jpg").scale(0.25).shift(UP * 0.5)
        einstein_border = SurroundingRectangle(
            einstein_pic,
            color=YELLOW,
            buff=0.0
        )
        self.play(FadeIn(einstein_pic), FadeIn(einstein_border))
        self.wait()

        # Show E=mc2
        tex_emc = Tex(r"$E=mc^{2}$").to_edge(DOWN)
        self.play(Write(tex_emc))
        self.wait()

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
        self.wait()
        tex_emp2 = Tex(r"$E=(1.673\text{e-}27\text{ kg})\cdot c^{2}$").shift(LEFT).next_to(tex_emp1, DOWN).align_to(tex_emp1, LEFT)
        self.play(Transform(tex_emp1.copy(), tex_emp2))
        self.wait()
        tex_emp3 = Tex(r"$E=1.503\text{e-}10\text{ J}$").shift(LEFT).next_to(tex_emp2, DOWN).align_to(tex_emp1, LEFT)
        self.play(Transform(tex_emp2.copy(), tex_emp3))
        self.wait()
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
        right_line_label = Tex("+1 V", color=RED).next_to(right_line, UP)
        e_dot = Dot(
            [left_line.get_left()[0], left_line.get_center()[1], 0],
            radius=0.15,
            color=BLUE
        )
        self.add_foreground_mobject(e_dot)
        self.play(FadeIn(eV_animation_background), FadeIn(left_line), FadeIn(right_line), FadeIn(e_dot), Write(left_line_label), Write(right_line_label))
        self.wait()
        eV_label = VGroup(
            Tex(r"$\text{KE}_{e}$ = "),
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
        self.wait()
        eV_label[1].add_updater(
            lambda m: m.set_value(
                (e_dot.get_x() - left_line.get_x()) / (right_line.get_x() - left_line.get_x()))
        )
        self.play(Write(eV_label))
        self.wait()
        self.play(
            e_dot.animate.shift([right_line.get_x() - left_line.get_x(), 0, 0]),
            rate_func=rate_functions.rush_into,
            run_time=4,
        )
        self.wait()
        self.play(FadeOut(e_dot))
        self.wait()
        e_dot.set_x(left_line.get_left()[0])
        self.play(FadeIn(e_dot))
        self.wait()
        self.play(
            e_dot.animate.shift(
                [right_line.get_x() - left_line.get_x(), 0, 0]),
            rate_func=rate_functions.rush_into,
            run_time=4,
        )
        self.wait()

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
        self.wait()
        tex_emp4 = Tex(r"$E=9.383\text{e+}8\text{ eV}$").shift(LEFT).next_to(tex_emp3, DOWN).align_to(tex_emp1, LEFT)
        self.play(Transform(tex_emp3.copy(), tex_emp4))
        self.wait()
        tex_emp5 = Tex(r"$E=938.3\text{ MeV}$").shift(LEFT).next_to(tex_emp4, DOWN).align_to(tex_emp1, LEFT)
        self.play(Transform(tex_emp4.copy(), tex_emp5))
        self.wait()
        tex_p2 = Tex(r"$m_{p}=\frac{938.3\text{ MeV}}{c^{2}}$").shift(LEFT).next_to(tex_emp5, DOWN).align_to(tex_emp1, LEFT)
        self.play(Transform(tex_emp5.copy(), tex_p2))
        self.wait()

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
        self.wait()

        # Clear screen
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class AtomicStructure(Scene):
    def construct(self):
        # Helper function to make protons
        def proton():
            proton = Circle(
                radius=0.35,
                color=RED,
            ).set_fill("#7d3129", opacity=1.0)
            return proton

        # Helper function to make neutrons
        def neutron():
            neutron = Circle(
                radius=0.35,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0)
            return neutron

        # Helper function to make electrons
        def electron():
            electron = Circle(
                radius=0.12,
                color=BLUE,
            ).set_fill("#2c626e", opacity=1.0)
            return electron

        # Helper function to make electron cloud
        def electron_cloud(inner_radius, outer_radius):
            electron_cloud = VGroup()
            electron_cloud_linspace = np.linspace(inner_radius, outer_radius, 100)
            for i in range(0, len(electron_cloud_linspace)-1):
                electron_cloud.add(
                    Annulus(
                        inner_radius=electron_cloud_linspace[i],
                        outer_radius=electron_cloud_linspace[i + 1],
                        stroke_width=0.0,
                        fill_opacity=0.5,
                        color=WHITE
                    )
                )
            electron_cloud.set_color_by_gradient(BLACK, BLUE, BLACK)
            return electron_cloud

        # Build a nucleus
        he3_p1 = proton()
        he3_p2 = proton()
        he3_n = neutron()
        he3_e1 = electron()
        he3_e2 = electron()
        he3_comps = VGroup(
            he3_p1,
            he3_p2,
            he3_n,
            he3_e1,
            he3_e2
        ).arrange(RIGHT, buff=LARGE_BUFF).shift(UP * 2)
        self.play(Create(he3_comps))
        self.wait()
        animations = [
            he3_p2.animate.move_to([he3_p2.radius, np.sqrt(3)/2*he3_p2.radius, 0]),
            Wait(),
            he3_p1.animate.move_to([-he3_p1.radius, np.sqrt(3)/2*he3_p1.radius, 0]),
            Wait(),
            he3_n.animate.move_to([0, -np.sqrt(3)/2*he3_n.radius, 0]),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5, run_time=5))
        nucleus_label = Tex(r"\underline{Nucleus}").next_to(he3_n, DOWN)
        self.play(Write(nucleus_label))
        self.wait()
        self.play(FadeOut(nucleus_label))
        self.wait()

        # Show electrons orbiting
        orbit_1 = Ellipse(width=4.0, height=2.0, color=BLUE_B, stroke_width=1.5).rotate(np.pi/4)
        orbit_2 = Ellipse(width=4.0, height=2.0, color=BLUE_B, stroke_width=1.5).rotate(3*np.pi/4)
        he3_e1_new = electron().move_to([0.5 * orbit_1.height * np.sin(np.pi / 3), 0.5 * orbit_1.height * np.cos(np.pi / 6), 0])
        he3_e2_new = electron().move_to([-0.5 * orbit_2.height * np.sin(np.pi / 3), 0.5 * orbit_2.height * np.cos(np.pi / 6), 0])
        self.bring_to_back(orbit_1)
        self.bring_to_back(orbit_2)
        self.play(
            DrawBorderThenFill(orbit_1),
            DrawBorderThenFill(orbit_2),
            Transform(he3_e1, he3_e1_new),
            Transform(he3_e2, he3_e2_new)
        )
        self.wait()
        self.play(
            MoveAlongPath(he3_e1, orbit_1),
            MoveAlongPath(he3_e2, orbit_2),
            run_time=5,
            rate_func=rate_functions.ease_in_out_quart
        )
        self.wait()

        # Show electron cloud
        self.play(
            FadeOut(he3_e1),
            FadeOut(he3_e2),
            FadeOut(orbit_1),
            FadeOut(orbit_2)
        )
        self.wait()
        he3_electron_cloud = electron_cloud(inner_radius=0.85, outer_radius=2.5)
        self.play(FadeIn(he3_electron_cloud))
        self.wait()

        # Move to he3 to the left
        he3_nucleus = VGroup(he3_p1, he3_p2, he3_n)
        he3 = VGroup(he3_nucleus, he3_electron_cloud)
        self.play(Transform(he3, he3.copy().scale(0.8).to_edge(LEFT).shift(DOWN)))
        self.wait()

        # Describe isotope notation
        he3_label = Tex(r"$^A_ZX$")
        self.play(Write(he3_label))
        self.wait()
        X_arrow = Arrow(start=[he3_label.get_right()[0] + 1.65, he3_label.get_center()[1], 0], end=[he3_label.get_right()[0], he3_label.get_center()[1], 0], stroke_width=1)
        X_label = Tex(r"Chemical symbol", font_size=40).next_to(X_arrow, RIGHT)
        self.play(
            GrowArrow(X_arrow),
            Write(X_label)
        )
        self.wait()
        self.play(Transform(he3_label, Tex(r"$^A_Z\text{He}$")))
        self.wait()
        Z_arrow = Arrow(start=[he3_label.get_left()[0] + 0.15, he3_label.get_bottom()[1] - 1.5, 0], end=[he3_label.get_left()[0] + 0.15, he3_label.get_bottom()[1], 0], stroke_width=1)
        Z_label = Tex(r"\# of protons", font_size=40).next_to(Z_arrow, DOWN)
        self.play(
            GrowArrow(Z_arrow),
            Write(Z_label)
        )
        self.wait()
        self.play(Transform(he3_label, Tex(r"$^A_2\text{He}$")))
        self.wait()
        A_arrow = Arrow(start=[he3_label.get_left()[0] + 0.15, he3_label.get_top()[1] + 1.5, 0], end=[he3_label.get_left()[0] + 0.15, he3_label.get_top()[1], 0], stroke_width=1)
        A_label = Tex(r"\# of nucleons (neutrons + protons)", font_size=40).next_to(A_arrow, UP)
        self.play(
            GrowArrow(A_arrow),
            Write(A_label)
        )
        self.wait()
        self.play(Transform(he3_label, Tex(r"$^3_2\text{He}$")))
        self.wait()
        self.play(
            Transform(he3_label, Tex(r"$^3_2\text{He}$").next_to(he3, UP)),
            FadeOut(X_arrow),
            FadeOut(X_label),
            FadeOut(Z_arrow),
            FadeOut(Z_label),
            FadeOut(A_arrow),
            FadeOut(A_label)
        )
        he3_name = Tex(r"\underline{Helium-3}").next_to(he3_label, UP)
        self.play(Write(he3_name))
        self.wait()

        # Talk about elements and isotopes
        isotope_description = Tex(
            r"\begin{tabular}{@{}l@{}c@{\hspace{0.5em}}l@{}}"
            r"Isotopes & : & Distinct types of the \\"
            r"& & same element, distinguished \\"
            r"& & by their mass number."
            r"\end{tabular}",
            font_size=40
        ).align_to(he3_name, UP).shift(RIGHT * 2)
        isotope_description_box = SurroundingRectangle(isotope_description, color=YELLOW, buff=SMALL_BUFF)
        same_p = Tex("Same number of protons", font_size=40).next_to(isotope_description, DOWN * 2)
        diff_n = Tex("different number of neutrons!", font_size=40).next_to(same_p, DOWN)
        self.play(
            DrawBorderThenFill(isotope_description_box),
            Write(isotope_description)
        )
        self.wait()
        self.play(
            Write(same_p),
            Write(diff_n)
        )
        self.wait()
        self.play(
            FadeOut(isotope_description_box),
            FadeOut(isotope_description),
            FadeOut(same_p),
            FadeOut(diff_n)
        )
        self.wait()

        # Helium 4 example
        he4_p1 = proton().move_to([-he3_p1.radius, he3_p1.radius, 0])
        he4_p2 = proton().move_to([he3_p1.radius, -he3_p1.radius, 0])
        he4_n1 = neutron().move_to([he3_p1.radius, he3_p1.radius, 0])
        he4_n2 = neutron().move_to([-he3_p1.radius, -he3_p1.radius, 0])
        he4_nucleus = VGroup(he4_p1, he4_p2, he4_n1, he4_n2).rotate(np.pi/4)
        he4_electron_cloud = electron_cloud(inner_radius=0.85, outer_radius=2.5)
        he4 = VGroup(he4_nucleus, he4_electron_cloud).scale(0.8).set_y(he3.get_center()[1])
        he4_label = Tex(r"$^4_2\text{He}$").next_to(he4, UP)
        he4_name = Tex(r"\underline{Helium-4}").next_to(he4_label, UP)
        self.play(
            FadeIn(he4),
            FadeIn(he4_label),
            FadeIn(he4_name),
        )
        self.wait()

        # Lithium 7 example
        li7_p1 = proton().move_to([-2 * he3_p1.radius, 0, 0])
        li7_p2 = proton()
        li7_p3 = proton().move_to([2 * he3_p1.radius, 0, 0])
        li7_n1 = neutron().move_to([-he3_p1.radius, np.sqrt(3)*he3_p1.radius, 0])
        li7_n2 = neutron().move_to([he3_p1.radius, np.sqrt(3)*he3_p1.radius, 0])
        li7_n3 = neutron().move_to([-he3_p1.radius, -np.sqrt(3)*he3_p1.radius, 0])
        li7_n4 = neutron().move_to([he3_p1.radius, -np.sqrt(3)*he3_p1.radius, 0])
        li7_nucleus = VGroup(li7_p1, li7_p2, li7_p3, li7_n1, li7_n2, li7_n3, li7_n4)
        li7_electron_cloud = electron_cloud(inner_radius=1.2, outer_radius=3.0)
        li7 = VGroup(li7_nucleus, li7_electron_cloud).scale(0.75).to_edge(RIGHT).set_y(he3.get_center()[1])
        li7_label = Tex(r"$^7_3\text{Li}$").next_to(li7, UP)
        li7_name = Tex(r"\underline{Lithium-7}").next_to(li7_label, UP)
        self.play(
            FadeIn(li7),
            FadeIn(li7_label),
            FadeIn(li7_name),
        )
        self.wait()

        # Clear screen
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
