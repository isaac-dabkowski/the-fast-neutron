from manim import *

import numpy as np
import random


class Lethargy(Scene):
    def construct(self):
        title = Tex(r"$\underline{\text{Lethargy}}$").to_edge(UP).shift(DOWN * 0.25)
        self.play(Write(title))
        self.wait()

        leth = Tex(r"$u=\text{ln}\left(\frac{E_0}{E}\right)$").next_to(title, DOWN)
        self.play(Write(leth))
        self.wait()

        enaught = Tex(r"$E_0$ is a reference energy, typically the ").next_to(leth, DOWN)
        enaught2 = Tex(r"highest energy we see in our system.").next_to(enaught, DOWN)
        self.play(Write(enaught))
        self.play(Write(enaught2))
        self.wait()

        self.play(
            FadeOut(enaught),
            FadeOut(enaught2)
        )
        self.wait()

        ax = Axes(
            x_range=[0, 2.5, 0.01],
            y_range=[0, 8],
            tips=True,
            y_axis_config={"include_numbers": False, "include_ticks": False},
            x_axis_config={"include_numbers": False, "include_ticks": False},
            x_length=6.0,
            y_length=3.25
        ).scale(1.2).next_to(leth, DOWN)
        ax_x_label = ax.get_x_axis_label(Tex("Energy", font_size = 50), edge=RIGHT, direction=RIGHT, buff=0.2)
        ax_y_label = ax.get_y_axis_label(Tex(r"$u$"), edge=LEFT, direction=LEFT, buff=0.1)
        self.play(
            FadeIn(ax),
            Write(ax_x_label),
            Write(ax_y_label)
        )
        l1 = ax.plot(
                lambda t:  np.log(1.5 / t),
                x_range = [0.001, 1.5],
                color=YELLOW
            )
        l2 = DashedLine(start=ax.c2p(1.5, 0), end=ax.c2p(1.5, 8))
        label1 = Tex(r"$E_0$").next_to(l2, RIGHT)
        self.play(
            Create(l1)
        )
        self.play(
            Create(l2),
            Write(label1)
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [title, leth]])
        self.wait()

        deltaleth = MathTex(
            r"\Delta u &= u' - u\\",
            r"&= \text{ln}\left(\frac{E_0}{E'}\right) - \text{ln}\left(\frac{E_0}{E}\right)\\",
            r"&= \text{ln}(E_0) - \text{ln}(E') - \text{ln}(E_0) + \text{ln}(E)\\",
            r"&= \text{ln}(E) - \text{ln}(E')\\",
            r"&= \text{ln}\left(\frac{E}{E'}\right)\\",
            font_size=45
        ).next_to(leth, DOWN)
        self.play(Write(deltaleth[0]))
        self.play(Write(deltaleth[1]))
        self.play(Write(deltaleth[2]))
        self.play(Write(deltaleth[3]))
        self.play(Write(deltaleth[4]))
        self.wait()
        self.play(
            Transform(deltaleth, Tex(r"$\Delta u =\text{ln}\left(\frac{E}{E'}\right)$", font_size=45).next_to(leth, DOWN))
        )
        self.wait()
        facts = MathTex(
            r"\text{For }E\rightarrow E\text{ }(\text{cos}\theta)=0&\text{, }\Delta u =\text{ln}\left(\frac{E}{E}\right)=0\\",
            r"\text{For }E\rightarrow \alpha E\text{ }(\text{cos}\theta)=-1&\text{, }\Delta u =\text{ln}\left(\frac{E}{\alpha E}\right)=\text{ln}\left(\frac{1}{\alpha}\right)",
            font_size=45
        ).next_to(deltaleth, DOWN)
        self.play(Write(facts[0]))
        self.wait()
        self.play(Write(facts[1]))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [title, leth]])
        self.play(Transform(title, Tex(r"$\underline{\text{Average change in lethargy}}$").to_edge(UP).shift(DOWN * 0.25)))
        self.wait()

        deriveavgleth = MathTex(
            r"p(u\rightarrow u')|du'|&=p(E\rightarrow E')|dE'|\\",
            r"p(u\rightarrow u')&=p(E\rightarrow E')\left|\frac{dE'}{du'}\right|\\",
            r"p(u\rightarrow u')&=-p(E\rightarrow E')E'\\"
        ).next_to(leth, DOWN).shift(LEFT * 0.1)
        self.play(Write(deriveavgleth[0]))
        self.wait()
        self.play(Write(deriveavgleth[1]))

        jacobian = MathTex(
            r"u'=\text{ln}\left(\frac{E_0}{E'}\right)&\text{, }E'=E_0e^{-u'}\\",
            r"\left|\frac{dE'}{du'}\right|=-E_0&e^{-u'}=-E'\\"
        ).next_to(deriveavgleth, DOWN)
        self.play(Write(jacobian[0]))
        self.play(Write(jacobian[1]))
        self.wait()
        self.play(
            FadeOut(jacobian)
        )
        self.play(Write(deriveavgleth[2]))
        self.wait()
        lethpdf = MathTex(
            r"p(u\rightarrow u')&=p(E'\rightarrow E)E'\\",
            r"&=\frac{1}{1-\alpha}\frac{E'}{E}\\",
            r"&=\frac{1}{1-\alpha}\frac{E_0e^{-u'}}{E_0e^{-u}}\\",
            r"&=\frac{1}{1-\alpha}e^{-(u-u')}\\",
        ).next_to(deriveavgleth, DOWN).shift(RIGHT * 0.1)
        self.play(Write(lethpdf[0]))
        self.wait()
        self.play(
            FadeOut(deriveavgleth),
            lethpdf[0].animate.next_to(leth, DOWN)
        )
        lethpdf[1].next_to(lethpdf[0], DOWN).shift(RIGHT * 0.7)
        lethpdf[2].next_to(lethpdf[1], DOWN).align_to(lethpdf[1], LEFT)
        lethpdf[3].next_to(lethpdf[2], DOWN).align_to(lethpdf[1], LEFT)
        self.play(Write(lethpdf[1]))
        self.play(Write(lethpdf[2]))
        self.play(Write(lethpdf[3]))
        self.wait()
        self.play(
            Transform(lethpdf, Tex(r"$p(u\rightarrow u')=\frac{1}{1-\alpha}e^{-(u-u')}$", font_size=45).next_to(leth, DOWN))
        )
        self.wait()
        xeq = Tex(r"$x = u' - u$").next_to(lethpdf, DOWN)
        self.play(Write(xeq))
        self.wait()
        xieqn = Tex(r"$\xi=\left<x\right>=\int^{\text{ln}\left(\frac{1}{\alpha}\right)}_0\frac{x}{1-\alpha}e^{-x}dx$").next_to(xeq, DOWN)
        self.play(Write(xieqn))
        self.wait()

        xidef = Tex(r"$\xi=\left<u'-u\right>=1+\frac{\alpha\text{ln}(\alpha)}{1-\alpha}$").next_to(xieqn, DOWN).shift(DOWN * 0.5)
        xibox = SurroundingRectangle(xidef)
        self.play(Write(xidef), Create(xibox))
        self.wait()

        self.play(
            FadeOut(xibox),
            FadeOut(lethpdf),
            FadeOut(xeq),
            FadeOut(xieqn),
            xidef.animate.next_to(leth, DOWN)
        )
        self.wait()

        ncol = VGroup(
            Tex(r"For $N$ scatters, the average change in"),
            Tex(r"lethargy is just $N\xi$.")
        ).arrange(DOWN).next_to(xidef, DOWN)
        self.play(Create(ncol))
        self.wait()

        tf = Tex(r"$\therefore$").next_to(ncol, DOWN)
        ntex = VGroup(
            Tex(r"The average number of collisions needed"),
            Tex(r"to go from $E_1$ to $E_2$ is:")
        ).arrange(DOWN).next_to(tf, DOWN)
        neqn = Tex(r"$\left<N\right>=\frac{1}{\xi}\Delta u = \frac{1}{\xi}\text{ln}\left(\frac{E_1}{E_2}\right)$").next_to(ntex, DOWN)
        nbox = SurroundingRectangle(neqn)
        self.play(Write(tf))
        self.play(Create(ntex))
        self.play(Write(neqn), Create(nbox))
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class ScatterSim(Scene):
    def construct(self):
        def downscatter(A):
            N = 0
            alpha = ((A - 1) / (A + 1))**2
            E = 2.0e6
            while E > 1:
                xi = random.random()
                E = E - (1 - alpha) * xi * E
                N += 1
            return N - 1

        def downscatter_w_hist(A):
            alpha = ((A- 1) / (A + 1))**2
            E = 2.0e6
            e_hist = [E]
            while E > 1.0:
                xi = random.random()
                E = E - (1 - alpha) * xi * E
                e_hist.append(E)
            return e_hist, len(e_hist) - 1

        def mean_line():
            if sum([val - 1 for val in data]) > 0:
                avgval = sum([idx * (val-1) for idx, val in enumerate(data)]) / sum([val - 1 for val in data])
            else:
                avgval = len(data) / 2
            meanline = DashedLine(
                start=histogram.c2p(avgval, 10**histogram.y_range[1]),
                end=histogram.c2p(avgval, 1)
            )
            return meanline

        title = Tex(r"$\underline{\text{Scattering simulation}}$").to_edge(UP).shift(DOWN * 0.25)
        self.play(Write(title))
        self.wait()

        t1 = Tex(r"Neutrons will start at 2 MeV, let's see how many").next_to(title, DOWN)
        t2 = Tex(r"scatters it takes to bring them down to 1 eV.").next_to(t1, DOWN)
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait()
        self.play(
            FadeOut(t1),
            FadeOut(t2)
        )

        # Quick demo
        ax = Axes(
            x_range=[0, 25, 5],
            y_range=[-1.5, 7, 1],
            tips=False,
            x_length=8.0,
            y_length=4.0,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )
        ax_x_label = ax.get_x_axis_label(Tex(r"\# of scatters", font_size = 50), edge=DOWN, direction=DOWN, buff=0.2)
        ax_y_label = ax.get_y_axis_label(Tex(r"Energy (eV)"), edge=LEFT, direction=LEFT, buff=0.1).rotate(90 * DEGREES)
        dl = DashedLine(start=ax.c2p(0, 1), end=ax.c2p(25, 1))
        alabel = Tex(r"$A=1$").next_to(ax, RIGHT)

        lines = VGroup()
        for i in range(5):
            e_hist, _ = downscatter_w_hist(1)
            hist_curve = ax.plot_line_graph(
                x_values = [0] + [i + 1 for i in range(len(e_hist) - 1) for _ in range(2)] + [len(e_hist)],
                y_values = [e for e in e_hist for _ in range(2)],
                add_vertex_dots=False
            )
            lines.add(hist_curve)

        self.play(Create(ax), Write(ax_x_label), Write(ax_y_label), Create(dl), Write(alabel))
        self.wait()
        self.play(Create(lines[0]))
        self.wait()
        for i in range(len(lines)-1):
            self.play(Create(lines[i+1]))
            self.wait(0.25)
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != title])
        self.wait()
        # Histogram helper functions
        # Lots of code from brianamedee/3B1B-Animated-Tutorials
        def get_bars(histogram, data):
            bars = VGroup()
            for x, prop in enumerate(np.array(data)):
                p1 = VectorizedPoint().move_to(histogram.c2p(x, 1))
                p2 = VectorizedPoint().move_to(histogram.c2p(x + 1, 1))
                p3 = VectorizedPoint().move_to(histogram.c2p(x + 1, prop))
                p4 = VectorizedPoint().move_to(histogram.c2p(x, prop))
                points = VGroup(p1, p2, p3, p4)
                bar = Rectangle().replace(points, stretch=True)
                bar.set_style(
                    fill_color=[YELLOW, GREEN],
                    fill_opacity=0.8,
                    stroke_color=[YELLOW, GREEN],
                )
                bars.add(bar)
            return bars

        ##THE UPDATER FUNCTION##
        def update(dummy, num_per_frame):
            for i in range(num_per_frame):
                N = downscatter(A)
                data[N] += 1
            bars.become(get_bars(histogram=histogram, data=data))
            bars.set_style(
                fill_color=[BLUE_B, BLUE_D], fill_opacity=0.8, stroke_color=BLUE
            )

        A = 1
        possible_outcomes = 50
        data = np.ones(possible_outcomes)  # Possible outcomes as an array
        histogram = Axes(
            x_range=[0, possible_outcomes, 10],
            y_range=[0, 5, 1],
            tips=False,
            x_length=10.0,
            y_length=4.0,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )
        ax_x_label = histogram.get_x_axis_label(Tex(r"\# of scatters to go from 2 MeV to 1 eV", font_size = 50), edge=DOWN, direction=DOWN, buff=0.2)
        ax_y_label = histogram.get_y_axis_label(Tex(r"\# of simulations"), edge=LEFT, direction=LEFT, buff=0.1).rotate(90 * DEGREES).shift(LEFT)
        bars = get_bars(histogram=histogram, data=data)
        text_counter = Tex("Total trials: ").scale(0.6).to_edge(RIGHT, buff=2.5)
        counter = always_redraw(
            lambda: Integer().scale(0.6).set_value(sum(data) - len(data)).next_to(text_counter, RIGHT, buff=0.3)
        )
        helper_tex = VGroup(
            Tex(r"$A=1$").scale(0.6),
            Tex(r"$\alpha=\left(\frac{A-1}{A+1}\right)^2=0$").scale(0.6),
            Tex(r"$\xi \equiv 1 \text{ if }A=1$").scale(0.6),
            Tex(r"$\left< N \right>=\frac{1}{\xi}\text{ln}\left(\frac{2\text{ MeV}}{1\text{ ev}}\right) \approx 14.5$").scale(0.6)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(text_counter, UP).align_to(text_counter, LEFT)
        meanline = always_redraw(mean_line)
        avg_counter = always_redraw(
            lambda: DecimalNumber(show_ellipsis=False, num_decimal_places=2).scale(0.6).set_value(sum([idx * (val-1) for idx, val in enumerate(data)]) / sum([val - 1 for val in data])).next_to(meanline, RIGHT, buff=0.3).align_to(meanline, UP)
        ) # Minus ones due to everything starting at 1 for log scale
        self.play(Create(histogram), Write(ax_x_label), Write(ax_y_label))
        self.wait()
        self.play(
            Write(helper_tex[0])
        )
        self.wait(0.5)
        self.play(
            Write(helper_tex[1])
        )
        self.wait(0.5)
        self.play(
            Write(helper_tex[2])
        )
        self.wait()
        self.add(bars, counter, text_counter, meanline, avg_counter)
        self.play(UpdateFromFunc(bars, lambda m: update(m, 1)), run_time=4)
        self.play(UpdateFromFunc(bars, lambda m: update(m, 2)), run_time=2)
        self.play(UpdateFromFunc(bars, lambda m: update(m, 10)), run_time=4)
        self.wait()
        self.play(Write(helper_tex[3]))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [title]])
        self.wait()

        # A = 2
        A = 2
        possible_outcomes = 50
        data = np.ones(possible_outcomes)  # Possible outcomes as an array
        histogram = Axes(
            x_range=[0, possible_outcomes, 10],
            y_range=[0, 5, 1],
            tips=False,
            x_length=8.0,
            y_length=4.0,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )
        ax_x_label = histogram.get_x_axis_label(Tex(r"\# of scatters to go from 2 MeV to 1 eV", font_size = 50), edge=DOWN, direction=DOWN, buff=0.2)
        ax_y_label = histogram.get_y_axis_label(Tex(r"\# of simulations"), edge=LEFT, direction=LEFT, buff=0.1).rotate(90 * DEGREES)
        bars = get_bars(histogram=histogram, data=data)
        text_counter = Tex("Total trials: ").scale(0.6).to_edge(RIGHT, buff=2.5)
        counter = always_redraw(
            lambda: Integer().scale(0.6).set_value(sum(data) - len(data)).next_to(text_counter, RIGHT, buff=0.3)
        )
        helper_tex = VGroup(
            Tex(r"$A=2$").scale(0.6),
            Tex(r"$\alpha=\left(\frac{A-1}{A+1}\right)^2=0.11$").scale(0.6),
            Tex(r"$\xi=1+\frac{\alpha\text{ln}(\alpha)}{1-\alpha}=0.73$").scale(0.6),
            Tex(r"$\left< N \right>=\frac{1}{\xi}\text{ln}\left(\frac{2\text{ MeV}}{1\text{ ev}}\right)\approx 20$").scale(0.6)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(text_counter, UP).align_to(text_counter, LEFT)
        meanline = always_redraw(mean_line)
        self.play(Create(histogram), Write(ax_x_label), Write(ax_y_label))
        self.wait()
        self.play(
            Write(helper_tex[0]),
            Write(helper_tex[1]),
            Write(helper_tex[2])
        )
        self.wait()
        self.add(bars, counter, text_counter, meanline, avg_counter)
        self.play(UpdateFromFunc(bars, lambda m: update(m, 3)), run_time=2)
        self.play(UpdateFromFunc(bars, lambda m: update(m, 13)), run_time=4)
        self.wait()
        self.play(Write(helper_tex[3]))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [title]])
        self.wait()

        # A = 12
        A = 12
        possible_outcomes = 200
        data = np.ones(possible_outcomes)  # Possible outcomes as an array
        histogram = Axes(
            x_range=[0, possible_outcomes, 20],
            y_range=[0, 5, 1],
            tips=False,
            x_length=8.0,
            y_length=4.0,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )
        ax_x_label = histogram.get_x_axis_label(Tex(r"\# of scatters to go from 2 MeV to 1 eV", font_size = 50), edge=DOWN, direction=DOWN, buff=0.2)
        ax_y_label = histogram.get_y_axis_label(Tex(r"\# of simulations"), edge=LEFT, direction=LEFT, buff=0.1).rotate(90 * DEGREES)
        bars = get_bars(histogram=histogram, data=data)
        text_counter = Tex("Total trials: ").scale(0.6).to_edge(RIGHT, buff=2.5)
        counter = always_redraw(
            lambda: Integer().scale(0.6).set_value(sum(data) - len(data)).next_to(text_counter, RIGHT, buff=0.3)
        )
        helper_tex = VGroup(
            Tex(r"$A=12$").scale(0.6),
            Tex(r"$\alpha=\left(\frac{A-1}{A+1}\right)^2=0.72$").scale(0.6),
            Tex(r"$\xi=1+\frac{\alpha\text{ln}(\alpha)}{1-\alpha}=0.16$").scale(0.6),
            Tex(r"$\left< N \right>=\frac{1}{\xi}\text{ln}\left(\frac{2\text{ MeV}}{1\text{ ev}}\right)\approx 92$").scale(0.6)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(text_counter, UP).align_to(text_counter, LEFT)
        meanline = always_redraw(mean_line)
        self.play(Create(histogram), Write(ax_x_label), Write(ax_y_label))
        self.wait()
        self.play(
            Write(helper_tex[0]),
            Write(helper_tex[1]),
            Write(helper_tex[2])
        )
        self.wait()
        self.add(bars, counter, text_counter, meanline, avg_counter)
        self.play(UpdateFromFunc(bars, lambda m: update(m, 3)), run_time=2)
        self.play(UpdateFromFunc(bars, lambda m: update(m, 13)), run_time=4)
        self.wait()
        self.play(Write(helper_tex[3]))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

        ax = Axes(
            x_range=[0, 300, 50],
            y_range=[0, 1800, 200],
            tips=False,
            y_axis_config={"include_numbers": True, "include_ticks": True},
            x_axis_config={"include_numbers": True, "include_ticks": True},
            x_length=8.0,
            y_length=5.5,
        )
        ax_x_label = ax.get_x_axis_label(Tex(r"$A$", font_size = 50), edge=DOWN, direction=DOWN, buff=0.2)
        ax_y_label = ax.get_y_axis_label(Tex(r"$\left< N \right>$ (2 MeV $\rightarrow$ 1 eV)"), edge=LEFT, direction=LEFT, buff=0.1).rotate(90 * DEGREES).shift(LEFT)
        self.play(
            FadeIn(ax),
            Write(ax_x_label),
            Write(ax_y_label)
        )
        l1 = ax.plot(
            lambda A: 1 / (1 + (((A-1)/(A+1))**2 * np.log(((A-1)/(A+1))**2))/(1 - ((A-1)/(A+1))**2)) * np.log(2e6),
            x_range = [1.01, 250],
            color=YELLOW
        )
        l2 = VGroup(
            DashedLine(start=ax.c2p(54, 0), end=ax.c2p(54, 411)),
            DashedLine(start=ax.c2p(54, 411), end=ax.c2p(0, 411))
        )
        label1 = Tex(r"$^{54}\text{Fe}$").next_to(l2, RIGHT)
        label2 = Tex(r"411").next_to(l2, UP)
        l3 = VGroup(
            DashedLine(start=ax.c2p(238, 0), end=ax.c2p(238, 1730)),
            DashedLine(start=ax.c2p(238, 1730), end=ax.c2p(0, 1730))
        )
        label3 = Tex(r"$^{238}\text{U}$").next_to(l3, RIGHT)
        label4 = Tex(r"1730").next_to(l3, UP)
        self.play(
            Create(l1)
        )
        self.play(
            Create(l2),
            Write(label1),
            Write(label2)
        )
        self.wait()
        self.play(
            Create(l3),
            Write(label3),
            Write(label4)
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
