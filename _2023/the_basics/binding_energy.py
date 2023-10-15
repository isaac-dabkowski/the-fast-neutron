from manim import *

def create_BE_data():
    """
    Generates BE/A data for many different nuclides.
    """
    def calc_BE_A(Z, N):
        """
        Calculate binding energy per nucleon for a given
        number of protons and neutrons with the SEMF
        """
        # Mass of proton and neutron in amu
        m_p = 1.007276
        m_n = 1.008665
        # MeV per amu
        c_2 = 931.494
        # SEMF coefficients
        a_V = 15.835
        a_S = 18.33
        a_C = 0.714
        a_A = 23.2
        a_P = 11.2

        # Atomic number
        A = Z + N
        # Initialize bindign energy
        BE = 0

        # Volume term
        vol = a_V * A
        BE += vol

        # Surface term
        surf = a_S * A ** (2 / 3)
        BE -= surf

        # Coulomb term
        col = a_C * (Z * (Z - 1)) / A ** (1 / 3)
        BE -= col

        # Asymmetry term
        asym = a_A * (A - 2 * Z) ** 2 / A
        BE -= asym

        # Pairing term
        if Z % 2 == 0 and N % 2 == 0:
            delta = 1
        elif Z % 2 == 1 and N % 2 == 1:
            delta = -1
        else:
            delta = 0
        pair = delta * a_P / A ** (1 / 2)
        BE += pair

        return BE / A
    BE_A = dict()
    A_max = 250
    # Loop over all mass numbers
    for A in range(1, A_max + 1):
        BE_A[A] = list()
        # Loop over all possible combinations of
        # neutrons and protons for the given mass number
        for Z in range(1, A + 1):
            N = A - Z
            be_per_a = calc_BE_A(Z=Z, N=N)
            # Cutoff to not include insane results
            if be_per_a > (4/A_max)*A + 1.8:
                BE_A[A].append((Z, be_per_a))
    return BE_A


class BindingEnergyTitleCard(Scene):
    def construct(self):
        section_title = Tex("Nuclear binding energy and the semi-empirical mass formula")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class MassDefect(Scene):
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

        # Start with nucleons apart from one another
        he4_p1 = proton()
        he4_p2 = proton()
        he4_n1 = neutron()
        he4_n2 = neutron()
        he4 = VGroup(he4_p1, he4_p2, he4_n1, he4_n2).arrange(RIGHT, buff=LARGE_BUFF)
        self.play(GrowFromCenter(he4))
        self.wait()

        # Arrange into nucleus
        self.play(
            he4_p1.animate.move_to([-he4_p1.radius, he4_p1.radius, 0]),
            he4_p2.animate.move_to([he4_p1.radius, -he4_p1.radius, 0]),
            he4_n1.animate.move_to([he4_p1.radius, he4_p1.radius, 0]),
            he4_n2.animate.move_to([-he4_p1.radius, -he4_p1.radius, 0])
        )
        self.play(he4.animate.rotate(np.pi/4))
        self.wait()

        # Predicted mass of nucleus
        tex = Tex(r"\underline{What would you expect the mass of the $^4$He nucleus to be?}").to_edge(UP)
        self.play(Write(tex))
        self.wait()
        self.play(he4.animate.to_edge(LEFT))
        self.wait()
        mp_mn = Tex(r"$m_p = 1.007278$ amu, $m_n = 1.008665$ amu").next_to(tex, DOWN)
        amu_kg = Tex(r"$1\text{ amu} = 1.66054\text{e-}27\text{ kg}$").next_to(mp_mn, DOWN)
        he_mass_calc = VGroup(
            Tex(r"$M\left(^4\text{He}\right)=Z\cdot m_p + (A-Z)\cdot m_n$"),
            Tex(r"$M\left(^4\text{He}\right)=2\cdot m_p + 2\cdot m_n$"),
            Tex(r"$M\left(^4\text{He}\right)=2\cdot (1.007278\text{ u}) + 2\cdot(1.008665\text{ u})$"),
            Tex(r"$M\left(^4\text{He}\right)=4.031883\text{ u}$")
        ).arrange(DOWN, buff=MED_SMALL_BUFF, center=False, aligned_edge=LEFT).next_to(amu_kg, DOWN * 3).shift(RIGHT)
        self.play(Write(mp_mn))
        self.wait()
        self.play(Write(amu_kg))
        self.wait()
        for m in he_mass_calc:
            self.play(Write(m))
            self.wait()
        predicted_mass = he_mass_calc[-1].copy()
        self.play(
            FadeOut(he_mass_calc),
            FadeOut(mp_mn),
            FadeOut(amu_kg),
            Transform(
                predicted_mass,
                Tex("Predicted mass = 4.031883 u").next_to(tex, DOWN * 2)
            )
        )
        self.wait()

        # Reveal actual mass and mass defect
        actual_mass = Tex("Actual mass = 4.001506 u").next_to(predicted_mass, DOWN * 2).align_to(predicted_mass, RIGHT)
        self.play(Write(actual_mass))
        self.wait()
        mass_defect = Tex(r"$\Delta$m = 0.030377 u").next_to(actual_mass, DOWN * 2).align_to(actual_mass, RIGHT)
        self.play(Write(mass_defect))
        self.wait()
        self.play(Transform(mass_defect, Tex("Mass defect = 0.030377 u").next_to(actual_mass, DOWN * 2).align_to(actual_mass, RIGHT)))
        self.wait()

        # Discuss connection between mass defect and binding energy
        md_be =  VGroup(
            Tex("The nucleus is in a stable"),
            Tex("configuration, it would take"),
            Tex("energy input to pull it apart.")
        ).arrange(DOWN, buff=MED_SMALL_BUFF).next_to(mass_defect, DOWN).to_edge(DOWN)
        self.play(Write(md_be))
        self.wait()
        self.play(FadeOut(predicted_mass), FadeOut(actual_mass), mass_defect.animate.next_to(tex, DOWN))
        self.wait()
        einstein_pic = ImageMobject("assets/Einstein.jpg").scale(0.15).shift(DOWN * 0.5)
        einstein_border = SurroundingRectangle(
            einstein_pic,
            color=YELLOW,
            buff=0.0
        )
        self.play(FadeOut(md_be), FadeIn(einstein_pic), FadeIn(einstein_border))
        self.wait()
        be = Tex(r"$E=mc^{2}$").next_to(einstein_border, DOWN)
        self.play(Write(be))
        self.wait()
        self.play(FadeOut(einstein_pic), FadeOut(einstein_border))
        self.wait()
        self.play(Transform(be, Tex(r"$\text{BE}=\Delta m \cdot c^2$").next_to(mass_defect, DOWN * 3.0)))
        self.wait()
        self.play(Transform(be, Tex(r"$\text{BE}=\Delta m \cdot c^2=28.296\text{ MeV}$").next_to(mass_defect, DOWN * 3.0)))
        self.wait()

        # Hint at SEMF
        self.play(FadeOut(mass_defect), FadeOut(be))
        self.wait()
        semf = Tex(r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n$").shift(RIGHT)
        self.play(Write(semf))
        self.wait()
        wrong_line = Line(semf.get_left(), semf.get_right(), color=RED)
        self.play(
            Transform(semf, Tex(r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n$", color=RED).shift(RIGHT)),
            Create(wrong_line)
        )
        self.wait()
        self.play(
            Transform(semf, Tex(
                r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n - \frac{\text{BE(A, Z)}}{c^2}$").shift(RIGHT)),
            FadeOut(wrong_line)
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class SEMFAnimation(Scene):
    def construct(self):
        # Helper function to make protons
        def proton():
            proton = Circle(
                radius=0.5,
                color=RED,
            ).set_fill("#7d3129", opacity=1.0)
            return proton

        # Helper function to make neutrons
        def neutron():
            neutron = Circle(
                radius=0.5,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0)
            return neutron

        # Display section title and equation
        tex = Tex(r"\underline{The semi-empirical mass formula}").to_edge(UP)
        self.play(Write(tex))
        self.wait()
        semf = Tex(r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n - \frac{\text{BE(A, Z)}}{c^2}$")
        self.play(Write(semf))
        self.wait()
        self.play(FadeOut(semf))
        self.wait()

        # Display binding enegy eq
        be = MathTex("\\text{BE}(A, Z)=", "a_VA", "-", "a_SA^{2/3}", "-", "a_c\\frac{Z(Z-1)}{A^{1/3}}", "-", "a_A\\frac{(A-2Z)^2}{A}", "+", "\\delta(A, Z)a_PA^{-1/2}", font_size=38)
        self.play(Write(be))
        self.wait()
        self.play(be.animate.next_to(tex, DOWN * 1.5))
        self.wait()

        # Display a key real quick
        symkey = VGroup(
            Tex(r"$A=\text{Mass number (\# protons + \# neutrons)}$"),
            Tex(r"$Z=\text{Atomic number (\# protons)}$"),
            Tex(r"$a_V, a_C, a_A, a_P=\text{Experimentally determined coefficients}$")
        ).arrange(DOWN, buff=MED_LARGE_BUFF, center=False, aligned_edge=LEFT).shift(UP * 0.5 + LEFT * 0.5)
        self.play(Write(symkey))
        self.wait()
        self.play(FadeOut(symkey))
        self.wait()

        # Draw a line across screen
        line = Line([-10, be.get_bottom()[1] - 0.25, 0], [10, be.get_bottom()[1] - 0.25, 0])
        self.play(Create(line))
        self.wait()

        # Make a nucleus
        nuc = ImageMobject("assets/random_nucleus.png").to_edge(RIGHT).shift(LEFT * 0.5 + DOWN)
        self.play(
            GrowFromCenter(nuc)
        )
        self.wait()

        # Volume term
        volframe = SurroundingRectangle(be[1], buff = .1)
        termname = Tex(r"\underline{\textit{Volume term}}").next_to(be, DOWN * 3.0).shift(LEFT * 3)
        termtex = Tex(r"$a_VA$").next_to(termname, DOWN)
        termdesc = Tex(r"Decribes strong force\\between neighboring nucleons").next_to(termtex, DOWN * 2)
        arrows = VGroup(
            Arrow(start=[5.05, -0.75, 0], end=[4.9, -1.35, 0], buff=0.0),
            Arrow(start=[5.05, -0.75, 0], end=[5.5, -1.25, 0], buff=0.0),
            Arrow(start=[5.05, -0.75, 0], end=[5.7, -0.65, 0], buff=0.0),
            Arrow(start=[5.05, -0.75, 0], end=[5.25, -0.15, 0], buff=0.0),
            Arrow(start=[5.05, -0.75, 0], end=[4.63, -0.08, 0], buff=0.0),
            Arrow(start=[5.05, -0.75, 0], end=[4.4, -0.75, 0], buff=0.0),
        )
        coefftex = Tex(r"$a_V\approx15.835\text{ MeV}$").next_to(termdesc, DOWN * 2)
        term_grp = VGroup(
            termname,
            termtex,
            termdesc,
            arrows,
            coefftex
        )
        self.play(Create(volframe))
        self.wait()
        self.play(Write(termname))
        self.wait()
        self.play(Write(termtex))
        self.wait()
        self.play(Write(termdesc))
        self.wait()
        self.play(Create(arrows))
        self.wait()
        self.play(Write(coefftex))
        self.wait()
        self.play(FadeOut(term_grp))
        self.wait()

        # Surface term
        surfframe = SurroundingRectangle(be[3], buff=.1)
        self.play(ReplacementTransform(volframe, surfframe))
        termname = Tex(r"\underline{\textit{Surface term}}").next_to(be, DOWN * 3.0).shift(LEFT * 3)
        termtex = Tex(r"$a_SA^{2/3}$").next_to(termname, DOWN)
        termdesc = Tex(r"Decribes how nucleons on nucleus's\\surface have fewer neighbors").next_to(termtex, DOWN * 2)
        coefftex = Tex(r"$a_S\approx18.33\text{ MeV}$").next_to(termdesc, DOWN * 2)
        arrows = VGroup(
            Arrow(start=[5.7, -0.65, 0], end=[5.05, -0.75, 0], buff=0.0),
            Arrow(start=[5.7, -0.65, 0], end=[5.5, -1.25, 0], buff=0.0),
            Arrow(start=[5.7, -0.65, 0], end=[5.25, -0.15, 0], buff=0.0),
        )
        term_grp = VGroup(
            termname,
            termtex,
            termdesc,
            arrows,
            coefftex
        )
        self.play(Write(termname))
        self.wait()
        self.play(Write(termtex))
        self.wait()
        self.play(Write(termdesc))
        self.wait()
        self.play(Create(arrows))
        self.wait()
        self.play(Write(coefftex))
        self.wait()
        self.play(FadeOut(term_grp))
        self.wait()

        # Coulomb term
        colframe = SurroundingRectangle(be[5], buff=.1)
        self.play(ReplacementTransform(surfframe, colframe))
        termname = Tex(r"\underline{\textit{Coulomb term}}").next_to(be, DOWN * 3.0).shift(LEFT * 3)
        termtex = Tex(r"$a_C\frac{Z(Z-1)}{A^{1/3}}$").next_to(termname, DOWN)
        termdesc = Tex(r"Decribes how protons repel\\each other").next_to(termtex, DOWN * 2)
        coefftex = Tex(r"$a_C\approx0.714\text{ MeV}$").next_to(termdesc, DOWN * 2)
        arrows = VGroup(
            Arrow(start=[4.92, -1.3, 0], end=[5.7, -0.65, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.17),
            Arrow(start=[4.92, -1.3, 0], end=[5.25, -0.15, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.15),
            Arrow(start=[4.92, -1.3, 0], end=[4.07, -0.22, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.13),
            Arrow(start=[4.92, -1.3, 0], end=[3.75, -0.8, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.13),
            Arrow(start=[4.92, -1.3, 0], end=[4.65, -2.0, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.2),
            Arrow(start=[4.92, -1.3, 0], end=[5.8, -1.8, 0], buff=0.0, stroke_width=4, max_tip_length_to_length_ratio=0.17)
        )
        term_grp = VGroup(
            termname,
            termtex,
            termdesc,
            arrows,
            coefftex
        )
        self.play(Write(termname))
        self.wait()
        self.play(Write(termtex))
        self.wait()
        self.play(Write(termdesc))
        self.wait()
        self.play(Create(arrows))
        self.wait()
        self.play(Write(coefftex))
        self.wait()
        self.play(FadeOut(term_grp), FadeOut(nuc))
        self.wait()

        # Asymmetry term
        asymframe = SurroundingRectangle(be[7], buff=.1)
        self.play(ReplacementTransform(colframe, asymframe))
        termname = Tex(r"\underline{\textit{Asymmetry term}}").next_to(be, DOWN * 3.0)
        termtex = Tex(r"$a_A\frac{(A-2Z)^2}{A}$").next_to(termname, DOWN)
        termdesc = Tex(r"Decribes how protons and neutrons\\fill quantum states more efficiently\\when they come in equal numbers").next_to(termtex, DOWN * 2)
        coefftex = Tex(r"$a_A\approx23.2\text{ MeV}$").next_to(termdesc, DOWN * 2)
        term_grp = VGroup(
            termname,
            termtex,
            termdesc,
            coefftex
        )
        self.play(Write(termname))
        self.wait()
        self.play(Write(termtex))
        self.wait()
        self.play(Write(termdesc))
        self.wait()
        self.play(Write(coefftex))
        self.wait()
        self.play(FadeOut(term_grp))
        self.wait()

        # Pairing term
        pairframe = SurroundingRectangle(be[9], buff=.1)
        self.play(ReplacementTransform(asymframe, pairframe))
        termname = Tex(r"\underline{\textit{Pairing term}}").next_to(be, DOWN * 3.0).shift(LEFT * 3.5)
        termtex = Tex(r"$\delta(A, Z)a_PA^{-1/2}$").next_to(termname, DOWN)
        termdesc = Tex(r"Decribes how pairs of like-\\nucleons are energetically\\favorable due to spin-coupling").next_to(termtex, DOWN * 2)
        coefftex = Tex(r"$a_P\approx11.2\text{ MeV}$").next_to(termdesc, DOWN * 2)
        term_grp = VGroup(
            termname,
            termtex,
            termdesc,
            coefftex
        )
        delta_font_size = 37
        deltatex = Tex(r"$\delta(A,Z)=$", font_size=delta_font_size).shift(DOWN * 1.0)
        deltaterms=VGroup(
            Tex("+1 if even $N_p$, even $N_n$", font_size=delta_font_size),
            Tex("-1 if odd $N_p$, odd $N_n$", font_size=delta_font_size),
            Tex("0 if otherwise", font_size=delta_font_size),
        ).arrange(DOWN, buff=MED_LARGE_BUFF, center=False, aligned_edge=LEFT).next_to(deltatex, RIGHT * 2.5)
        deltadesc = VGroup(
            deltatex,
            deltaterms
        ).to_edge(RIGHT).shift(RIGHT * 0.35)
        deltabrace = Brace(Line(deltaterms[0].get_corner(UL), deltaterms[-1].get_corner(DL)), LEFT).next_to(deltaterms, LEFT)
        self.play(Write(termname))
        self.wait()
        self.play(Write(termtex))
        self.wait()
        self.play(Write(termdesc))
        self.wait()
        self.play(Create(deltadesc), FadeIn(deltabrace))
        self.wait()
        self.play(Write(coefftex))
        self.wait()
        self.play(FadeOut(term_grp))
        self.wait()


class SEMFPlots(Scene):
    def construct(self):
        # Generate SEMF data
        data = create_BE_data()

        # Show that Iron is the most stable for 56 nucleons
        fe_question = Tex(r"\underline{For 56 nucleons, what number of protons will maximize binding energy?}", font_size=40).to_edge(UP)
        fe_data = data[56]
        fe_z = [d[0] for d in fe_data]
        fe_be = [56 * d[1] for d in fe_data]
        fe_data = [*zip(fe_z, fe_be)]
        fe_ax = Axes(
            x_range=[10, 40, 5],
            y_range=[150, 600, 50],
            tips=False,
            y_axis_config={"include_numbers": True, "font_size": 30},
            x_axis_config={"include_numbers": True,  "font_size": 30},
        ).scale(0.8)
        fe_ax_x_label = fe_ax.get_x_axis_label(Tex("Atomic number", font_size = 40), edge=DOWN, buff=0.1).next_to(fe_ax.coords_to_point(sum(fe_ax.x_range[0:2]) / 2, fe_ax.y_range[0]), DOWN * 2)
        fe_ax_y_label = fe_ax.get_y_axis_label(Tex("BE (MeV)", font_size=40)).next_to(fe_ax.coords_to_point(fe_ax.x_range[0], sum(fe_ax.y_range[0:2]) / 2), LEFT).rotate(np.pi / 2)
        fe_graph = fe_ax.plot_line_graph(
            x_values=fe_z,
            y_values=fe_be,
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=2,
        )
        fe_dot = Dot(fe_ax.coords_to_point(*max(fe_data, key=lambda x: x[1])))
        fe_line = DashedLine(start=fe_dot.get_center(), end=[fe_dot.get_x(), fe_ax.coords_to_point(0, fe_ax.y_range[0])[1], 0])
        fe_tex = Tex("$^{56}$Fe").next_to(fe_dot, UP)
        self.play(Write(fe_question))
        self.wait()
        self.play(Create(fe_ax), FadeIn(fe_ax_x_label), FadeIn(fe_ax_y_label))
        self.wait()
        self.play(DrawBorderThenFill(fe_graph))
        self.wait()
        self.play(GrowFromCenter(fe_dot), Create(fe_line), Write(fe_tex))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != fe_question])
        self.wait()

        # Show that Uranium is the most stable for 238
        u_question = Tex(r"\underline{For 238 nucleons, what number of protons will maximize binding energy?}", font_size=40).to_edge(UP)
        u_data = data[238]
        u_z = [d[0] for d in u_data]
        u_be = [238 * d[1] for d in u_data]
        u_data = [*zip(u_z, u_be)]
        u_ax = Axes(
            x_range=[60, 125, 10],
            y_range=[1350, 1850, 50],
            tips=False,
            y_axis_config={"include_numbers": True, "font_size": 30},
            x_axis_config={"include_numbers": True,  "font_size": 30},
        ).scale(0.8)
        u_ax_x_label = u_ax.get_x_axis_label(Tex("Atomic number", font_size = 40), edge=DOWN, buff=0.1).next_to(u_ax.coords_to_point(sum(u_ax.x_range[0:2]) / 2, u_ax.y_range[0]), DOWN * 2)
        u_ax_y_label = u_ax.get_y_axis_label(Tex("BE (MeV)", font_size=40)).next_to(u_ax.coords_to_point(u_ax.x_range[0], sum(u_ax.y_range[0:2]) / 2), LEFT).rotate(np.pi / 2)
        u_graph = u_ax.plot_line_graph(
            x_values=u_z,
            y_values=u_be,
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=2,
        )
        u_dot = Dot(u_ax.coords_to_point(*max(u_data, key=lambda x: x[1])))
        u_line = DashedLine(start=u_dot.get_center(), end=[u_dot.get_x(), u_ax.coords_to_point(0, u_ax.y_range[0])[1], 0])
        u_tex = Tex("$^{238}$U").next_to(u_dot, UP)
        self.play(Transform(fe_question, u_question))
        self.wait()
        self.play(Create(u_ax), FadeIn(u_ax_x_label), FadeIn(u_ax_y_label))
        self.wait()
        self.play(DrawBorderThenFill(u_graph))
        self.wait()
        self.play(GrowFromCenter(u_dot), Create(u_line), Write(u_tex))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != fe_question])
        self.wait()


class PlotAllIsotopes(ThreeDScene):
        def construct(self):
            # Plot all binding energy data
            ax = ThreeDAxes(
                x_range=[0, 250, 50],
                y_range=[0, 150, 25],
                z_range=[2, 10, 1],
                tips=False,
                y_axis_config={"include_numbers": True, "font_size": 30},
                x_axis_config={"include_numbers": True,  "font_size": 30},
            )
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(ax)
