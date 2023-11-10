from manim import *

class DecayChainsTitleCard(Scene):
    def construct(self):
        section_title = Tex("Decay chains")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class SolvingDecayChains(Scene):
    def construct(self):
        title = Tex(r"\underline{Decay chains}").to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Discussion
        t1 = Tex("Things can get much, much more complicated from here!").next_to(title, DOWN).shift(DOWN * 0.125)
        t2 = Tex("Real world decay chains can get long, and they").next_to(t1, DOWN).shift(DOWN * 0.125)
        t3 = Tex("can have several different branches.").next_to(t2, DOWN).shift(DOWN * 0.125)
        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait()
        self.play(Write(t3))
        self.wait()
        self.play(
            FadeOut(t1),
            FadeOut(t2),
            FadeOut(t3)
        )
        self.wait()

        # System of diff eq
        t1 = VGroup(
            Tex(r"$X_1$"),
            VGroup(
                Tex(r"$\lambda_1$"),
                Arrow()
            ).arrange(DOWN, buff=0.3),
            Tex(r"$X_2$"),
            VGroup(
                Tex(r"$\lambda_2$"),
                Arrow()
            ).arrange(DOWN, buff=0.3),
            Tex(r"$X_3$")
        ).arrange(RIGHT).next_to(title, DOWN)
        t1[1][1].set_y(t1[0].get_y())
        t1[3][1].set_y(t1[0].get_y())
        self.play(
            Write(t1[0]),
            Write(t1[1][0]),
            Create(t1[1][1]),
            Write(t1[2]),
            Write(t1[3][0]),
            Create(t1[3][1]),
            Write(t1[4]),
        )
        self.wait()

        # N_1(t)
        eq1 = VGroup(
            Tex(r"$\frac{dN_1}{dt} = -\lambda_1 N_1(t)$"),
            Tex(r"$\frac{dN_2}{dt} = \lambda_1 N_1(t)-\lambda_2 N_2(t)$"),
            Tex(r"$\frac{dN_3}{dt} = \lambda_2 N_2(t)$"),
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(t1, DOWN).shift(DOWN * 0.125)
        n1eq = Tex(r"$N_1(t)=N_1(0)e^{-\lambda_1 t}$").align_to(eq1[0], DOWN).shift(DOWN)
        self.play(Write(eq1[0]))
        self.wait()
        self.play(Write(eq1[1]))
        self.wait()
        self.play(Write(eq1[2]))
        self.wait()
        self.play(
            FadeOut(eq1[1]),
            FadeOut(eq1[2]),
            eq1[0].animate.set_x(0),
            Write(n1eq)
        )
        self.wait()
        eq1[1].set_y(eq1[0].get_y()).set_x(eq1[0].get_x())
        self.play(
            FadeOut(eq1[0]),
            FadeOut(n1eq),
            Write(eq1[1])
        )
        self.wait()

        # N_2(t)
        eq2 = VGroup(
            Tex(r"$\frac{dN_2}{dt} + \lambda_2 N_2(t)= \lambda_1 N_1(0)e^{-\lambda_1 t}$"),
            Tex(r"$\int_0^t\frac{d}{dt'}\left[N_2(t')e^{\lambda_2 t'}\right]dt'=\int_0^t \lambda_1 N_1(0)e^{(\lambda_2 -\lambda_1) t'}dt'$"),
            Tex(r"$N_2(t)e^{\lambda_2 t}-N_2(0)=\frac{\lambda_1 N_1(0)}{\lambda_2 -\lambda_1}\left(e^{(\lambda_2 -\lambda_1) t} - 1\right)$"),
            Tex(r"$N_2(t)=N_2(0)e^{-\lambda_2 t} + \frac{\lambda_1 N_1(0)}{\lambda_2 -\lambda_1}\left(e^{-\lambda_1 t} - e^{-\lambda_2 t}\right)$")
        ).arrange(DOWN).next_to(eq1[1], DOWN).shift(DOWN * 0.125)
        self.play(Write(eq2[0]))
        self.wait()
        self.play(Write(eq2[1]))
        self.wait()
        self.play(Write(eq2[2]))
        self.wait()
        self.play(Write(eq2[3]))
        self.wait()
        self.play(
            FadeOut(eq2[0]),
            FadeOut(eq2[1]),
            FadeOut(eq2[2]),
            eq2[3].animate.move_to(eq2[0].get_center())
        )
        self.wait()
        eq1[2].set_y(eq1[0].get_y()).set_x(eq1[0].get_x())
        self.play(
            FadeOut(eq1[1]),
            FadeOut(eq2[-1]),
            Write(eq1[2])
        )
        self.wait()

        # N_3(t)
        eq3 = VGroup(
            Tex(r"$\int_0^t\frac{dN_3}{dt'}dt'=\int_0^t \lambda_2 N_2(0)e^{-\lambda_2 t'} + \frac{\lambda_1 N_1(0)}{\lambda_2 -\lambda_1}\left(e^{-\lambda_1 t'} - e^{-\lambda_2 t'}\right)dt'$"),
            Tex(r"$N_3(t)-N_3(0)=-\frac{\lambda_2}{\lambda_2}N_2(0)\left[e^{-\lambda_2 t} - 1\right] + ...$")
        ).arrange(DOWN).next_to(eq1[1], DOWN).shift(DOWN * 0.125)
        n3eq = MathTex(r"N_3(t) = & N_3(0) + N_2(0)\left(1-e^{-\lambda_2 t}\right) \\ &+ \frac{N_1(0)}{\lambda_2 - \lambda_1}\left[\lambda_2(1-e^{-\lambda_1 t}) - \lambda_1(1-e^{-\lambda_2 t})\right]").shift(DOWN * 0.5)
        self.play(Write(eq3[0]))
        self.wait()
        self.play(Write(eq3[1]))
        self.wait()
        self.play(
            FadeOut(eq3[0]),
            FadeOut(eq3[1]),
            Write(n3eq)
        )
        self.wait()
        self.play(
            FadeOut(eq1[2]),
            FadeOut(n3eq)
        )
        self.wait()

        # Plot and mess with params
        lambda_1 = ValueTracker(0.4)
        lambda_2 = ValueTracker(0.5)
        n1 = ValueTracker(10)
        n2 = ValueTracker(0)
        n3 = ValueTracker(0)
        ax = Axes(
            x_range=[0, 20, 5],
            y_range=[0, 20, 5],
            tips=False,
            y_axis_config={"include_numbers": True},
            x_axis_config={"include_numbers": True},
            x_length=6.0,
            y_length=3.5
        ).scale(1.2).to_corner(DL).shift(RIGHT * 0.25 + UP * 0.25)
        ax_x_label = ax.get_x_axis_label(Tex("Time (s)", font_size = 50), edge=DOWN, direction=DOWN, buff=0.2)
        ax_y_label = ax.get_y_axis_label(Tex("$N$"), edge=LEFT, direction=LEFT, buff=0.1)
        legend = VGroup(
            VGroup(
                Tex(r"$N_1(t)=$", font_size=35),
                Line(color=YELLOW, start=[0, 0, 0], end=[0.75, 0, 0])
            ).arrange(RIGHT),
            VGroup(
                Tex(r"$N_2(t)=$", font_size=35),
                Line(color=BLUE, start=[0, 0, 0], end=[0.75, 0, 0])
            ).arrange(RIGHT),
            VGroup(
                Tex(r"$N_3(t)=$", font_size=35),
                Line(color=RED, start=[0, 0, 0], end=[0.75, 0, 0])
            ).arrange(RIGHT)
        ).arrange(DOWN, buff=MED_SMALL_BUFF).move_to([-3.5, 2.5, 0])
        def get_n1_curve():
            n1_curve = ax.plot(
                lambda t : n1.get_value() * np.exp(-lambda_1.get_value() * t),
                x_range = [0, 20],
                color=YELLOW
            )
            return n1_curve
        def get_n2_curve():
            n2_curve = ax.plot(
                lambda t : n2.get_value() * np.exp(-lambda_2.get_value() * t) + lambda_1.get_value() * n1.get_value() / (lambda_2.get_value() - lambda_1.get_value()) * (np.exp(-lambda_1.get_value() * t) - np.exp(-lambda_2.get_value() * t)),
                x_range = [0, 20],
                color=BLUE
            )
            return n2_curve
        def get_n3_curve():
            n3_curve = ax.plot(
                lambda t : n3.get_value() + n2.get_value() * (1 - np.exp(-lambda_2.get_value() * t)) + n1.get_value() / (lambda_2.get_value() - lambda_1.get_value()) * (lambda_2.get_value() * (1 - np.exp(-lambda_1.get_value() * t)) - lambda_1.get_value() * (1 - np.exp(-lambda_2.get_value() * t))),
                x_range = [0, 20],
                color=RED
            )
            return n3_curve
        n1_curve = always_redraw(get_n1_curve)
        n2_curve = always_redraw(get_n2_curve)
        n3_curve = always_redraw(get_n3_curve)
        self.play(
            FadeIn(ax),
            FadeIn(ax_x_label),
            FadeIn(ax_y_label),
            FadeIn(legend),
            t1.animate.to_edge(RIGHT)
        )
        self.wait()
        lambda_1_label = VGroup(
            Tex(r"$\lambda_1=$"),
            DecimalNumber(
                lambda_1.get_value(),
                show_ellipsis=False,
                num_decimal_places=3,
                include_sign=False,
            ),
            Tex(r"s$^{-1}$")
        ).arrange(RIGHT).shift(RIGHT * 4 + UP * 0.5)
        lambda_1_label[1].add_updater(
            lambda m: m.set_value(lambda_1.get_value())
        )
        lambda_2_label = VGroup(
            Tex(r"$\lambda_2=$"),
            DecimalNumber(
                lambda_2.get_value(),
                show_ellipsis=False,
                num_decimal_places=3,
                include_sign=False,
            ),
            Tex(r"s$^{-1}$")
        ).arrange(RIGHT).next_to(lambda_1_label, DOWN).align_to(lambda_1_label, LEFT).shift(DOWN * 0.25)
        lambda_2_label[1].add_updater(
            lambda m: m.set_value(lambda_2.get_value())
        )
        n1_label = VGroup(
            Tex(r"$N_1(0)=$"),
            DecimalNumber(
                n1.get_value(),
                show_ellipsis=False,
                num_decimal_places=3,
                include_sign=False,
            )
        ).arrange(RIGHT).next_to(lambda_2_label, DOWN).align_to(lambda_1_label, LEFT).shift(DOWN * 0.25)
        n1_label[1].add_updater(
            lambda m: m.set_value(n1.get_value())
        )
        n2_label = VGroup(
            Tex(r"$N_2(0)=$"),
            DecimalNumber(
                n2.get_value(),
                show_ellipsis=False,
                num_decimal_places=3,
                include_sign=False,
            )
        ).arrange(RIGHT).next_to(n1_label, DOWN).align_to(lambda_1_label, LEFT).shift(DOWN * 0.25)
        n2_label[1].add_updater(
            lambda m: m.set_value(n2.get_value())
        )
        n3_label = VGroup(
            Tex(r"$N_3(0)=$"),
            DecimalNumber(
                n3.get_value(),
                show_ellipsis=False,
                num_decimal_places=3,
                include_sign=False,
            )
        ).arrange(RIGHT).next_to(n2_label, DOWN).align_to(lambda_2_label, LEFT).shift(DOWN * 0.25)
        n3_label[1].add_updater(
            lambda m: m.set_value(n3.get_value())
        )
        self.play(
            Write(lambda_1_label),
            Write(lambda_2_label),
            Write(n1_label),
            Write(n2_label),
            Write(n3_label)
        )
        self.wait()
        self.play(
            Create(n1_curve),
            run_time=3
        )
        self.wait()
        self.play(
            Create(n2_curve),
            run_time=3
        )
        self.wait()
        self.play(
            Create(n3_curve),
            run_time=3
        )
        self.wait()
        self.play(n1.animate.set_value(20))
        self.wait()
        self.play(n1.animate.set_value(15))
        self.wait()
        self.play(n2.animate.set_value(5))
        self.wait()
        self.play(n2.animate.set_value(0))
        self.wait()
        self.play(n3.animate.set_value(5))
        self.wait()
        self.play(n3.animate.set_value(0))
        self.wait()
        self.play(lambda_1.animate.set_value(1))
        self.wait()
        self.play(lambda_1.animate.set_value(0.4))
        self.wait()
        self.play(lambda_2.animate.set_value(1))
        self.wait()
        self.play(lambda_2.animate.set_value(0.3))
        self.wait()
        self.play(
            lambda_1.animate.set_value(0.2),
            lambda_2.animate.set_value(5)
        )
        self.wait()
        self.play(
            FadeOut(ax),
            FadeOut(ax_x_label),
            FadeOut(ax_y_label),
            FadeOut(legend),
            FadeOut(n1_curve),
            FadeOut(n2_curve),
            FadeOut(n3_curve)
        )
        # Activity example for secular equilibrium
        ax = Axes(
            x_range=[0, 20, 5],
            y_range=[0, 5, 1 ],
            tips=False,
            y_axis_config={"include_numbers": True},
            x_axis_config={"include_numbers": True},
            x_length=5.0,
            y_length=3.5
        ).scale(1.2).to_corner(DL).shift(RIGHT * 1.25 + UP * 0.25)
        ax_x_label = ax.get_x_axis_label(Tex("Time (s)", font_size = 50), edge=DOWN, direction=DOWN, buff=0.2)
        ax_y_label = ax.get_y_axis_label(Tex("$A (Bq)$"), edge=LEFT, direction=LEFT, buff=0.1)
        legend = VGroup(
            VGroup(
                Tex(r"$A_1(t)=$", font_size=35),
                Line(color=YELLOW, start=[0, 0, 0], end=[0.75, 0, 0])
            ).arrange(RIGHT),
            VGroup(
                Tex(r"$A_2(t)=$", font_size=35),
                Line(color=BLUE, start=[0, 0, 0], end=[0.75, 0, 0])
            ).arrange(RIGHT)
        ).arrange(DOWN, buff=MED_SMALL_BUFF).move_to([-2.5, 2.25, 0])
        def get_a1_curve():
            a1_curve = ax.plot(
                lambda t : lambda_1.get_value() * n1.get_value() * np.exp(-lambda_1.get_value() * t),
                x_range = [0, 20],
                color=YELLOW
            )
            return a1_curve
        def get_a2_curve():
            a2_curve = ax.plot(
                lambda t : lambda_2.get_value() * (n2.get_value() * np.exp(-lambda_2.get_value() * t) + lambda_1.get_value() * n1.get_value() / (lambda_2.get_value() - lambda_1.get_value()) * (np.exp(-lambda_1.get_value() * t) - np.exp(-lambda_2.get_value() * t))),
                x_range = [0, 20],
                color=BLUE
            )
            return a2_curve
        a1_curve = always_redraw(get_a1_curve)
        a2_curve = always_redraw(get_a2_curve)
        self.play(
            FadeIn(ax),
            FadeIn(ax_x_label),
            FadeIn(ax_y_label),
            FadeIn(legend),
            t1.animate.to_edge(RIGHT)
        )
        self.wait()
        self.play(
            Create(a1_curve),
            Create(a2_curve),
            run_time=3
        )
        self.wait()
        self.play(lambda_2.animate.set_value(0.4))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class BatemanEquations(Scene):
    def construct(self):
        title = Tex(r"\underline{Bateman equations}").to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Discussion
        t1 = Tex("The equations we have been solving").next_to(title, DOWN).shift(DOWN * 0.125)
        t2 = Tex("are called ``Bateman equations''").next_to(t1, DOWN).shift(DOWN * 0.125)
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait()
        bateman = VGroup(
            Tex(r"$\frac{dN_1}{dt} = -\lambda_1 N_1(t)$"),
            Tex(r"$\frac{dN_2}{dt} = \lambda_1 N_1(t) -\lambda_2 N_2(t)$"),
            Tex(r"$...$"),
            Tex(r"$\frac{dN_i}{dt} = \lambda_{i-1} N_{i-1}(t) - \lambda_{i} N_{i}(t)$"),
            Tex(r"$...$"),
            Tex(r"$\frac{dN_N}{dt} = \lambda_{N-1} N_{N-1}(t)$"),
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(t2, DOWN).shift(DOWN * 0.125)
        bateman[2].shift(RIGHT)
        bateman[4].shift(RIGHT)
        self.play(Write(bateman))
        self.wait()
        self.play(
            FadeOut(t1),
            FadeOut(t2),
            bateman.animate.next_to(title, DOWN).shift(DOWN * 0.125)
        )
        self.play(
            FadeOut(bateman[1]),
            FadeOut(bateman[2]),
            FadeOut(bateman[4]),
            bateman[3].animate.shift(UP * 1.25),
            bateman[5].animate.shift(UP * 1.5)
        )
        self.wait()
        t3 = Tex(r"If $N_i(0)=0$ for all $i \neq 1$").shift(DOWN * 0.45)
        self.play(Write(t3))
        self.wait()
        batemansoln = Tex(r"$N_n(t)=N_1(0)\times{\displaystyle\left(\prod_{i=1}^{n-1}\lambda_i\right)}\times{\displaystyle \sum_{i=1}^n\frac{e^{-\lambda_i t}}{\displaystyle \prod_{j=1,j\neq i}^{n}(\lambda_j-\lambda_i)}}$").to_edge(DOWN)
        self.play(Write(batemansoln))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class MatrixExponential(Scene):
    def construct(self):
        title = Tex(r"\underline{The matrix exponential method}").to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Discussion
        t1 = Tex("This technique allows us to solve much").next_to(title, DOWN).shift(DOWN * 0.125)
        t2 = Tex("more complicated decay chains with the").next_to(t1, DOWN).shift(DOWN * 0.125)
        t3 = Tex("help of a computer.").next_to(t2, DOWN).shift(DOWN * 0.125)
        self.play(Write(t1), run_time=0.5)
        self.play(Write(t2), run_time=0.5)
        self.play(Write(t3), run_time=0.5)
        self.wait()
        self.play(
            FadeOut(t1),
            FadeOut(t2),
            FadeOut(t3)
        )
        self.wait()

        # Write out bateman equations
        eq1 = VGroup(
            Tex(r"$X_1$"),
            VGroup(
                Tex(r"$\lambda_1$"),
                Arrow()
            ).arrange(DOWN, buff=0.3),
            Tex(r"$X_2$"),
            VGroup(
                Tex(r"$\lambda_2$"),
                Arrow()
            ).arrange(DOWN, buff=0.3),
            Tex(r"$X_3$")
        ).arrange(RIGHT).next_to(title, DOWN)
        eq1[1][1].set_y(eq1[0].get_y())
        eq1[3][1].set_y(eq1[0].get_y())
        self.play(
            Write(eq1[0]),
            Write(eq1[1][0]),
            Create(eq1[1][1]),
            Write(eq1[2]),
            Write(eq1[3][0]),
            Create(eq1[3][1]),
            Write(eq1[4]),
        )
        self.wait()
        bateman = VGroup(
            Tex(r"$\frac{dN_1}{dt} = -\lambda_1 N_1(t)$"),
            Tex(r"$\frac{dN_2}{dt} = \lambda_1 N_1(t) -\lambda_2 N_2(t)$"),
            Tex(r"$\frac{dN_3}{dt} = \lambda_2 N_2(t)$"),
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(eq1, DOWN).shift(DOWN * 0.125)
        self.play(Write(bateman))
        self.wait()
        self.play(FadeOut(bateman))
        self.wait()
        dn1 = [r"$\frac{dN_1}{dt}$", r"$=$", r"$(-\lambda_1)N_1(t)$", r"$+$", r"$(0)N_2(t)$", r"$+$", r"$(0)N_3(t)$"]
        dn2 = [r"$\frac{dN_2}{dt}$", r"$=$", r"$(\lambda_1)N_1(t)$", r"$+$", r"$(-\lambda_2)N_2(t)$", r"$+$", r"$(0)N_3(t)$"]
        dn3 = [r"$\frac{dN_3}{dt}$", r"$=$", r"$(0)N_1(t)$", r"$+$", r"$(\lambda_2)N_2(t)$", r"$+$", r"$(0)N_3(t)$"]
        dn1_mob=Tex(*dn1)
        dn2_mob=Tex(*dn2)
        dn3_mob=Tex(*dn3)
        dn1_grp=VGroup(*dn1_mob).arrange(RIGHT, buff=0.8)
        dn1_grp[1].shift(LEFT * 0.5)
        dn1_grp[2].shift(LEFT)
        dn1_grp[3].shift(LEFT * 1.5)
        dn1_grp[4].shift(LEFT * 1.25)
        dn1_grp[5].shift(LEFT * 1.75)
        dn1_grp[6].shift(LEFT * 2)
        dn2_grp=VGroup(*dn2_mob)
        dn3_grp=VGroup(*dn3_mob)
        for i, item in enumerate(dn2_grp):
            item.align_to(dn1_grp[i], RIGHT)
        for i, item in enumerate(dn3_grp):
            item.align_to(dn1_grp[i], RIGHT)
        bateman = VGroup(dn1_grp, dn2_grp, dn3_grp).arrange(DOWN).next_to(eq1, DOWN)
        self.play(Write(bateman))
        self.wait()

        # Matrix form
        nmat1 = Matrix([["N_1(t)"], ["N_2(t)"], ["N_3(t)"]])
        lmat = Matrix([["-\lambda_1", 0, 0], ["\lambda_1", "-\lambda_2", 0], [0, "\lambda_2", 0]])
        nmat2 = Matrix([["N_1(t)"], ["N_2(t)"], ["N_3(t)"]])
        mateq = VGroup(
            Tex(r"$\frac{d}{dt}$", font_size=70),
            nmat1,
            Tex(r"$=$"),
            lmat,
            nmat2
        ).arrange(RIGHT).next_to(bateman, DOWN)
        self.play(Create(mateq))
        self.wait()
        r1 = SurroundingRectangle(bateman[0])
        r2 = SurroundingRectangle(mateq[3].get_rows()[0])
        self.play(
            FadeIn(r1),
            FadeIn(r2)
        )
        self.wait()
        self.play(
            Transform(r1, SurroundingRectangle(bateman[1])),
            Transform(r2, SurroundingRectangle(mateq[3].get_rows()[1]))
        )
        self.wait()
        self.play(
            Transform(r1, SurroundingRectangle(bateman[2])),
            Transform(r2, SurroundingRectangle(mateq[3].get_rows()[2]))
        )
        self.wait()
        self.play(
            Transform(r1, SurroundingRectangle(VGroup(*[b[2][0:-5] for b in bateman]))),
            Transform(r2, SurroundingRectangle(mateq[3].get_columns()[0]))
        )
        self.wait()
        self.play(
            Transform(r1, SurroundingRectangle(VGroup(*[b[4][0:-5] for b in bateman]))),
            Transform(r2, SurroundingRectangle(mateq[3].get_columns()[1]))
        )
        self.wait()
        self.play(
            Transform(r1, SurroundingRectangle(VGroup(*[b[6][0:-5] for b in bateman]))),
            Transform(r2, SurroundingRectangle(mateq[3].get_columns()[2]))
        )
        self.wait()
        self.play(
            FadeOut(bateman),
            FadeOut(r1),
            FadeOut(r2),
            mateq.animate.next_to(eq1, DOWN)
        )
        self.wait()
        eq2 = Tex(*[r"$\frac{dn}{dt}$", r"$=$", r"$\Lambda$", r"$n(t)$"])
        eq2_grp=VGroup(*eq2)
        eq2_grp[0].set_x(mateq[1].get_x()).set_y(-2)
        eq2_grp[1].set_x(mateq[2].get_x()).set_y(-2)
        eq2_grp[2].set_x(mateq[3].get_x()).set_y(-2)
        eq2_grp[3].set_x(mateq[4].get_x()).set_y(-2)
        b1 = Brace(VGroup(*mateq[0:2])).next_to(VGroup(*mateq[0:2]), DOWN)
        b1.put_at_tip(eq2_grp[0])
        b2 = Brace(mateq[3]).next_to(mateq[3], DOWN)
        b3 = Brace(mateq[4]).next_to(mateq[4], DOWN)
        self.play(
            FadeIn(b1),
            Write(eq2_grp[0])
        )
        self.wait()
        self.play(
            FadeIn(b2),
            Write(eq2_grp[2])
        )
        self.wait()
        self.play(
            FadeIn(b3),
            Write(eq2_grp[3])
        )
        self.wait()
        self.play(Write(eq2_grp[1]))
        self.wait()
        self.play(
            FadeOut(mateq),
            FadeOut(b1),
            FadeOut(b2),
            FadeOut(b3),
            eq2_grp.animate.arrange(RIGHT).next_to(eq1, DOWN)
        )
        self.wait()
        eq3 = Tex(r"$n(t)=e^{\Lambda t}n(0)$").next_to(eq2_grp, DOWN)
        self.play(Write(eq3))
        self.wait()
        expansion = MathTex(r"e^x &= 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + ... \\ e^{\Lambda t} &= \text{I} + \Lambda t + \frac{1}{2!}\Lambda^2t^2 + \frac{1}{3!}\Lambda^3 t^3 + ...").next_to(eq3, DOWN)
        self.play(Write(expansion))
        self.wait()
        self.play(
            FadeOut(eq1),
            eq2_grp.animate.shift(LEFT * 2.5),
            eq3.animate.shift(LEFT * 2.5),
            expansion.animate.shift(LEFT * 2.5)
        )
        self.wait()
        I = VGroup(
            Tex(r"$\text{I}=$"),
            Matrix([[1,0,0],[0,1,0],[0,0,1]])
        ).arrange(RIGHT).shift(RIGHT * 4)
        self.play(
            Write(I[0]),
            Create(I[1])
        )
        self.wait()
        self.play(
            FadeOut(title),
            FadeOut(eq2_grp),
            FadeOut(eq3),
            FadeOut(expansion),
            FadeOut(I)
        )
        self.wait()

        # Big decay chain
        isos = VGroup(
            Tex(r"$X_1$"),
            VGroup(
                Tex(r"$X_2$"),
                Tex(r"$X_3$")
            ).arrange(RIGHT, buff=3.25),
            VGroup(
                Tex(r"$X_4$"),
                Tex(r"$X_5$")
            ).arrange(RIGHT),
            VGroup(
                Tex(r"$X_6$"),
                Tex(r"$X_7$")
            ).arrange(RIGHT),
            Tex(r"$X_8$")
        ).arrange(DOWN, buff=1.25)
        isos[2][0].set_x(isos[1][0].get_x())
        isos[2][1].set_x(isos[0].get_x())
        isos[3][0].set_x(isos[2][1].get_x())
        isos[3][1].set_x(isos[1][1].get_x())
        isos[4].set_x(isos[1][1].get_x())
        arrows = VGroup(
            Line(start=isos[0].get_corner(DL), end=isos[1][0].get_corner(UR), buff=0.1).add_tip(tip_shape=ArrowTriangleFilledTip, tip_length=0.2, tip_width=0.2),
            Line(start=isos[0].get_corner(DR), end=isos[1][1].get_corner(UL), buff=0.1).add_tip(tip_shape=ArrowTriangleFilledTip, tip_length=0.2, tip_width=0.2),
            Line(start=isos[1][0].get_edge_center(DOWN), end=isos[2][0].get_edge_center(UP), buff=0.1).add_tip(tip_shape=ArrowTriangleFilledTip, tip_length=0.2, tip_width=0.2),
            Line(start=isos[1][0].get_corner(DR), end=isos[2][1].get_corner(UL), buff=0.1).add_tip(tip_shape=ArrowTriangleFilledTip, tip_length=0.2, tip_width=0.2),
            Line(start=isos[1][1].get_corner(DL), end=isos[2][1].get_corner(UR), buff=0.1).add_tip(tip_shape=ArrowTriangleFilledTip, tip_length=0.2, tip_width=0.2),
            Line(start=isos[2][1].get_edge_center(DOWN), end=isos[3][0].get_edge_center(UP), buff=0.1).add_tip(tip_shape=ArrowTriangleFilledTip, tip_length=0.2, tip_width=0.2),
            Line(start=isos[2][1].get_corner(DR), end=isos[3][1].get_corner(UL), buff=0.1).add_tip(tip_shape=ArrowTriangleFilledTip, tip_length=0.2, tip_width=0.2),
            Line(start=isos[3][0].get_edge_center(RIGHT), end=isos[3][1].get_edge_center(LEFT), buff=0.1).add_tip(tip_shape=ArrowTriangleFilledTip, tip_length=0.2, tip_width=0.2),
            Line(start=isos[3][1].get_edge_center(DOWN), end=isos[4].get_edge_center(UP), buff=0.1).add_tip(tip_shape=ArrowTriangleFilledTip, tip_length=0.2, tip_width=0.2)
        )
        self.play(
            Write(isos),
            Create(arrows)
        )
        self.wait()
        brs = VGroup(
            Tex(r"$f_{12}=0.85$", font_size=35).move_to(arrows[0].get_center()).shift(LEFT + UP * 0.2),
            Tex(r"$f_{13}=0.15$", font_size=35).move_to(arrows[1].get_center()).shift(RIGHT + UP * 0.2),
            Tex(r"$f_{24}=0.4$", font_size=35).move_to(arrows[2].get_center()).shift(LEFT * 0.9 + UP * 0.2),
            Tex(r"$f_{25}=0.6$", font_size=35).move_to(arrows[3].get_center()).shift(RIGHT * 0.7 + UP * 0.3),
            Tex(r"$f_{56}=0.25$", font_size=35).move_to(arrows[5].get_center()).shift(LEFT),
            Tex(r"$f_{57}=0.75$", font_size=35).move_to(arrows[6].get_center()).shift(RIGHT + UP * 0.1),
        )
        self.play(
            Write(brs)
        )

        # Highlight decays
        tracker = ValueTracker(0)
        def update_color(obj):
            T=tracker.get_value()
            rgbcolor=[255, 255, 255 - 255 * T]
            m_color=rgb_to_color(rgbcolor)
            obj.set_color(m_color)

        brs[0].add_updater(update_color)
        brs[1].add_updater(update_color)
        isos[0].add_updater(update_color)
        arrows[0].add_updater(update_color)
        arrows[1].add_updater(update_color)
        self.play(
            Write(brs[0]),
            Write(brs[1]),
            tracker.animate.set_value(1)
        )
        self.wait()
        self.play(
            tracker.animate.set_value(0)
        )
        self.wait()
        brs[0].remove_updater(update_color)
        brs[1].remove_updater(update_color)
        isos[0].remove_updater(update_color)
        arrows[0].remove_updater(update_color)
        arrows[1].remove_updater(update_color)

        brs[2].add_updater(update_color)
        brs[3].add_updater(update_color)
        isos[1][0].add_updater(update_color)
        arrows[2].add_updater(update_color)
        arrows[3].add_updater(update_color)
        self.play(
            Write(brs[2]),
            Write(brs[3]),
            tracker.animate.set_value(1)
        )
        self.wait()
        self.play(
            tracker.animate.set_value(0)
        )
        self.wait()
        brs[2].remove_updater(update_color)
        brs[3].remove_updater(update_color)
        isos[1][0].remove_updater(update_color)
        arrows[2].remove_updater(update_color)
        arrows[3].remove_updater(update_color)

        isos[1][1].add_updater(update_color)
        arrows[4].add_updater(update_color)
        self.play(
            tracker.animate.set_value(1)
        )
        self.wait()
        self.play(
            tracker.animate.set_value(0)
        )
        self.wait()
        isos[1][1].remove_updater(update_color)
        arrows[4].remove_updater(update_color)

        brs[4].add_updater(update_color)
        brs[5].add_updater(update_color)
        isos[2][1].add_updater(update_color)
        arrows[5].add_updater(update_color)
        arrows[6].add_updater(update_color)
        self.play(
            Write(brs[4]),
            Write(brs[5]),
            tracker.animate.set_value(1)
        )
        self.wait()
        self.play(
            tracker.animate.set_value(0)
        )
        self.wait()
        brs[4].remove_updater(update_color)
        brs[5].remove_updater(update_color)
        isos[2][1].remove_updater(update_color)
        arrows[5].remove_updater(update_color)
        arrows[6].remove_updater(update_color)

        isos[3][0].add_updater(update_color)
        arrows[7].add_updater(update_color)
        self.play(
            tracker.animate.set_value(1)
        )
        self.wait()
        self.play(
            tracker.animate.set_value(0)
        )
        self.wait()
        isos[3][0].remove_updater(update_color)
        arrows[7].remove_updater(update_color)

        isos[3][1].add_updater(update_color)
        arrows[8].add_updater(update_color)
        self.play(
            tracker.animate.set_value(1)
        )
        self.wait()
        self.play(
            tracker.animate.set_value(0)
        )
        self.wait()
        isos[3][1].remove_updater(update_color)
        arrows[8].remove_updater(update_color)

        decay_diagram = VGroup(
            isos,
            arrows,
            brs
        )
        self.play(decay_diagram.animate.to_edge(LEFT).shift(LEFT * 0.4))
        self.wait()

        lambdas = VGroup(
            Tex(r"$\lambda_1=4.0\times 10^-{6}\text{ s}^{-1}$"),
            Tex(r"$\lambda_2=1.5\times 10^-{7}\text{ s}^{-1}$"),
            Tex(r"$\lambda_3=1.0\times 10^-{2}\text{ s}^{-1}$"),
            Tex(r"$\lambda_4=0.0 \text{ s}^{-1}$"),
            Tex(r"$\lambda_5=3.0\times 10^-{5}\text{ s}^{-1}$"),
            Tex(r"$\lambda_6=2.0\times 10^-{8}\text{ s}^{-1}$"),
            Tex(r"$\lambda_7=3.0\times 10^-{3}\text{ s}^{-1}$"),
            Tex(r"$\lambda_8=0.0\text{ s}^{-1}$"),
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(decay_diagram, RIGHT).shift(RIGHT * 1.5)
        self.play(Write(lambdas))
        self.wait()
        self.play(FadeOut(lambdas))

        diffeqfontsize = 40
        diffeq = VGroup(
            Tex(r"$\frac{dN_1}{dt}=-\lambda_1N_1(t)$", font_size=diffeqfontsize),
            Tex(r"$\frac{dN_2}{dt}=f_{12}\lambda_1N_1(t)-\lambda_2N_2(t)$", font_size=diffeqfontsize),
            Tex(r"$\frac{dN_3}{dt}=f_{13}\lambda_1N_1(t)-\lambda_3N_3(t)$", font_size=diffeqfontsize),
            Tex(r"$\frac{dN_4}{dt}=f_{24}\lambda_2N_2(t)$", font_size=diffeqfontsize),
            Tex(r"$\frac{dN_5}{dt}=f_{25}\lambda_2N_2(t)+\lambda_3N_3(t)-\lambda_5N_5(t)$", font_size=diffeqfontsize),
            Tex(r"$\frac{dN_6}{dt}=f_{56}\lambda_5N_5(t)-\lambda_6N_6(t)$", font_size=diffeqfontsize),
            Tex(r"$\frac{dN_7}{dt}=f_{57}\lambda_5N_5(t)+\lambda_6N_6(t)-\lambda_7N_7(t)$", font_size=diffeqfontsize),
            Tex(r"$\frac{dN_8}{dt}=\lambda_7N_7(t)$", font_size=diffeqfontsize)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(decay_diagram, RIGHT).shift(RIGHT * 0.5)
        self.play(Write(diffeq))
        self.wait()
        self.play(
            FadeOut(diffeq),
            FadeOut(decay_diagram)
        )
        self.wait()

        nmat1 = Matrix([["N_1(t)"], ["N_2(t)"], ["N_3(t)"], ["N_4(t)"], ["N_5(t)"], ["N_6(t)"], ["N_7(t)"], ["N_8(t)"]])
        lmat = Matrix([
            [r"-\lambda_{1}", 0, 0, 0, 0, 0, 0, 0],
            [r"f_{12}\lambda_{1}", r"-\lambda_{2}", 0, 0, 0, 0, 0, 0],
            [r"f_{13}\lambda_{1}", 0, r"-\lambda_{3}", 0, 0, 0, 0, 0],
            [0, r"f_{24}\lambda_{2}", 0, 0, 0, 0, 0, 0],
            [0, r"f_{25}\lambda_{2}", r"\lambda_{3}", 0, r"-\lambda_{5}", 0, 0, 0],
            [0, 0, 0, 0, r"f_56\lambda_{5}", r"-\lambda_{6}", 0, 0],
            [0, 0, 0, 0, r"f_57\lambda_{5}", r"\lambda_{6}", r"-\lambda_{7}", 0],
            [0, 0, 0, 0, 0, 0, r"\lambda_{7}", 0]
        ])
        nmat2 = Matrix([["N_1(t)"], ["N_2(t)"], ["N_3(t)"], ["N_4(t)"], ["N_5(t)"], ["N_6(t)"], ["N_7(t)"], ["N_8(t)"]])
        mateq = VGroup(
            Tex(r"$\frac{d}{dt}$", font_size=70),
            nmat1,
            Tex(r"$=$"),
            lmat,
            nmat2
        ).arrange(RIGHT).scale(0.8)
        self.play(Create(mateq))
        self.wait()
        self.play(mateq.animate.shift(UP * 0.5))
        brace = Brace(mateq[3]).next_to(mateq[3], DOWN)
        ltex = Tex(r"$\Lambda$").next_to(brace, DOWN)
        self.play(
            FadeIn(brace),
            Write(ltex)
        )
        self.wait()
        # self.play(decay_diagram.animate.scale(0.7))