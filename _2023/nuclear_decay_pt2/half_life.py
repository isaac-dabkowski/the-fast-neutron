from manim import *

from resources import Isotope, AlphaParticle, BetaPlusParticle, NeutrinoParticle, AlphaDecay, BetaPlusDecay

class HalfLifeTitleCard(Scene):
    def construct(self):
        section_title = Tex("Decay constants and half lives")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class DecayConstant(Scene):
    def construct(self):
        t1 = VGroup(
            Tex("Different unstable isotopes"),
            Tex("decay at different rates")
        ).arrange(DOWN, buff=MED_SMALL_BUFF).shift(UP)
        self.play(Write(t1))
        self.wait()

        # U235
        u235 = Isotope(element="U", mass_number=235, fill_color="#197d21")
        u235_s = u235.sprite.copy().shift(1.5 * DOWN + 2.5 * LEFT).scale(0.8)
        alpha = AlphaParticle()
        alpha_decay = AlphaDecay(parent=u235)
        th231_s = alpha_decay.daughter.sprite.copy().scale(0.77).set_y(u235_s.get_y()).set_x(u235_s.get_x())
        th231_s[0].set_fill_color("#424242")
        alpha_s = alpha.sprite.copy().set_y(u235_s.get_y()).set_x(u235_s.get_x())
        self.play(GrowFromCenter(u235_s))
        self.wait()
        self.play(
            GrowFromCenter(alpha_s),
            alpha_s.animate.shift(LEFT * 2.5),
            ReplacementTransform(u235_s, th231_s),
            run_time=0.75
        )

        # Cr47
        cr47 = Isotope(element="Cr", mass_number=47, fill_color="#a83271")
        cr47_s = cr47.sprite.copy().shift(1.5 * DOWN + 2.5 * RIGHT).scale(0.65)
        betap = BetaPlusParticle()
        neu = NeutrinoParticle()

        beta_plus_decay = BetaPlusDecay(parent=cr47)
        v47_s = beta_plus_decay.daughter.sprite.copy().scale(0.6).set_y(cr47_s.get_y()).set_x(cr47_s.get_x())
        v47_s[0].set_fill_color("#2f2445")

        betap_s = betap.sprite.copy().set_y(cr47_s.get_y()).set_x(cr47_s.get_x())
        neu_s = neu.sprite.copy().set_y(cr47_s.get_y()).set_x(cr47_s.get_x())
        self.play(GrowFromCenter(cr47_s))
        self.wait(0.6)
        self.play(
            GrowFromCenter(betap_s),
            betap_s.animate.shift(RIGHT * 2.5 + DOWN),
            GrowFromCenter(neu_s),
            neu_s.animate.shift(RIGHT * 2.5 + UP),
            ReplacementTransform(cr47_s, v47_s),
            run_time=0.75
        )
        self.wait()

        # Title
        title = Tex(r"\underline{Decay constant}").to_edge(UP).shift(DOWN * 0.5)
        self.play(
            Write(title),
            FadeOut(t1),
            FadeOut(th231_s),
            FadeOut(alpha_s),
            FadeOut(v47_s),
            FadeOut(betap_s),
            FadeOut(neu_s)
        )
        self.wait()

        # Describe decay constants
        t1 = Tex("Describes the rate at which an isotope decays").next_to(title, DOWN)
        self.play(Write(t1))
        self.wait()
        t2 = Tex("Represented with $\lambda$, units of $s^{-1}$").next_to(t1, DOWN).shift(DOWN * 0.25)
        self.play(Write(t2), Transform(title, Tex(r"\underline{Decay constant $\lambda$}").to_edge(UP).shift(DOWN * 0.5)))
        self.wait()
        t3 = Tex(r"Mean lifetime $\tau=\frac{1}{\lambda}$").next_to(t2, DOWN).shift(DOWN * 0.25)
        self.play(Write(t3))
        self.wait()
        t4 = Tex("Decay constants do not change with time").next_to(t3, DOWN).shift(DOWN * 0.25)
        self.play(Write(t4))
        self.wait()
        t5 = Tex("Collections of isotopes decay exponentially").next_to(t4, DOWN).shift(DOWN * 0.25)
        self.play(Write(t5))
        self.wait()
        t6 = Tex("$N(t)=N_0e^{-\lambda t}$").next_to(t5, DOWN).shift(DOWN * 0.25)
        self.play(Write(t6))
        self.wait()
        self.play(Transform(t6, Tex(r"$\frac{dN}{dt}=-\lambda N(t)$").next_to(t5, DOWN).shift(DOWN * 0.25)))
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class HalfLife(Scene):
    def construct(self):
        title = Tex(r"\underline{Half life}").to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(title))
        self.wait()

        t1 = VGroup(
            Tex("The amount of time expected for a quantity"),
            Tex("of an istope to lose half of its initial"),
            Tex("population to decay")
        ).arrange(DOWN, buff=MED_SMALL_BUFF).next_to(title, DOWN).shift(DOWN * 0.5)
        hlf = Tex(r"$t_{1/2}=\frac{\text{ln}\left(2\right)}{\lambda}$").next_to(t1, DOWN).shift(DOWN * 0.5)
        self.play(Write(t1))
        self.wait()
        self.play(Transform(title, Tex(r"\underline{Half life $t_{1/2}$}").to_edge(UP).shift(DOWN * 0.5)))
        self.wait()
        self.play(Write(hlf))
        self.wait()
        self.play(
            FadeOut(t1),
            hlf.animate.move_to([3.5, 1.5, 0])
        )
        self.wait()

        # Plot decay over time
        ax = Axes(
            x_range=[0, 3.5, 1],
            y_range=[0, 1.2],
            tips=False,
            y_axis_config={"include_numbers": False},
            x_axis_config={"include_numbers": False},
            x_length=4.0,
            y_length=3.0
        ).scale(1.2).to_edge(LEFT).shift(RIGHT + DOWN * 0.5)
        ax_x_label = ax.get_x_axis_label(Tex("Time", font_size = 50), edge=RIGHT, buff=0.1).shift(DOWN * 0.25)
        ax_y_label = ax.get_y_axis_label(Tex(r"$\frac{N(t)}{N_0}$"), edge=LEFT + UP, direction=UP, buff=0.2)
        values_x = [
            (1, "$1/\lambda$"),
            (2, "$2/\lambda$"),
            (3, "$3/\lambda$")
        ]
        axis_tick_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = Tex(x_tex, font_size=40)
            tex.next_to(ax.c2p(x_val, 0), DOWN)  # Put tex on the position
            axis_tick_labels.add(tex)
        axis_tick_labels.add(Tex("1.0", font_size=40).next_to(ax.c2p(0, 1), LEFT))
        curve = ax.plot(
            lambda x : np.exp(-x),
            x_range = [0, 3.5],
            color=YELLOW
        )
        self.play(
            FadeIn(ax),
            FadeIn(ax_x_label),
            FadeIn(ax_y_label),
            FadeIn(axis_tick_labels)
        )
        self.wait()
        self.play(
            ReplacementTransform(axis_tick_labels[0], Tex(r"$1\tau$", font_size=40).next_to(ax.c2p(1, 0), DOWN)),
            ReplacementTransform(axis_tick_labels[1], Tex(r"$2\tau$", font_size=40).next_to(ax.c2p(2, 0), DOWN)),
            ReplacementTransform(axis_tick_labels[2], Tex(r"$3\tau$", font_size=40).next_to(ax.c2p(3, 0), DOWN)),
            Transform(hlf, Tex(r"$t_{1/2}=\frac{\text{ln}\left(2\right)}{\lambda}=\text{ln}(2)\tau$").move_to([3.5, 1.5, 0]))
        )
        self.play(Create(curve), run_time=3)
        curve_grp = VGroup(
            ax,
            ax_x_label,
            ax_y_label,
            curve
        )
        self.wait()

        # Show dependence of pop on tau and half life
        t = ValueTracker(1)
        def get_l1():
            line = DashedLine(
                start=ax.c2p(t.get_value(), 0),
                end=ax.c2p(t.get_value(), np.exp(-t.get_value()))
            )
            return line
        def get_l2():
            line = DashedLine(
                start=ax.c2p(t.get_value(), np.exp(-t.get_value())),
                end=ax.c2p(0, np.exp(-t.get_value()))
            )
            return line
        l1 = always_redraw(get_l1)
        l2 = always_redraw(get_l2)
        label = Tex(r"$\frac{1}{e}$", font_size=40).next_to(ax.c2p(0, np.exp(-1)), LEFT)
        self.play(Create(l1))
        self.play(Create(l2))
        self.play(Write(label))
        self.wait()
        eq1 = Tex(r"$N(t_0 + k\tau)=\frac{N(t_0)}{e^k}$").next_to(hlf, DOWN)
        self.play(
            Write(eq1)
        )
        self.wait()
        self.play(
            t.animate.set_value(2),
            Transform(label, Tex(r"$\frac{1}{e^2}$", font_size=40).next_to(ax.c2p(0, np.exp(-2)), LEFT))
        )
        self.wait()
        self.play(
            t.animate.set_value(3),
            Transform(label, Tex(r"$\frac{1}{e^3}$", font_size=40).next_to(ax.c2p(0, np.exp(-3)), LEFT))
        )
        self.wait()
        self.play(
            t.animate.set_value(np.log(2)),
            Transform(label, Tex(r"$\frac{1}{2}$", font_size=40).next_to(ax.c2p(0, 0.5), LEFT))
        )
        l3 = Line(start=ax.c2p(np.log(2), 0), end=ax.c2p(np.log(2) - 0.25, -0.25))
        label2 = Tex(r"$t_{1/2}$", font_size=40).next_to(ax.c2p(t.get_value() - 0.25, -0.25), LEFT)
        self.play(
            Create(l3),
            Write(label2)
        )
        self.wait()
        eq2 = Tex(r"$N(t_0 + kt_{1/2})=\frac{N(t_0)}{2^k}$").next_to(eq1, DOWN)
        self.play(
            Write(eq2)
        )
        self.play(
            t.animate.set_value(2 * np.log(2)),
            Transform(label, Tex(r"$\frac{1}{4}$", font_size=40).next_to(ax.c2p(0, 0.25), LEFT)),
            Transform(l3, Line(start=ax.c2p(2 * np.log(2), 0), end=ax.c2p(2 * np.log(2), -0.25))),
            Transform(label2, Tex(r"$2t_{1/2}$", font_size=40).next_to(ax.c2p(2 * np.log(2), -0.125), DOWN))
        )
        self.wait()
        self.play(
            t.animate.set_value(3 * np.log(2)),
            Transform(label, Tex(r"$\frac{1}{8}$", font_size=40).next_to(ax.c2p(0, 0.125), LEFT)),
            Transform(l3, Line(start=ax.c2p(3 * np.log(2), 0), end=ax.c2p(3 * np.log(2) + 0.25, -0.25))),
            Transform(label2, Tex(r"$2t_{1/2}$", font_size=40).next_to(ax.c2p(3 * np.log(2) + 0.25, -0.25), RIGHT))
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()