from manim import *

from resources import Isotope, BetaPlusParticle, NeutrinoParticle, BetaPlusDecay

class BRCard(Scene):
    def construct(self):
        section_title = Tex("Branching ratios")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class BR(Scene):
    def construct(self):
        title = Tex(r"\underline{Branching ratios}").to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(title))
        self.wait()

        t1 = VGroup(
            Tex("Some isotopes can undergo decay through multiple "),
            Tex("different modes, each of which has its own decay constant.")
        ).arrange(DOWN, buff=MED_SMALL_BUFF).next_to(title, DOWN).shift(DOWN * 0.25)
        self.play(Write(t1))
        self.wait()

        bptex = Tex(r"\underline{Beta plus decay}").move_to([-2.5, -0.35, 0])
        mg23 = Isotope(element="Mg", mass_number=23, fill_color="#753c1b")
        mg23_s = mg23.sprite.copy().scale(0.6).shift(DOWN * 2 + LEFT * 2)
        betap = BetaPlusParticle()
        neu = NeutrinoParticle()
        beta_plus_decay = BetaPlusDecay(parent=mg23)
        na23_s = beta_plus_decay.daughter.sprite.copy().scale(0.6).set_y(mg23_s.get_y()).set_x(mg23_s.get_x())
        na23_s[0].set_fill_color("#2f2445")
        betap_s = betap.sprite.copy().set_y(mg23_s.get_y()).set_x(mg23_s.get_x())
        neu_s = neu.sprite.copy().set_y(mg23_s.get_y()).set_x(mg23_s.get_x())
        self.play(Write(bptex))
        self.wait(0.6)
        self.play(GrowFromCenter(mg23_s))
        self.wait(0.6)
        self.play(
            GrowFromCenter(betap_s),
            betap_s.animate.shift(LEFT * 1.5 + DOWN * 0.75),
            GrowFromCenter(neu_s),
            neu_s.animate.shift(LEFT * 1.5 + UP * 0.75),
            ReplacementTransform(mg23_s, na23_s),
            run_time=0.75
        )
        ectex = Tex(r"\underline{Electron capture}").move_to([2.5, -0.35, 0])
        mg231 = Isotope(element="Mg", mass_number=23, fill_color="#753c1b")
        mg23_s1 = mg231.sprite.copy().scale(0.6).shift(DOWN * 2 + RIGHT * 2)
        neu1 = NeutrinoParticle()
        beta_plus_decay1 = BetaPlusDecay(parent=mg231)
        na23_s1 = beta_plus_decay1.daughter.sprite.copy().scale(0.6).set_y(mg23_s1.get_y()).set_x(mg23_s1.get_x())
        na23_s1[0].set_fill_color("#2f2445")
        neu_s1 = neu1.sprite.copy().set_y(mg23_s1.get_y()).set_x(mg23_s1.get_x())
        self.play(Write(ectex))
        self.wait(0.6)
        self.play(GrowFromCenter(mg23_s1))
        self.wait(0.6)
        self.play(
            GrowFromCenter(neu_s1),
            neu_s1.animate.shift(RIGHT * 1.5),
            ReplacementTransform(mg23_s1, na23_s1),
            run_time=0.75
        )
        self.wait()
        self.play(
            FadeOut(bptex),
            FadeOut(na23_s),
            FadeOut(betap_s),
            FadeOut(neu_s),
            FadeOut(ectex),
            FadeOut(na23_s1),
            FadeOut(neu_s1),
        )

        t2 = Tex(r"$\lambda = \lambda_1 + \lambda_2 + ... + \lambda_N$").next_to(t1, DOWN).shift(DOWN * 0.25)
        self.play(Write(t2))
        self.wait()

        t3 = Tex(r"$1 = \frac{\lambda_1}{\lambda} + \frac{\lambda_2}{\lambda} + ... + \frac{\lambda_N}{\lambda}$").next_to(t2, DOWN).shift(DOWN * 0.25)
        self.play(Write(t3))
        self.wait()

        t4 = Tex(r"$1 = f_1 + f_2 + ... + f_N$").next_to(t3, DOWN).shift(DOWN * 0.25)
        self.play(Write(t4))
        self.wait()

        t5 = Tex(r"$f_i$ = Fraction of times a decay will be of type $i$").next_to(t4, DOWN).shift(DOWN * 0.25)
        self.play(Write(t5))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
