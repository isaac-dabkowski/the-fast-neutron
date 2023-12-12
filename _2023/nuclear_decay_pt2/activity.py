from manim import *

class ActivityTitleCard(Scene):
    def construct(self):
        section_title = Tex("Activity")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class Activity(Scene):
    def construct(self):
        title = Tex(r"\underline{Activity}").to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(title))
        self.wait()

        t1 = VGroup(
            Tex("Activity is the rate at which radioactive decay"),
            Tex("is occuring at a given point in time."),
            Tex("Activity = The rate of change in a nuclide's population")
        ).arrange(DOWN, buff=MED_SMALL_BUFF).next_to(title, DOWN).shift(DOWN * 0.25)
        self.play(Write(t1))
        self.wait()

        e1 = VGroup(
            Tex(r"$\frac{dN}{dt}=-\lambda N(t)$"),
            Tex(r"$\therefore$"),
            Tex(r"$A(t)=\lambda N(t)$")
        ).arrange(RIGHT).next_to(t1, DOWN)
        self.play(Write(e1))
        self.wait()

        t2 = Tex("For a single isotope decaying in isolation:").next_to(e1, DOWN).shift(DOWN * 0.5)
        self.play(Write(t2))
        self.wait()

        e2 = VGroup(
            Tex(r"$N(t)=N_0e^{-\lambda t}$"),
            Tex(r"$\therefore$"),
            Tex(r"$A(t)=\lambda N_0e^{-\lambda t}$")
        ).arrange(RIGHT).next_to(t2, DOWN)
        self.play(Write(e2))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class ActivityUnits(Scene):
    def construct(self):
        title = Tex(r"\underline{Activity units}").to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(title))
        self.wait()

        t1 = VGroup(
            Tex("Activity is a quantity which describes rates"),
            Tex("of decay, with dimensionality of inverse time."),
            Tex("We describe activity in terms of becquerels and curies.")
        ).arrange(DOWN, buff=MED_SMALL_BUFF).next_to(title, DOWN).shift(DOWN * 0.25)
        self.play(Write(t1[:-1]))
        self.wait()
        self.play(Write(t1[-1].shift(DOWN * 0.25)))
        self.wait()

        bq = Tex(r"$\text{1 Bq} = 1 \frac{\text{decay}}{\text{second}}$").next_to(t1, DOWN).shift(DOWN * 0.25)
        self.play(Write(bq))
        self.wait()
        ci = Tex(r"$\text{1 Ci} = 3.7\times 10^{10}\text{ Bq} = 3.7\times 10^{10}\frac{\text{decays}}{\text{second}}$").next_to(bq, DOWN).shift(DOWN * 0.25)
        self.play(Write(ci))
        self.wait()

        t2 = Tex(r"1 Ci $\approx$ Activity of 1 gram of radium").next_to(ci, DOWN).shift(DOWN * 0.25)
        self.play(Write(t2))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()