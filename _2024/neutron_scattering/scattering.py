from manim import *

from resources import Proton, Electron

class ScatteringTitleCard(Scene):
    def construct(self):
        section_title = Tex("Neutron scattering")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class ScatteringFormulas(Scene):
    def construct(self):
        x = VGroup(
            Electron().sprite[0].set_x(-3),
            Tex("$x$").set_x(-3)
        )
        X = VGroup(
            Proton().sprite[0],
            Tex("$X$")
        )
        y = VGroup(
            Electron().sprite[0].set_x(3).set_y(2).set_fill_color(PINK).set_stroke_color("#38003b"),
            Tex("$y$").set_x(3).set_y(2)
        )
        Y = VGroup(
            Proton().sprite[0].set_x(3).set_y(-2).set_fill_color("#05ad08").set_stroke_color("#003b0c"),
            Tex("$Y$").set_x(3).set_y(-2)
        )
        a1 = Arrow(start=x[0].get_right(), end=X[0].get_left(), buff=0.2)
        a2 = always_redraw(lambda: Arrow(start=X[0].get_right(), end=y[0].get_corner(DL), buff=0.2))
        a3 = Arrow(start=X[0].get_right(), end=Y[0].get_corner(UL), buff=0.2)
        line = DashedLine(start=X[0].get_right(), end=[4, 0, 0], buff=0.2)
        angle = always_redraw(lambda: Angle(line, a2, radius=0.8))
        theta = always_redraw(lambda: Tex(r"$\theta$").next_to(angle, RIGHT))
        diagram = VGroup(
            x,
            X,
            Y,
            y,
            a1,
            a2,
            a3,
            angle,
            theta,
            line
        )
        diagram.scale(0.6).to_edge(LEFT).shift(RIGHT)
        ex = Tex(r"$\underline{\text{Neutron scattering kinematics}}$").to_edge(UP).shift(DOWN * 0.25)
        ey = Tex(r"$\sqrt{E_y}=a\pm\sqrt{a^2+b}$").next_to(ex, DOWN).shift(RIGHT * 3.5)
        aeq = Tex(r"$a=\sqrt{\frac{m_xm_XE}{\left(m_y+m_Y\right)^2}}\text{cos}\theta$").next_to(ey, DOWN)
        beq = Tex(r"$b=\frac{m_Y-m_x}{m_y+m_Y}E+\frac{m_Y}{m_y+m_Y}Q$").next_to(aeq, DOWN)
        self.play(
            Write(ex)
        )
        self.wait()
        self.play(
            Write(ey),
            Write(aeq),
            Write(beq),
            GrowFromCenter(x),
            GrowFromCenter(X),
            GrowFromCenter(Y),
            GrowFromCenter(y),
            Create(a1),
            Create(a2),
            Create(a3),
            Create(angle),
            Create(theta),
            Create(line)
        )
        self.wait()

        ntex1 = Tex("Neutron", font_size=40).next_to(x, UP * 2.5)
        ar1 = Arrow(start=ntex1.get_center(), end=x.get_center())
        self.play(
            Write(ntex1),
            Create(ar1),
            x.animate.set_stroke_color(GREEN),
            x.animate.set_fill("#416033", opacity=1.0)
        )
        self.wait()
        ntex2 = Tex("Nucleus", font_size=40).next_to(X, UP * 2.5)
        ar2 = Arrow(start=ntex2.get_center(), end=X.get_center())
        self.play(
            Write(ntex2),
            Create(ar2),
            X.animate.set_stroke_color("#ed9a51"),
            X.animate.set_fill("#b35707", opacity=1.0)
        )
        self.wait()
        ntex3 = Tex("Neutron", font_size=40).next_to(y, UP * 2.5)
        ar3 = Arrow(start=ntex3.get_center(), end=y.get_center())
        self.play(
            Write(ntex3),
            Create(ar3),
            y.animate.set_stroke_color(GREEN),
            y.animate.set_fill("#416033", opacity=1.0)
        )
        self.wait()
        ntex4 = Tex("Nucleus", font_size=40).next_to(Y, DOWN * 2.5)
        ar4 = Arrow(start=ntex4.get_center(), end=Y.get_center())
        self.play(
            Write(ntex4),
            Create(ar4),
            Y.animate.set_stroke_color("#ed9a51"),
            Y.animate.set_fill("#b35707", opacity=1.0)
        )
        self.wait()

        self.play(
            Transform(ey, Tex(r"$\sqrt{E'}=a\pm\sqrt{a^2+b}$").next_to(ex, DOWN).shift(RIGHT * 3.5)),
            Transform(aeq, Tex(r"$a=\sqrt{\frac{m_n^2E}{\left(M+m_n\right)^2}}\text{cos}\theta$").next_to(ey, DOWN)),
            Transform(beq, Tex(r"$b=\frac{M-m_n}{M+m_n}E+\frac{M}{M+m_n}Q$").next_to(aeq, DOWN))
        )
        self.wait()

        self.play(
            FadeOut(diagram),
            FadeOut(ntex1),
            FadeOut(ar1),
            FadeOut(ntex2),
            FadeOut(ar2),
            FadeOut(ntex3),
            FadeOut(ar3),
            FadeOut(ntex4),
            FadeOut(ar4),
            ey.animate.shift(LEFT * 3.5),
            aeq.animate.shift(LEFT * 3.5),
            beq.animate.shift(LEFT * 3.5)
        )
        self.wait()
        self.play(FadeOut(ey), FadeOut(aeq), FadeOut(beq))

        e_eqn1 = Tex(r"$\sqrt{E'}=\sqrt{\frac{m_n^2E}{\left(M+m_n\right)^2}}\text{cos}\theta \pm \sqrt{\frac{m_n^2E}{(M+m_n\right)^2}\text{cos}^2\theta+\frac{M-m_n}{M+m_n}E+\frac{M}{M+m_n}Q}$", font_size=30).next_to(ex, DOWN * 1.5)
        self.play(Write(e_eqn1))
        self.wait()

        e_eqn2 = Tex(r"$\sqrt{E'}=\frac{1}{M+m_n}\left[\sqrt{m_n^2E}\text{cos}\theta \pm \sqrt{(M^2 + m_n^2\text{cos}^2\theta-m_n^2)E+(M+m_n)MQ}\right]$", font_size=30).next_to(e_eqn1, DOWN * 1.5)
        self.play(Write(e_eqn2))
        self.wait()

        aeqn = Tex(r"$A=\frac{M}{m_n}\approx\text{Mass number}$").next_to(e_eqn2, DOWN * 1.5)
        self.play(Write(aeqn))
        self.wait()
        self.play(FadeOut(aeqn))
        self.wait()

        e_eqn3 = Tex(r"$\sqrt{E'}=\frac{1}{A+1}\left[\sqrt{E}\text{cos}\theta \pm \sqrt{(A^2 + \text{cos}^2\theta-1)E+(A^2+A)Q}\right]$", font_size=30).next_to(e_eqn2, DOWN * 1.5)
        self.play(Write(e_eqn3))
        self.wait()

        e_eqn4 = Tex(r"$E'=\frac{1}{(A+1)^2}\left[\sqrt{E}\text{cos}\theta \pm \sqrt{(A^2 + \text{cos}^2\theta-1)E+(A^2+A)Q}\right]^2$", font_size=30).next_to(e_eqn3, DOWN * 1.5)
        self.play(Write(e_eqn4))
        self.wait()

        self.play(
            FadeOut(e_eqn1),
            FadeOut(e_eqn2),
            FadeOut(e_eqn3),
            FadeOut(e_eqn4)
        )
        self.wait()

class AngleFormula(Scene):
    def construct(self):
        title = Tex(r"$\underline{\text{Neutron scattering kinematics}}$").to_edge(UP).shift(DOWN * 0.25)
        self.add(title)
        coseqn = Tex(r"$\text{cos}\theta=\frac{1}{2}\left[(A+1)\sqrt{\frac{E'}{E}}-(A-1)\sqrt{\frac{E}{E'}}-\frac{QA}{\sqrt{EE'}}\right]$")
        self.play(Write(coseqn))
        self.wait()
        self.play(coseqn.animate.next_to(title, DOWN * 1.5))
        self.wait()

        A = ValueTracker(1)
        ax = Axes(
            x_range=[0, 1.15, 0.01],
            y_range=[-1, 1],
            tips=False,
            y_axis_config={"include_numbers": True, "include_ticks": True},
            x_axis_config={"include_numbers": False, "include_ticks": False},
            x_length=6.0,
            y_length=3.5
        ).scale(1.2).next_to(coseqn, DOWN)
        ax_x_label = ax.get_x_axis_label(Tex("Energy", font_size = 50), edge=RIGHT, direction=RIGHT, buff=0.2)
        ax_y_label = ax.get_y_axis_label(Tex("$\\text{cos}\\theta$"), edge=LEFT, direction=LEFT, buff=0.1)


        def get_cos_curve():
            A_val = A.get_value()
            alpha = ((A_val - 1)/(A_val + 1))**2
            cos_curve = ax.plot(
                lambda E:  0.5*((A_val + 1)*(E)**0.5-(A_val-1)*(1/E)**0.5),
                x_range = [max([0.001, alpha + 0.001]), 1],
                color=YELLOW
            )
            return cos_curve
        cos_curve = always_redraw(get_cos_curve)

        self.play(
            FadeIn(ax),
            FadeIn(ax_x_label),
            FadeIn(ax_y_label)
        )
        self.wait()

        A_label = VGroup(
            Tex(r"$A=$"),
            DecimalNumber(
                A.get_value(),
                show_ellipsis=False,
                num_decimal_places=0,
                include_sign=False,
            )
        ).arrange(RIGHT).shift(UP * 0.25).align_to(ax_x_label, LEFT)
        update_a_label = lambda m: m.set_value(A.get_value())
        A_label[1].add_updater(update_a_label)
        self.play(
            Write(A_label)
        )
        self.wait()
        self.play(
            Create(cos_curve),
            run_time=3
        )
        self.wait()

        l1 = DashedLine(start=ax.c2p(0, 1), end=ax.c2p(1.15, 1))
        l2 = DashedLine(start=ax.c2p(0, -1), end=ax.c2p(1.15, -1))
        l3 = DashedLine(start=ax.c2p(1, 1), end=ax.c2p(1, -1))
        elabel = Tex(r"$E$").next_to(l3, RIGHT).shift(DOWN)

        self.play(Create(l1))
        self.play(Create(l2))
        self.play(Create(l3), Write(elabel))
        self.wait()

        self.play(A.animate.set_value(2))
        self.wait()

        def get_alpha_E_line():
            A_val = A.get_value()
            alpha = ((A_val - 1)/(A_val + 1))**2
            l4 = DashedLine(start=ax.c2p(alpha, 1), end=ax.c2p(alpha, -1.1))
            return l4
        l4 = always_redraw(get_alpha_E_line)
        alphae = Tex(r"$\alpha E$").next_to(l4, DOWN, buff=0.05)
        alphae.add_updater(lambda m: m.set_x(l4.get_x()))
        self.play(Create(l4), Write(alphae))
        self.wait()
        self.play(A.animate.set_value(3), rate_func=rate_functions.linear)
        self.play(A.animate.set_value(5), rate_func=rate_functions.linear)
        self.play(A.animate.set_value(10), rate_func=rate_functions.linear)
        self.wait()
        A_label[1].remove_updater(update_a_label)
        self.play(
            A.animate.set_value(1000),
            Transform(A_label[1], Tex(r"$\infty$").next_to(A_label[0])),
            rate_func=rate_functions.ease_in_quad
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class EnergyDistribution(Scene):
    def construct(self):
        title = Tex(r"$\underline{\text{Post-scatter neutron energy distribution}}$").to_edge(UP).shift(DOWN * 0.25)
        self.play(Write(title))
        self.wait()

        t1 = VGroup(
            Tex(r"What is the probability density function that"),
            Tex(r"describes post-scatter neutron energies?")
        ).arrange(DOWN).next_to(title, DOWN)
        self.play(Create(t1))
        self.wait()

        subpdf = VGroup(
            Tex(r"$\frac{1}{1-\alpha}\frac{1}{E}$"),
            Tex(r"$,$"),
            Tex(r"$\alpha E\leq E'\leq E$"),
            Tex(r"$0$"),
            Tex(r"$,$"),
            Tex("otherwise"),
        ).arrange_in_grid(rows=2, cols=3)
        pdf = VGroup(
            Tex(r"$p(E\rightarrow E')=$"),
            Brace(subpdf, direction=LEFT),
            subpdf
        ).arrange(RIGHT).next_to(title, DOWN)
        self.play(FadeOut(t1))
        self.play(
            Create(pdf)
        )
        self.wait()

        ax = Axes(
            x_range=[0, 2.5, 0.01],
            y_range=[0, 1],
            tips=True,
            y_axis_config={"include_numbers": False, "include_ticks": False},
            x_axis_config={"include_numbers": False, "include_ticks": False},
            x_length=6.0,
            y_length=3.25
        ).scale(1.2).next_to(pdf, DOWN)
        ax_x_label = ax.get_x_axis_label(Tex("Energy", font_size = 50), edge=RIGHT, direction=RIGHT, buff=0.2)
        ax_y_label = ax.get_y_axis_label(Tex(r"$p(E\rightarrow E')$"), edge=LEFT, direction=LEFT, buff=0.1)
        self.play(
            FadeIn(ax),
            Write(ax_x_label),
            Write(ax_y_label)
        )
        l1 = Line(start=ax.c2p(0.5, 0.6), end=ax.c2p(2, 0.6))
        l2 = DashedLine(start=ax.c2p(0.5, 0.6), end=ax.c2p(0.5, 0))
        l3 = DashedLine(start=ax.c2p(2, 0.6), end=ax.c2p(2, 0))
        self.play(
            Create(l1)
        )
        self.play(
            Create(l2),
            Create(l3)
        )
        label1 = Tex(r"$E$").next_to(l3, DOWN)
        label2 = Tex(r"$\alpha E$").next_to(l2, DOWN)
        self.play(
            Write(label1),
            Write(label2)
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != title])
        self.wait()

        t1 = Tex(r"What is the average change in energy?").next_to(title, DOWN)
        self.play(Write(t1))
        self.wait()

        avgE = MathTex(
            r"\left<-\Delta E\right> &= E - \left<\Delta E\right> \\",
            r"\left<-\Delta E\right>&= E - \int^E_{\alpha E}E'p(E\rightarrow E')dE' \\",
            r"\left<-\Delta E\right>&= E - \int^E_{\alpha E}\frac{1}{1-\alpha}\frac{E'}{E}dE' \\",
            r"\left<-\Delta E\right>&= E - \frac{1}{1-\alpha}\frac{1}{2E}\left[ E^2-\alpha^2E^2 \right] \\",
            r"\left<-\Delta E\right>&= \frac{1}{2}(1-\alpha) E",
            font_size=40
        ).next_to(t1, DOWN)
        self.play(Write(avgE[0]))
        self.play(Write(avgE[1]))
        self.play(Write(avgE[2]))
        self.play(Write(avgE[3]))
        self.play(Write(avgE[4]))
        self.play(
            FadeOut(avgE[0]),
            FadeOut(avgE[1]),
            FadeOut(avgE[2]),
            FadeOut(avgE[3]),
            avgE[4].animate.next_to(t1, DOWN)
        )
        avgEbox = SurroundingRectangle(avgE[4])
        self.play(Create(avgEbox))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class MinPostScatterE(Scene):
    def construct(self):
        coseqn = Tex(r"$\text{cos}\theta=\frac{1}{2}\left[(A+1)\sqrt{\frac{E'}{E}}-(A-1)\sqrt{\frac{E}{E'}}-\frac{QA}{\sqrt{EE'}}\right]$")
        self.play(Write(coseqn))
        self.play(Transform(coseqn, Tex(r"$\text{cos}\theta=\frac{1}{2}\left[(A+1)\sqrt{\frac{E'}{E}}-(A-1)\sqrt{\frac{E}{E'}}\right]$")))
        self.wait()
        self.play(Transform(coseqn, Tex(r"$-1=\frac{1}{2}\left[(A+1)\sqrt{\frac{E'}{E}}-(A-1)\sqrt{\frac{E}{E'}}\right]$")))
        self.wait()
        self.play(Transform(coseqn, Tex(r"$E'=\left(\frac{A-1}{A+1}\right)^2E$")))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
