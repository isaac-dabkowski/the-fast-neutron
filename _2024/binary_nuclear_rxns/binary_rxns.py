from manim import *

from resources import Proton, Electron

class BNRTitleCard(Scene):
    def construct(self):
        section_title = Tex("Binary nuclear reactions")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class BNR(Scene):
    def construct(self):
        # Random BNRs
        x = Electron().sprite[0].set_y(-1).set_x(-8)
        X = Proton().sprite[0].set_y(-1)
        y = Proton().sprite[0].set_y(-1).set_fill_color(PURPLE).set_stroke_color("#56025c").scale(0.7)
        Y = Electron().sprite[0].set_y(-1).set_fill_color(PINK).set_stroke_color("#3e0142").scale(0.7)
        self.play(GrowFromCenter(X), run_time=0.3)
        self.play(x.animate.set_x(0), run_time=2, rate_func=rate_functions.linear)
        self.remove(x, X)
        self.add(y, Y)
        self.play(y.animate.move_to([10, 2, 0]), Y.animate.move_to([10, -4, 0]), run_time=0.3, rate_func=rate_functions.linear)
        self.remove(y, Y)

        x = Electron().sprite[0].set_y(-8)
        X = Proton().sprite[0].set_y(1)
        z = Electron().sprite[0].set_y(1).set_fill_color(PINK).set_stroke_color("#f59042")
        y = Proton().sprite[0].set_y(1).set_fill_color(PURPLE).set_stroke_color("#f5dd42")
        Y = Electron().sprite[0].set_y(1).set_fill_color(PINK).set_stroke_color("#b042f5")
        self.play(GrowFromCenter(X), run_time=0.3)
        self.play(x.animate.set_y(1), run_time=0.5, rate_func=rate_functions.linear)
        self.remove(x, X)
        self.add(y, z, Y)
        self.play(y.animate.move_to([-5, 5, 0]), z.animate.move_to([0, 5, 0]), Y.animate.move_to([5, 5, 0]), run_time=0.7, rate_func=rate_functions.linear)
        self.remove(y, z, Y)

        x = Electron().sprite[0].set_x(8)
        X = Proton().sprite[0]
        y = Proton().sprite[0].set_fill_color(PURPLE).set_stroke_color("#f5426f")
        Y = Electron().sprite[0].set_fill_color(PINK).set_stroke_color("#42f554")
        self.play(GrowFromCenter(X), run_time=0.3)
        self.play(x.animate.set_x(0), run_time=0.5, rate_func=rate_functions.linear)
        self.remove(x, X)
        self.add(y, Y)
        self.play(y.animate.move_to([-8, 4, 0]), Y.animate.move_to([-8, -2, 0]), run_time=1.5, rate_func=rate_functions.linear)
        self.remove(y, Y)

        x = Electron().sprite[0].set_y(8)
        X = Proton().sprite[0].set_y(1)
        Y = Electron().sprite[0].set_y(1).set_fill_color(PINK).set_stroke_color("#3e0142")
        self.play(GrowFromCenter(X), run_time=0.3)
        self.play(x.animate.set_y(1), run_time=0.5, rate_func=rate_functions.linear)
        self.remove(x, X)
        self.add(Y)
        self.play(Y.animate.move_to([0, -5, 0]), run_time=0.7, rate_func=rate_functions.linear)
        self.remove(Y)

        title = Tex(r"\underline{Binary nuclear reactions}").to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(title))
        self.wait()
        tex1 = VGroup(
            Tex("Binary nuclear reactions are reactions"),
            Tex("between two nuclei which produce one or"),
            Tex("more reaction products.")
        ).arrange(DOWN, buff=MED_SMALL_BUFF).next_to(title, DOWN)
        self.play(Write(tex1))
        self.wait()

        x = Electron().sprite[0].set_y(-1).set_x(-8)
        X = Proton().sprite[0].set_y(-1)
        y = Proton().sprite[0].set_y(-1).set_fill_color(PURPLE).set_stroke_color("#56025c").scale(0.7)
        Y = Electron().sprite[0].set_y(-1).set_fill_color(PINK).set_stroke_color("#3e0142").scale(0.7)
        self.play(GrowFromCenter(X), run_time=0.3)
        self.play(x.animate.set_x(0), run_time=1.5, rate_func=rate_functions.linear)
        self.remove(x, X)
        self.add(y, Y)
        self.play(y.animate.move_to([10, 2, 0]), Y.animate.move_to([10, -4, 0]), run_time=0.5, rate_func=rate_functions.linear)
        self.remove(y, Y)

        tex2 = Tex("We will assume all participants are non-relativistic.").next_to(tex1, DOWN).shift(DOWN * 0.3)
        tex3 = Tex("All calculations here will be done with classical mechanics.").next_to(tex2, DOWN).shift(DOWN * 0.3)
        self.play(Write(tex2))
        self.wait()
        self.play(Write(tex3))
        self.wait()
        self.play(
            FadeOut(tex1),
            FadeOut(tex2),
            FadeOut(tex3)
        )

        x = Electron().sprite[0].set_y(-2).set_x(-8)
        X = Proton().sprite[0].set_y(-2)
        y = Proton().sprite[0].set_y(-2).set_fill_color(PURPLE).set_stroke_color("#56025c").scale(0.7)
        Y = Electron().sprite[0].set_y(-2).set_fill_color(PINK).set_stroke_color("#3e0142").scale(1.2)
        self.play(GrowFromCenter(X), run_time=0.3)
        self.play(x.animate.set_x(0), run_time=1.25, rate_func=rate_functions.linear)
        self.remove(x, X)
        self.add(y, Y)
        self.play(y.animate.move_to([10, 1, 0]), Y.animate.move_to([10, -5, 0]), run_time=0.3, rate_func=rate_functions.linear)
        self.remove(y, Y)
        self.wait()
        x.set_x(-4)
        X.set_x(-2)
        Y.set_x(2)
        y.set_x(4)
        Y.set_y(-2)
        y.set_y(-2)
        ar1 = Arrow(start=[-1.5, -2, 0], end=[1.5, -2, 0])
        p1 = Tex("+").move_to([-3, -2, 0])
        p2 = Tex("+").move_to([3, -2, 0])
        eq = Tex(r"$x + X \rightarrow Y + y$").set_y(1)
        self.play(
            GrowFromCenter(x),
            GrowFromCenter(X),
            GrowFromCenter(Y),
            GrowFromCenter(y),
            Create(ar1),
            Write(p1),
            Write(p2),
            Write(eq)
        )
        self.wait()
        b1 = Brace(eq[0][0], direction=UP)
        b2 = Brace(eq[0][2], direction=DOWN)
        b3 = Brace(eq[0][4], direction=UP)
        b4 = Brace(eq[0][6], direction=DOWN)
        t1 = Tex("Projectile", font_size=35).next_to(b1, UP)
        t2 = Tex("Target", font_size=35).next_to(b2, DOWN)
        t3 = Tex("Heavy product", font_size=35).next_to(b3, UP)
        t4 = Tex("Light product", font_size=35).next_to(b4, DOWN)
        self.play(
            Create(b1),
            Create(b2),
            Create(b3),
            Create(b4),
            Write(t1),
            Write(t2),
            Write(t3),
            Write(t4)
        )
        self.wait()
        self.play(
            FadeOut(b1),
            FadeOut(b2),
            FadeOut(b3),
            FadeOut(b4),
            FadeOut(t1),
            FadeOut(t2),
            FadeOut(t3),
            FadeOut(t4)
        )
        self.wait()
        CN = Electron().sprite[0].set_y(-2).set_fill_color("#46026e").set_stroke_color("#79767a").scale(1.6)
        ar2 = Arrow(start=[1, -2, 0], end=[3, -2, 0])
        eq2 = Tex(r"$X(x,y)Y$").set_y(-0.5)
        self.play(
            x.animate.shift(LEFT*1.5),
            p1.animate.shift(LEFT*1.5),
            X.animate.shift(LEFT*1.5),
            ar1.animate.shift(LEFT*1.5),
            y.animate.shift(RIGHT*1.5),
            p2.animate.shift(RIGHT*1.5),
            Y.animate.shift(RIGHT*1.5),
            ReplacementTransform(ar1, Arrow(start=[-3, -2, 0], end=[-1, -2, 0])),
            Create(ar2),
            GrowFromCenter(CN),
            ReplacementTransform(eq, Tex(r"$x + X \rightarrow (x+X)^{*} \rightarrow Y + y$").set_y(1)),
            Write(eq2)
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class ConservationEqns(Scene):
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
            Proton().sprite[0].set_x(3).set_y(2).set_fill_color(PINK).set_stroke_color("#38003b").scale(0.7),
            Tex("$y$").set_x(3).set_y(2)
        )
        Y = VGroup(
            Electron().sprite[0].set_x(3).set_y(-2).set_fill_color("#05ad08").set_stroke_color("#003b0c").scale(1.2),
            Tex("$Y$").set_x(3).set_y(-2)
        )
        a1 = Arrow(start=x[0].get_right(), end=X[0].get_left(), buff=0.25)
        a2 = always_redraw(lambda: Arrow(start=X[0].get_right(), end=y[0].get_corner(DL), buff=0.25))
        a3 = Arrow(start=X[0].get_right(), end=Y[0].get_corner(UL), buff=0.25)
        line = DashedLine(start=X[0].get_right(), end=[4, 0, 0], buff=0.25)
        angle = always_redraw(lambda: Angle(line, a2, radius=1))
        theta = always_redraw(lambda: Tex(r"$\theta$").next_to(angle, RIGHT))
        self.play(
            GrowFromCenter(x),
            GrowFromCenter(X),
            GrowFromCenter(Y),
            GrowFromCenter(y),
            Create(a1),
            Create(a2),
            Create(a3)
        )
        self.wait()
        self.play(
            Create(line),
            Create(angle),
            Write(theta)
        )
        self.play(y.animate.shift(LEFT + UP * 0.5))
        self.play(y.animate.shift(RIGHT * 1.5 + DOWN * 0.5))
        self.wait()
        masses = VGroup(
            Tex("$m_x$").next_to(x[0].get_top(), UP),
            Tex("$m_X$").next_to(X[0].get_top(), UP),
            Tex("$m_Y$").next_to(Y[0].get_top(), UP),
            Tex("$m_y$").next_to(y[0].get_top(), UP),
        )
        self.play(
            Write(masses)
        )
        self.wait()
        diagram = VGroup(
            x,
            X,
            y,
            Y,
            a1,
            a2,
            a3,
            line,
            theta,
            masses
        )
        self.play(
            diagram.animate.scale(0.5).to_corner(UL)
        )
        self.wait()
        tex1 = Tex(r"$\underline{\text{Conservation of Energy}}$").to_edge(UP).shift(RIGHT * 1.5)
        self.play(Write(tex1))
        self.wait()
        ce = Tex("$E_x = E_y + E_Y + Q$").next_to(tex1, DOWN).shift(DOWN * 0.5)
        self.play(Write(ce))
        self.wait()

        tex2 = Tex(r"$\underline{\text{Conservation of Momentum}}$").shift(DOWN * 0.5).set_x(tex1.get_x())
        cm = Tex(r"$p_Y^2=p_y^2+p_x^2-2p_xp_y\text{cos}\theta$").next_to(tex2, DOWN).shift(DOWN * 0.5)
        self.play(Write(tex2))
        self.wait()
        a4 = Arrow(start=[-2, 0, 0], end=[2, 0, 0], buff=0)
        a5 = Arrow(start=[-2, 0, 0], end=[1.5, 1.5, 0], buff=0)
        a6 = Arrow(start=[1.5, 1.5, 0], end=[2, 0, 0], buff=0)
        t1 = Tex("$p_x$").align_to(a4, DOWN).shift(DOWN * 0.25)
        t2 = Tex("$p_y$").next_to(a5, LEFT).shift(RIGHT * 1.5 + UP * 0.25)
        t3 = Tex("$p_Y$").next_to(a6, RIGHT).shift(LEFT * 0.25 + UP * 0.25)
        diagram2 = VGroup(
            a4,
            a5,
            a6,
            t1,
            t2,
            t3
        ).to_edge(LEFT).shift(DOWN * 3).scale(0.8)
        angle2 = Angle(a4, a5, radius=1.25)
        theta2 = Tex(r"$\theta$").next_to(angle2, RIGHT)
        diagram2.add(angle2)
        diagram2.add(theta2)
        self.play(
            Create(a4),
            Create(a5),
            Create(a6),
            Write(t1),
            Write(t2),
            Write(t3),
            Create(angle2),
            Write(theta2)
        )
        self.wait()
        self.play(
            Write(cm)
        )
        self.wait()
        self.play(
            FadeOut(tex1),
            FadeOut(ce),
            FadeOut(tex2),
            FadeOut(cm),
            FadeOut(diagram2)
        )
        self.wait()
        ey = Tex(r"$\sqrt{E_y}=a\pm\sqrt{a^2+b}$").shift(DOWN * 0.75)
        self.play(
            Write(ey),
            diagram.animate.shift(RIGHT * 5)
        )
        self.wait()
        aeq = Tex(r"$a=\sqrt{\frac{m_xm_XE_x}{\left(m_y+m_Y\right)^2}}\text{cos}\theta$").shift(LEFT * 3 + DOWN * 2.5)
        beq = Tex(r"$b=\frac{m_Y-m_x}{m_y+m_Y}E_x+\frac{m_Y}{m_y+m_Y}Q$").shift(RIGHT * 3 + DOWN * 2.5)
        self.play(
            Write(aeq),
            Write(beq)
        )
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class ExothermicRxns(Scene):
    def construct(self):
        ex = Tex(r"$\underline{\text{Exothermic reactions (Q} > \text{0)}}$").to_edge(UP).shift(DOWN * 0.25)
        ey = Tex(r"$\sqrt{E_y}=a\pm\sqrt{a^2+b}$").next_to(ex, DOWN)
        aeq = Tex(r"$a=\sqrt{\frac{m_xm_XE_x}{\left(m_y+m_Y\right)^2}}\text{cos}\theta$").next_to(ey, DOWN)
        beq = Tex(r"$b=\frac{m_Y-m_x}{m_y+m_Y}E_x+\frac{m_Y}{m_y+m_Y}Q$").next_to(aeq, DOWN)
        self.play(
            Write(ex)
        )
        self.wait()
        self.play(
            Write(ey),
            Write(aeq),
            Write(beq)
        )
        self.play(
            ey.animate.shift(RIGHT * 3.5),
            aeq.animate.shift(RIGHT * 3.5),
            beq.animate.shift(RIGHT * 3.5)
        )
        self.play(
            FadeIn(ImageMobject("assets/BNR_diagram.png").scale(1.5).to_corner(UL).shift(DOWN * 1 + RIGHT * 1.5))
        )
        self.wait()
        line = Line(start=[-10, beq.get_y() - 0.5, 0], end=[10, beq.get_y() - 0.5, 0])
        t1 = MathTex(r"\text{If Q} > 0\text{...}").next_to(ex, DOWN).shift(DOWN * 3)
        self.play(
            Create(line)
        )
        self.wait()
        self.play(Write(t1))
        self.wait()
        logic = VGroup(
            VGroup(
                Tex(r"$a > 0$"),
                Tex(r"$b > 0 \text{ since } m_Y > m_x$"),
                Tex(r"$a-\sqrt{a^2+b} < 0$")
            ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT),
            VGroup(
                MathTex(r"\text{There is only one possible}\\\text{energy for the light product!}"),
                Tex(r"$\text{If } E_x \approx 0 \rightarrow E_y = \frac{m_Y}{m_y+m_Y}Q$")
            ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT)
        ).next_to(t1, DOWN)
        self.play(
            Write(logic[0][0])
        )
        self.wait()
        self.play(
            Write(logic[0][1])
        )
        self.wait()
        self.play(
            Write(logic[0][2])
        )
        self.wait()
        self.play(
            Write(logic[1][0])
        )
        self.wait()
        self.play(
            Write(logic[1][1])
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class EndothermicRxns(Scene):
    def construct(self):
        ex = Tex(r"$\underline{\text{Endothermic reactions (Q} < \text{0)}}$").to_edge(UP).shift(DOWN * 0.25)
        ey = Tex(r"$\sqrt{E_y}=a\pm\sqrt{a^2+b}$").next_to(ex, DOWN)
        aeq = Tex(r"$a=\sqrt{\frac{m_xm_XE_x}{\left(m_y+m_Y\right)^2}}\text{cos}\theta$").next_to(ey, DOWN)
        beq = Tex(r"$b=\frac{m_Y-m_x}{m_y+m_Y}E_x+\frac{m_Y}{m_y+m_Y}Q$").next_to(aeq, DOWN)
        self.play(
            Write(ex),
            Write(ey),
            Write(aeq),
            Write(beq)
        )
        self.play(
            ey.animate.shift(RIGHT * 3.5),
            aeq.animate.shift(RIGHT * 3.5),
            beq.animate.shift(RIGHT * 3.5)
        )
        img = ImageMobject("assets/BNR_diagram.png").scale(1.5).to_corner(UL).shift(DOWN * 1 + RIGHT * 1.5)
        self.play(
            FadeIn(img)
        )
        self.wait()
        line = Line(start=[-10, beq.get_y() - 0.5, 0], end=[10, beq.get_y() - 0.5, 0])
        t1 = MathTex(r"\text{If Q} < 0\text{...}").next_to(ex, DOWN).shift(DOWN * 3)
        self.play(
            Create(line)
        )
        self.wait()
        self.play(Write(t1))
        self.wait()
        logic = VGroup(
            VGroup(
                Tex(r"$a > 0$"),
                Tex(r"$b > 0 \text{ OR } b < 0$")
            ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT),
            VGroup(
                MathTex(r"\text{It is possible for }a^2+b\text{ to be negative!}"),
                Tex(r"$\text{There is a threshold that } E_x \text{ has to meet}$")
            ).arrange(DOWN, aligned_edge=RIGHT).to_edge(RIGHT)
        ).next_to(t1, DOWN)
        self.play(
            Write(logic[0][0])
        )
        self.wait()
        self.play(
            Write(logic[0][1])
        )
        self.wait()
        self.play(
            Write(logic[1][0])
        )
        self.wait()
        self.play(
            Write(logic[1][1])
        )
        self.wait()
        self.play(
            FadeOut(line),
            FadeOut(img),
            FadeOut(t1),
            FadeOut(logic[1])
        )
        self.play(
            logic[0].animate.next_to(ex, DOWN).to_edge(LEFT).shift(RIGHT + DOWN * 0.5)
        )
        line = Line(start=[-10, beq.get_y() - 0.5, 0], end=[10, beq.get_y() - 0.5, 0])
        self.wait()
        e3 = Tex(r"$a+\sqrt{a^2+b} > 0$").next_to(logic[0][1], DOWN).shift(DOWN * 1.5)
        self.play(
            Create(line),
            Write(e3)
        )
        self.wait()
        e4 = Tex(r"$a-\sqrt{a^2+b} > 0$ if $E_x$ is large enough").next_to(e3, DOWN).align_to(e3, LEFT)
        self.play(
            Write(e4)
        )
        self.wait()
        t5 = Tex(r"There can be 2 possible energies if $Q<0$ and $E_x$ is large!").to_edge(DOWN)
        self.play(Write(t5))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class KinematicThreshold(Scene):
    def construct(self):
        title = Tex(r"$\underline{\text{Kinematic threshold}}$").to_edge(UP).shift(DOWN * 0.25)
        t1 = VGroup(
            Tex("Minimum amount of projectile energy for"),
            Tex("a reaction to proceed"),
            Tex(r"$E_{th}=0$ if $Q>0$"),
            Tex(r"$E_{th}>0$ if $Q<0$")
        ).arrange(DOWN).next_to(title, DOWN)
        self.play(Write(title))
        self.wait()
        self.play(Write(t1[0:2]))
        self.wait()
        self.play(Write(t1[2]))
        self.wait()
        self.play(Write(t1[3]))
        self.wait()
        self.play(FadeOut(t1))
        self.wait()

        t1 = VGroup(
            Tex(r"$\sqrt{E_y}=a\pm\sqrt{a^2+b}$"),
            Tex(r"If $Q<0$, $E_{th}$ makes it so that"),
            Tex(r"$\sqrt{a^2+b}\geq 0$")
        ).arrange(DOWN).next_to(title, DOWN)
        self.play(Write(t1))
        self.wait()
        self.play(FadeOut(t1))

        tt = MathTex(
            r"\sqrt{a^2+b} &= 0 \\",
            r"a^2+b &= 0 \\",
            r"a^2 &= -b \\",
            r"\left(\sqrt{\frac{m_xm_yE_x}{\left(m_y+m_Y\right)^2}}\text{cos}\theta\right)^2 &= -\frac{m_Y-m_x}{m_y+m_Y}E_x-\frac{m_Y}{m_y+m_Y}Q \\",
            r"\frac{m_xm_yE_x}{\left(m_y+m_Y\right)^2}\text{cos}^2 0 &= -\frac{m_Y-m_x}{m_y+m_Y}E_x-\frac{m_Y}{m_y+m_Y}Q \\",
            r"\frac{m_xm_yE_x}{\left(m_y+m_Y\right)^2} &= -\frac{m_Y-m_x}{m_y+m_Y}E_x-\frac{m_Y}{m_y+m_Y}Q \\",
            font_size=40
        ).next_to(title, DOWN)

        tt2 = MathTex(
            r"\frac{m_xm_yE_x}{\left(m_y+m_Y\right)^2} &= -\frac{m_Y-m_x}{m_y+m_Y}E_x-\frac{m_Y}{m_y+m_Y}Q \\",
            r"\frac{m_xm_yE_x}{\left(m_y+m_Y\right)^2} + \frac{m_Y-m_x}{m_y+m_Y}E_x &= -\frac{m_Y}{m_y+m_Y}Q \\",
            r"\left[\frac{m_xm_y}{\left(m_y+m_Y\right)^2} + \frac{m_Y-m_x}{m_y+m_Y}\right]E_x &= -\frac{m_Y}{m_y+m_Y}Q \\",
            r"\left[\frac{m_xm_y}{m_y+m_Y} + (m_Y-m_x)\right]E_x &= -m_YQ \\",
            r"\left[\frac{m_xm_y}{m_y+m_Y} + \frac{(m_Y-m_x)(m_y+m_Y)}{m_y+m_Y}\right]E_x &= -m_YQ \\",
            font_size=40
        ).next_to(title, DOWN)

        tt3 = MathTex(
            r"\left[\frac{m_xm_y}{m_y+m_Y} + \frac{(m_Y-m_x)(m_y+m_Y)}{m_y+m_Y}\right]E_x &= -m_YQ \\",
            r"\left[\frac{m_xm_y}{m_y+m_Y} + \frac{m_Y^2+m_ym_Y-m_xm_y-m_xm_Y}{m_y+m_Y}\right]E_x &= -m_YQ \\",
            r"\left[\frac{m_xm_y+m_Y^2+m_ym_Y-m_xm_y-m_xm_Y}{m_y+m_Y}\right]E_x &= -m_YQ \\",
            r"\left[\frac{m_Y^2+m_ym_Y-m_xm_Y}{m_y+m_Y}\right]E_x &= -m_YQ \\",
            r"\left[\frac{m_Y+m_y-m_x}{m_y+m_Y}\right]E_x &= -Q \\",
            font_size=40
        ).next_to(title, DOWN)

        tt4 = MathTex(
            r"\left[\frac{m_Y+m_y-m_x}{m_y+m_Y}\right]E_x &= -Q \\",
            r"E_x &= -\frac{m_y+m_Y}{m_Y+m_y-m_x}Q \\"
            r"E_x &\approx -\frac{m_x+m_X}{m_X}Q \\"
        ).next_to(title, DOWN)

        tt5 = Tex(r"$E^{k}_{th}\approx-\left(1+\frac{m_x}{m_X}\right)Q$").next_to(tt4, DOWN)

        for eq in tt:
            self.play(Write(eq), run_time=0.75)

        self.play(
            FadeOut(tt[:-1]),
            ReplacementTransform(tt[-1], tt2[0])
        )
        self.wait()

        for eq in tt2[1:]:
            self.play(Write(eq), run_time=0.75)

        self.play(
            FadeOut(tt2[:-1]),
            ReplacementTransform(tt2[-1], tt3[0])
        )
        self.wait()

        for eq in tt3[1:]:
            self.play(Write(eq), run_time=0.75)

        self.play(
            FadeOut(tt3[:-1]),
            ReplacementTransform(tt3[-1], tt4[0])
        )
        self.wait()

        for eq in tt4[1:]:
            self.play(Write(eq), run_time=0.75)
        self.wait()

        self.play(
            Write(tt5),
            Create(SurroundingRectangle(tt5), color=YELLOW, fill_color=BLACK, fill_opacity=1.0, buff=0.1)
        )
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class CoulombThreshold(Scene):
    def construct(self):
        X1 = VGroup(
            Proton().sprite[0],
            Tex("$p$")
        ).shift(LEFT * 2)
        X2 = VGroup(
            Proton().sprite[0].set_x(2).set_fill_color(PINK).set_stroke_color("#38003b").scale(2),
            Tex("$X$").set_x(2)
        )
        self.play(
            GrowFromCenter(X1),
            GrowFromCenter(X2)
        )
        self.wait()
        ar1 = Arrow(start=[-2.5, 0, 0], end=[-4.5, 0, 0])
        ar2 = Arrow(start=[3.0, 0, 0], end=[5.0, 0, 0])
        self.play(
            Create(ar1),
            Create(ar2)
        )
        self.wait()
        self.play(
            Wiggle(X1),
            Wiggle(X2)
        )
        self.play(
            X1.animate.shift(LEFT),
            X2.animate.shift(RIGHT),
            ar1.animate.shift(LEFT),
            ar2.animate.shift(RIGHT)
        )
        self.wait()
        self.play(
            FadeOut(ar1),
            FadeOut(ar2)
        )
        self.play(
            X1.animate.shift([4, 0, 0]).set_rate_func(rate_functions.there_and_back)
        )
        animations = [
            X1.animate.shift([-9, 0, 0]).set_rate_func(rate_functions.there_and_back),
            X2.animate.shift([7, 0, 0]).set_rate_func(rate_functions.ease_in_quad),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.35), run_time=4)
        self.wait()
        self.remove(X1)
        self.remove(X2)

        title = Tex(r"$\underline{\text{Coulomb threshold}}$").to_edge(UP).shift(DOWN * 0.25)
        self.play(Write(title))
        self.wait()
        t1 = Tex(r"$V(r)=\frac{1}{4\pi\epsilon_0}\frac{Z_xZ_Xe^2}{r}$").next_to(title, DOWN)
        t2 = Tex(r"$r(\text{in fm})\approx1.2\left(A_x^{1/3}+A_X^{1/3})$").next_to(t1, DOWN)
        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait()
        t3 = Tex(r"$E^{c}_{th}\approx\frac{1}{4\pi\epsilon_0}\frac{Z_xZ_Xe^2}{1.2\left(A_x^{1/3}+A_X^{1/3})[\text{fm}]}$").next_to(t2, DOWN)
        t4 = Tex(r"$E_{th}=\text{max}\left[E^{k}_{th},E^{c}_{th}\right]$").next_to(t3, DOWN)
        self.play(Write(t3))
        self.wait()
        self.play(Write(t4))
        self.wait()
        self.play(
            FadeOut(t1),
            FadeOut(t2),
            FadeOut(t3),
            t4.animate.set_y(t1.get_y())
        )
        self.wait()
        thresh = VGroup(
            Tex(r"$E^{k}_{th}\approx-\left(1+\frac{m_x}{m_X}\right)Q$"),
            Tex(r"$E^{c}_{th}\approx\frac{1}{4\pi\epsilon_0}\frac{Z_xZ_Xe^2}{1.2\left(A_x^{1/3}+A_X^{1/3})[\text{fm}]}$")
        ).arrange(RIGHT, buff=2).next_to(t4, DOWN)
        line = Line(start=[-10, thresh[0].get_y() - 0.75, 0], end=[10, thresh[0].get_y() - 0.75, 0])
        self.play(
            Write(thresh),
            Create(line)
        )
        self.wait()
        eq = Tex(r"$\text{Cl}^{35}_{17}(\alpha,n)\text{K}^{38}_{19}$").next_to(line, DOWN)
        self.play(Write(eq))
        self.wait()
        Q = Tex(r"$Q=-5.86\text{ MeV}$").next_to(eq, DOWN)
        self.play(Write(Q))
        self.wait()
        soln = VGroup(
            Tex(r"$E^{k}_{th}\approx-\left(1+\frac{m_x}{m_X}\right)Q$"),
            Tex(r"$E^{c}_{th}\approx\frac{1}{4\pi\epsilon_0}\frac{Z_xZ_Xe^2}{1.2\left(A_x^{1/3}+A_X^{1/3})[\text{fm}]}$")
        ).arrange(RIGHT, buff=2).next_to(Q, DOWN)
        self.play(Write(soln))
        self.wait()
        self.play(
            Transform(soln[0], Tex(r"$E^{k}_{th}\approx-\left(1+\frac{m_\alpha}{m_{\text{Cl}^{35}}}\right)Q$").set_x(thresh[0].get_x()).set_y(soln[1].get_y()))
        )
        self.wait()
        self.play(
            Transform(soln[0], Tex(r"$E^{k}_{th}\approx 6.49\text{ MeV}$").set_x(thresh[0].get_x()).set_y(soln[1].get_y()))
        )
        self.wait()
        self.play(
            Transform(soln[1], Tex(r"$E^{c}_{th}\approx\frac{1}{4\pi\epsilon_0}\frac{2\cdot 17 \cdot e^2}{1.2\left(4^{1/3}+35^{1/3})[\text{fm}]}$").set_x(thresh[1].get_x()).set_y(soln[0].get_y()))
        )
        self.wait()
        self.play(
            Transform(soln[1], Tex(r"$E^{c}_{th}\approx8.40\text{ MeV}$").set_x(thresh[1].get_x()).set_y(soln[0].get_y()))
        )
        tt5 = Tex(r"$E_{th}\approx8.40\text{ MeV}$").set_y(soln[1].get_y() - 1.0)
        self.play(
            Write(tt5),
            Create(SurroundingRectangle(tt5), color=YELLOW, fill_color=BLACK, fill_opacity=1.0, buff=0.1)
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()