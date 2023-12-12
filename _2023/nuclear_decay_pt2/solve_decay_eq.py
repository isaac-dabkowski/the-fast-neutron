from manim import *

class SolvingDecayEquationsTitleCard(Scene):
    def construct(self):
        section_title = Tex("Solving decay equations")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class SolvingDecayEquations(Scene):
    def construct(self):
        title = Tex(r"\underline{Solving decay equations}").to_edge(UP)
        self.play(Write(title))
        self.wait()

        t1 = Tex("We are going to need to solve some differential equations").next_to(title, DOWN).shift(DOWN * 0.125)
        self.play(Write(t1))
        self.wait()
        self.play(FadeOut(t1))
        self.wait()

        t1 = VGroup(
            Tex(r"$X_1$"),
            VGroup(
                Tex(r"$\lambda_1$"),
                Arrow()
            ).arrange(DOWN, buff=0.3),
            Tex(r"$X_2$")
        ).arrange(RIGHT).next_to(title, DOWN).shift(DOWN * 0.125)
        t1[1][1].set_y(t1[0].get_y())
        self.play(
            Write(t1[0]),
            Write(t1[1][0]),
            Create(t1[1][1]),
            Write(t1[2]),
        )
        self.wait()

        eq1 = VGroup(
            Tex(r"$\frac{dN_1}{dt} = -\lambda_1 N_1(t)$"),
            Tex(r"$\frac{dN_1}{dt} + \lambda_1 N_1(t) = 0$"),
            Tex(r"$I(t)=e^{\lambda_1 t}$"),
            Tex(r"$\int_0^t \frac{d}{dt'}\left[N_1(t')e^{\lambda_1 t'}\right]dt'=\int_0^t 0 dt'$"),
            Tex(r"$N_1(t)e^{\lambda_1 t}-N_1(0)e^0=0$"),
            Tex(r"$N_1(t)=N_1(0)e^{-\lambda_1 t}$")
        ).arrange(DOWN).next_to(t1, DOWN).shift(DOWN * 0.125)
        self.play(Write(eq1[0]))
        self.wait()
        self.play(Write(eq1[1]))
        self.wait()
        self.play(Write(eq1[2]))
        self.wait()
        self.play(Write(eq1[3]))
        self.wait()
        self.play(Write(eq1[4]))
        self.wait()
        self.play(Write(eq1[5]))
        self.wait()
        self.play(
            FadeOut(eq1[1]),
            FadeOut(eq1[2]),
            FadeOut(eq1[3]),
            FadeOut(eq1[4]),
            eq1[5].animate.next_to(eq1[0], DOWN)
        )
        self.wait()
        self.play(
            FadeOut(eq1[0]),
            FadeOut(eq1[5])
        )
        self.wait()

        eq2 = VGroup(
            Tex(r"$\frac{dN_2}{dt} = \lambda_1 N_1(t) -\lambda_2 N_2(t)$").scale(0.8),
            Tex(r"$\frac{dN_2}{dt} = \lambda_1 N_1(0)e^{-\lambda_1 t}$").scale(0.8),
            Tex(r"$\int_0^t\frac{dN_2}{dt'}dt' = \lambda_1 N_1(0) \int_0^t e^{-\lambda_1 t'}dt'$").scale(0.8),
            Tex(r"$N_2(t) - N_2(0) = \lambda_1 N_1(0) \left( \frac{e^{-\lambda_1 t}}{-\lambda_1} - \frac{e^{-\lambda_1 \cdot 0}}{-\lambda_1}\right)$").scale(0.8),
            Tex(r"$N_2(t) = N_2(0) + N_1(0) \left(1 - e^{-\lambda_1 t}\right)$").scale(0.8)
        ).arrange(DOWN).next_to(t1, DOWN).shift(DOWN * 0.125)
        self.play(Write(eq2[0]))
        self.wait()
        self.play(Transform(eq2[0], Tex(r"$\frac{dN_2}{dt} = \lambda_1 N_1(t)$").scale(0.8).move_to(eq2[0].get_center())))
        self.wait()
        self.play(Write(eq2[1]))
        self.wait()
        self.play(Write(eq2[2]))
        self.wait()
        self.play(Write(eq2[3]))
        self.wait()
        self.play(Write(eq2[4]))
        self.wait()
        self.play(
            FadeOut(eq2[1]),
            FadeOut(eq2[2]),
            FadeOut(eq2[3]),
            eq2[4].animate.next_to(eq2[0], DOWN)
        )
        self.wait()
        self.play(
            FadeOut(eq2[0])
        )
        self.wait()

        eq1 = Tex(r"$N_1(t)=N_1(0)e^{-\lambda_1 t}$").scale(0.8).to_corner(DR).shift(UP * 1.5 + LEFT * 2.585)
        self.play(
            Write(eq1),
            eq2[4].animate.to_corner(DR).shift(UP * 0.5),
            t1.animate.align_to(eq1, LEFT)
        )
        self.wait()

        # Plot decay over time
        lambda_1 = ValueTracker(0.4)
        n1 = ValueTracker(5)
        n2 = ValueTracker(0)
        ax = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            tips=False,
            y_axis_config={"include_numbers": True},
            x_axis_config={"include_numbers": True},
            x_length=4.0,
            y_length=4.0
        ).scale(1.2).to_edge(LEFT).shift(RIGHT * 0.25 + DOWN * 0.15)
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
        ).arrange(RIGHT, buff=MED_LARGE_BUFF).move_to([-3, 2, 0])
        def get_n1_curve():
            n1_curve = ax.plot(
                lambda t : n1.get_value() * np.exp(-lambda_1.get_value() * t),
                x_range = [0, 10],
                color=YELLOW
            )
            return n1_curve
        def get_n2_curve():
            n2_curve = ax.plot(
                lambda t : n2.get_value() + n1.get_value() * (1 - np.exp(-lambda_1.get_value() * t)),
                x_range = [0, 10],
                color=BLUE
            )
            return n2_curve
        n1_curve = always_redraw(get_n1_curve)
        n2_curve = always_redraw(get_n2_curve)
        self.play(
            FadeIn(ax),
            FadeIn(ax_x_label),
            FadeIn(ax_y_label),
            FadeIn(legend)
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
        ).arrange(RIGHT).next_to(t1, DOWN).align_to(t1, LEFT).shift(DOWN * 0.5)
        lambda_1_label[1].add_updater(
            lambda m: m.set_value(lambda_1.get_value())
        )
        n1_label = VGroup(
            Tex(r"$N_1(0)=$"),
            DecimalNumber(
                n1.get_value(),
                show_ellipsis=False,
                num_decimal_places=3,
                include_sign=False,
            )
        ).arrange(RIGHT).next_to(lambda_1_label, DOWN).align_to(t1, LEFT)
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
        ).arrange(RIGHT).next_to(n1_label, DOWN).align_to(t1, LEFT)
        n2_label[1].add_updater(
            lambda m: m.set_value(n2.get_value())
        )
        self.play(
            Write(lambda_1_label),
            Write(n1_label),
            Write(n2_label)
        )
        self.wait()
        self.play(
            Create(n1_curve),
            Create(n2_curve),
            run_time=3
        )
        self.wait()
        self.play(lambda_1.animate.set_value(2))
        self.wait()
        self.play(lambda_1.animate.set_value(0.5))
        self.wait()
        self.play(n1.animate.set_value(8))
        self.wait()
        self.play(n1.animate.set_value(5))
        self.wait()
        self.play(n2.animate.set_value(3))
        self.wait()
        self.play(n2.animate.set_value(0))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != title])
        self.wait()

class SolvingDecayEquationsWithProduction(Scene):
    def construct(self):
        title = Tex(r"\underline{Solving decay equations}").to_edge(UP)
        self.add(title)
        self.wait()

        t1 = VGroup(
            Tex("Production"),
            VGroup(
                Tex(r"$Q(t)$"),
                Arrow()
            ).arrange(DOWN, buff=0.4),
            Tex(r"$X_1$"),
            VGroup(
                Tex(r"$\lambda_1$"),
                Arrow()
            ).arrange(DOWN, buff=0.3),
            Tex("Decay")
        ).arrange(RIGHT).next_to(title, DOWN)
        t1[1][0].shift(LEFT * 0.1)
        t1[1][1].set_y(t1[0].get_y())
        t1[3][1].set_y(t1[0].get_y())
        self.play(
            Write(t1[0]),
            Write(t1[1][0]),
            Create(t1[1][1]),
            Write(t1[2]),
            Write(t1[3][0]),
            Create(t1[3][1]),
            Write(t1[4])
        )
        self.wait()

        eq1 = VGroup(
            Tex(r"$\frac{dN_1}{dt} = -\lambda_1 N_1(t) + Q(t)$"),
            Tex(r"$\frac{dN_1}{dt} + \lambda_1 N_1(t) = Q(t)$"),
            Tex(r"$I(t)=e^{\lambda_1 t}$"),
            Tex(r"$\frac{d}{dt}\left[N_1(t)e^{\lambda_1 t}\right]=Q(t)e^{\lambda_1 t}$"),
            Tex(r"$\int_0^t\frac{d}{dt'}\left[N_1(t')e^{\lambda_1 t'}\right]dt'=\int_0^tQ(t')e^{\lambda_1 t'}dt'$"),
            Tex(r"$N_1(t)e^{\lambda_1 t} - N_1(0)e^{0}=\int_0^tQ(t')e^{\lambda_1 t'}dt'$"),
            Tex(r"$N_1(t)=N_1(0)e^{-\lambda_1 t} + \int_0^tQ(t')e^{\lambda_1 (t'-t)}dt'$"),
        ).arrange(DOWN).next_to(title, DOWN)
        self.play(
            FadeOut(t1),
            Transform(title, Tex(r"\underline{Solving decay equations with production}").to_edge(UP)),
            Write(eq1[0])
        )
        self.wait()
        self.play(Write(eq1[1]))
        self.wait()
        self.play(Write(eq1[2]))
        self.wait()
        self.play(Write(eq1[3]))
        self.wait()
        self.play(Write(eq1[4]))
        self.wait()
        self.play(Write(eq1[5]))
        self.wait()
        self.play(Write(eq1[6]))
        self.wait()
        self.play(
            FadeOut(eq1[1]),
            FadeOut(eq1[2]),
            FadeOut(eq1[3]),
            FadeOut(eq1[4]),
            FadeOut(eq1[5]),
            eq1[6].animate.move_to(eq1[1].get_center())
        )
        self.wait()
        eq2 = VGroup(
            Tex("If $Q(t)$ is a constant Q:"),
            Tex(r"$N_1(t)=N_1(0)e^{-\lambda_1 t} + Qe^{-\lambda_1 t}\int_0^te^{\lambda_1 (t')}dt'$"),
            Tex(r"$N_1(t)=N_1(0)e^{-\lambda_1 t} + \frac{Q}{\lambda_1}e^{-\lambda_1 t}\left[e^{\lambda_1 t} - e^{0}\right]$"),
            Tex(r"$N_1(t)=N_1(0)e^{-\lambda_1 t} + \frac{Q}{\lambda_1}\left[1 - e^{-\lambda_1 t}\right]$")
        ).arrange(DOWN).next_to(eq1[1], DOWN)
        self.play(
            Write(eq2[0]),
            Transform(title, Tex(r"\underline{Solving decay equations with constant production}").to_edge(UP)),
        )
        self.wait()
        self.play(Write(eq2[1]))
        self.wait()
        self.play(Write(eq2[2]))
        self.wait()
        self.play(Write(eq2[3]))
        self.wait()
        self.play(
            FadeOut(eq2[1]),
            FadeOut(eq2[2]),
            eq2[3].animate.move_to(eq2[1].get_center())
        )
        self.wait()
        self.play(
            FadeOut(eq1[0]),
            FadeOut(eq1[6]),
            FadeOut(eq2[0]),
            eq2[3].animate.move_to(eq1[0].get_center())
        )
        self.wait()

        # Plot decay over time
        lambda_1 = ValueTracker(0.25)
        n1 = ValueTracker(10)
        q = ValueTracker(0)
        ax = Axes(
            x_range=[0, 20, 5],
            y_range=[0, 20, 5],
            tips=False,
            y_axis_config={"include_numbers": True},
            x_axis_config={"include_numbers": True},
            x_length=4.0,
            y_length=3.5
        ).scale(1.2).to_edge(LEFT).shift(RIGHT * 2 + DOWN * 0.5)
        ax_x_label = ax.get_x_axis_label(Tex("Time (s)", font_size = 50), edge=DOWN, direction=DOWN, buff=0.1).shift(DOWN * 0.2)
        ax_y_label = ax.get_y_axis_label(Tex("$N_1(t)$", font_size = 50), edge=LEFT, direction=LEFT, buff=0.3)
        def get_n1_curve():
            n1_curve = ax.plot(
                lambda t : n1.get_value() * np.exp(-lambda_1.get_value() * t) + q.get_value() / lambda_1.get_value() * (1 - np.exp(-lambda_1.get_value() * t)),
                x_range = [0, 20],
                color=YELLOW
            )
            return n1_curve
        n1_curve = always_redraw(get_n1_curve)
        self.play(
            FadeIn(ax),
            FadeIn(ax_x_label),
            FadeIn(ax_y_label)
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
        ).arrange(RIGHT).next_to(t1, DOWN).align_to(eq2, RIGHT).shift(DOWN * 0.5 + RIGHT * 0.5)
        lambda_1_label[1].add_updater(
            lambda m: m.set_value(lambda_1.get_value())
        )
        n1_label = VGroup(
            Tex(r"$N_1(0)=$"),
            DecimalNumber(
                n1.get_value(),
                show_ellipsis=False,
                num_decimal_places=3,
                include_sign=False,
            )
        ).arrange(RIGHT).next_to(lambda_1_label, DOWN).align_to(lambda_1_label, LEFT)
        n1_label[1].add_updater(
            lambda m: m.set_value(n1.get_value())
        )
        q_label = VGroup(
            Tex(r"$Q=$"),
            DecimalNumber(
                q.get_value(),
                show_ellipsis=False,
                num_decimal_places=3,
                include_sign=False,
            ),
            Tex(r"s$^{-1}$")
        ).arrange(RIGHT).next_to(n1_label, DOWN).align_to(lambda_1_label, LEFT)
        q_label[1].add_updater(
            lambda m: m.set_value(q.get_value())
        )
        self.play(
            Write(lambda_1_label),
            Write(n1_label),
            Write(q_label)
        )
        self.wait()
        self.play(
            Create(n1_curve),
            run_time=3
        )
        self.wait()
        self.play(lambda_1.animate.set_value(1))
        self.wait()
        self.play(lambda_1.animate.set_value(0.25))
        self.wait()
        self.play(n1.animate.set_value(15))
        self.wait()
        self.play(n1.animate.set_value(10))
        self.wait()
        self.play(q.animate.set_value(3.75))
        self.wait()
        def get_ql1_curve():
            ql1_curve = DashedLine(
                start=ax.c2p(0, q.get_value() / lambda_1.get_value()),
                end=ax.c2p(20, q.get_value() / lambda_1.get_value()),
                color=WHITE
            )
            return ql1_curve
        def get_ql1_tex():
            ql1_tex = Tex(r"$\frac{Q}{\lambda_1}$").next_to(ql1_curve, UP)
            return ql1_tex
        ql1_curve = always_redraw(get_ql1_curve)
        ql1_tex = always_redraw(get_ql1_tex)
        self.play(
            Create(ql1_curve),
            Write(ql1_tex)
        )
        self.wait()
        lim = Tex(r"$\displaystyle{\lim_{t \to \infty}}N_1(t)=\frac{Q}{\lambda_1}$").next_to(q_label, DOWN).align_to(lambda_1_label, LEFT).shift(DOWN * 0.3)
        act = Tex(r"$\displaystyle{\lim_{t \to \infty}}A_1(t)=Q$").next_to(lim, DOWN).align_to(lambda_1_label, LEFT)
        self.play(Write(lim))
        self.wait()
        self.play(Write(act))
        self.wait()
        self.play(n1.animate.set_value(20))
        self.wait()
        self.play(n1.animate.set_value(0))
        self.wait()
        self.play(q.animate.set_value(2))
        self.wait()
        self.play(
            q.animate.set_value(3),
            lambda_1.animate.set_value(0.2)
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != title])
        self.wait()
