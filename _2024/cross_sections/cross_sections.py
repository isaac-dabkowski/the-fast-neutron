from manim import *
from resources import Isotope
import random
class XSTitleCard(Scene):
    def construct(self):
        section_title = Tex("What is a cross section?")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class XSIntro(Scene):
    def construct(self):
        # Neutron beam
        neutrons = VGroup(
            Circle(
                radius=0.4,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0),
            Circle(
                radius=0.4,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0),
            Circle(
                radius=0.4,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0),
            Circle(
                radius=0.4,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0),
            Circle(
                radius=0.4,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0),
            Circle(
                radius=0.4,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0)
        ).arrange(DOWN, buff=2.5).shift(LEFT * 5).scale(0.3)

        self.play(Create(neutrons))
        self.wait()

        self.play(
            AnimationGroup(*[n.animate.shift([13, 0, 0]) for n in neutrons], lag_ratio=0.3)
        )
        self.wait()

        for n in neutrons:
            n.shift([-13, 0, 0])
        self.play(Create(neutrons))
        self.wait()

        sheet = VGroup(
            DashedVMobject(
                Rectangle(height=6, width=1), num_dashes=50),
                Circle(
                    radius=0.18,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0).shift(DOWN * 2.5),
                Circle(
                    radius=0.18,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0).shift(DOWN),
                Circle(
                    radius=0.18,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0),
                Circle(
                    radius=0.18,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0).shift(UP),
                Circle(
                    radius=0.18,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0).shift(UP * 1.5),
                Circle(
                    radius=0.18,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0).shift(UP * 2)
        )
        self.play(AnimationGroup(*[Create(i) for i in sheet]))
        self.wait()

        beam_on_sheet1 = AnimationGroup(
            *[
                neutrons[0].animate.shift([13, 0, 0]),
                neutrons[1].animate.shift([5, 0, 0])
            ],
            lag_ratio=0.3
        ).set_run_time(1).set_rate_func(rate_functions.linear)
        self.play(beam_on_sheet1)
        collision1 = AnimationGroup(
            *[
                Uncreate(neutrons[1]),
                Wiggle(sheet[-2], scale_value=1.5)
            ]
        ).set_run_time(0.5)
        self.play(collision1)
        beam_on_sheet2 = AnimationGroup(
            *[
                neutrons[2].animate.shift([13, 0, 0]),
                neutrons[3].animate.shift([13, 0, 0]),
                neutrons[4].animate.shift([13, 0, 0]),
                neutrons[5].animate.shift([5, 0, 0])
            ],
            lag_ratio=0.3
        ).set_run_time(2).set_rate_func(rate_functions.linear)
        self.play(beam_on_sheet2)
        collision1 = AnimationGroup(
            *[
                Uncreate(neutrons[-1]),
                Wiggle(sheet[1], scale_value=1.5)
            ]
        ).set_run_time(0.5)
        self.play(collision1)
        self.wait()

        self.play(FadeOut(sheet))
        self.wait()

        q1 = VGroup(
            Tex("What is the probability that a neutron"),
            Tex("will be absorbed by the sheet?")
        ).arrange(DOWN)
        self.play(
            AnimationGroup(
                *[Write(q1[0]), Write(q1[1])],
                lag_ratio=1.0
            ).set_run_time(1.5)
        )
        self.wait()

        self.play(FadeOut(q1))
        self.wait()

        q1 = Tex("What is the probability that a neutron will be absorbed by the sheet?", font_size=42).to_edge(UP)
        sheet_headon = VGroup(
            DashedVMobject(
                Rectangle(height=6, width=6), num_dashes=50, fill_opacity=0),
                Circle(
                    radius=0.3,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0).shift(DOWN * 2.5).shift(LEFT),
                Circle(
                    radius=0.3,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0).shift(DOWN).shift(RIGHT * 2.5),
                Circle(
                    radius=0.3,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0).shift(LEFT * 0.5),
                Circle(
                    radius=0.3,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0).shift(UP).shift(LEFT*2.5),
                Circle(
                    radius=0.3,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0).shift(UP * 1.5).shift(RIGHT),
                Circle(
                    radius=0.3,
                    color=ORANGE,
                ).set_fill("#b57f21", opacity=1.0).shift(UP * 2).shift(RIGHT * 2)
        ).shift(LEFT * 3.5 + DOWN * 0.5)

        self.play(AnimationGroup(*[Create(i) for i in sheet_headon] + [Create(q1)]))
        self.wait()
        self.play(AnimationGroup(*[Wiggle(i, scale_value=1.2) for i in sheet_headon[1:]]))
        self.wait()
        sheet_headon_bkgd = VGroup(
            Rectangle(height=6, width=6, color=GRAY).set_fill(color=GRAY, opacity=0.5)
        ).shift(LEFT * 3.5 + DOWN * 0.5).set_z_index(-1)
        self.play(FadeIn(sheet_headon_bkgd))
        self.play(FadeOut(sheet_headon_bkgd))
        self.wait()

        peq1 = VGroup(
            Tex(r"$p=\frac{\text{Area of atoms}}{\text{Area of sheet}}$", font_size=42),
            Tex(r"$N=\text{Atom density}$", font_size=42),
            Tex(r"$A=\text{Sheet area}$", font_size=42),
            Tex(r"$\Delta x=\text{Sheet thickness}$", font_size=42),
            Tex(r"$\sigma=\text{Area per atom}$", font_size=42)
        ).arrange(DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT).shift(RIGHT * 3.5 + UP * 0.5)
        peq1[0].shift(LEFT)
        self.play(Write(peq1[0]))
        self.wait()
        self.play(
            Write(peq1[1]),
            Write(peq1[2]),
            Write(peq1[3]),
            Write(peq1[4])
        )
        self.wait()

        peq2 = Tex(r"$p=\frac{N\sigma A \Delta x}{A}$", font_size=42).shift(RIGHT * 3.5).next_to(peq1, DOWN).align_to(peq1, LEFT).shift(DOWN * 0.6)
        self.play(Write(peq2))
        self.wait()

        self.play(
            Transform(peq2, Tex(r"$p=\frac{N\sigma A \Delta x}{A}=N\sigma \Delta x$", font_size=42).shift(RIGHT * 3.5).next_to(peq1, DOWN).align_to(peq1, LEFT).shift(DOWN * 0.6))
        )
        self.wait()

        br = SurroundingRectangle(peq2)
        self.play(Create(br))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class XSDef(Scene):
    def construct(self):
        microtitle = Tex(r"\underline{Microscopic cross section ``$\sigma$''}", font_size=40).to_edge(UP).shift(UP * 0.2)
        self.play(Write(microtitle))
        self.wait()

        microdef = Tex(r"The microscopic cross section is an ``effective'' area\\which describes a probability of interaction.", font_size=40).next_to(microtitle, DOWN).shift(DOWN * 0.2)
        self.play(Write(microdef))
        self.wait()

        barnsdef = Tex("The units are ``barns'', where 1 barn is $10^{-24}$ cm$^2$.", font_size=40).next_to(microdef, DOWN).shift(DOWN * 0.2)
        self.play(Write(barnsdef))
        self.wait()

        atom = Circle(
            radius=0.5,
            color=ORANGE,
        ).set_fill("#b57f21", opacity=1).shift(DOWN * 2.5)
        invisline = Line(start=atom.get_center(), end=atom.get_right())
        brace = Brace(invisline, direction=UP).align_to(atom, UP).shift(UP * 0.5)
        l1 = DashedLine(start=atom.get_center(), end=brace.get_left())
        l2 = DashedLine(start=atom.get_right(), end=brace.get_right())
        brace.shift(UP * 0.2)
        bracelabel = Tex(r"$\approx10^{-15}$ m", font_size=30).next_to(brace, UP)
        self.play(Create(atom))
        self.play(Create(brace), Write(bracelabel), Create(l1), Create(l2))
        self.wait()

        self.play(FadeOut(atom), FadeOut(brace), FadeOut(bracelabel), FadeOut(l1), FadeOut(l2))
        self.wait()

        horzline = Line(start=[-15, 0, 0], end=[15, 0, 0]).next_to(barnsdef, DOWN).shift(DOWN * 0.2)

        macrotitle = Tex(r"\underline{Macroscopic cross section ``$\Sigma$''}", font_size=40).next_to(horzline, DOWN).shift(DOWN * 0.2)
        self.play(FadeIn(horzline), Write(macrotitle))
        self.wait()

        macroform = Tex(r"$\Sigma = N \sigma$, units of cm$^{-1}$.", font_size=40).next_to(macrotitle, DOWN).shift(DOWN * 0.2)
        ndef = Tex("$N$ is atomic density in units of atoms/volume.", font_size=40).next_to(macroform, DOWN).shift(DOWN * 0.2)
        self.play(Write(macroform))
        self.play(Write(ndef))
        self.wait()

        macrodef = Tex(r"The macroscopic cross section describes the probability per length\\of travel for an interaction to occur in a specific sample of material.", font_size=40).next_to(ndef, DOWN).shift(DOWN * 0.2)
        self.play(Write(macrodef))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class BeamIntensity(Scene):
    def construct(self):
        font_size = 40
        spacer = 0.2
        title = Tex(r"\underline{Radiation attentuation}", font_size=font_size).to_edge(UP).shift(UP * spacer)
        self.play(Write(title))
        self.wait()

        idef = Tex(r"$\mathrm{I}(x)=$The intensity of a beam penetrating a slab.", font_size=font_size).next_to(title, DOWN).shift(DOWN * spacer)
        self.play(Write(idef))
        self.wait()

        didx = Tex(r"$\frac{d\mathrm{I}}{dx}=-\Sigma(x)\mathrm{I}(x)$", font_size=font_size).next_to(idef, DOWN).shift(DOWN * spacer)
        self.play(Write(didx))
        self.wait()

        constI = Tex(r"If $\Sigma(x)$ is a constant, $\mathrm{I}(x)=\mathrm{I}(0)e^{-\Sigma x}$", font_size=font_size).next_to(didx, DOWN).shift(DOWN * spacer)
        self.play(Write(constI))
        self.wait()

        notconstI = Tex(r"If $\Sigma(x)$ varies with $x$, $\mathrm{I}(x)=\mathrm{I}(0)\cdot\text{exp}\left(-\int^x_0\Sigma(x')dx'\right)$", font_size=font_size).next_to(constI, DOWN).shift(DOWN * spacer)
        self.play(Write(notconstI))
        self.wait()

        self.play(FadeOut(idef), FadeOut(didx), FadeOut(constI), FadeOut(notconstI))
        self.wait()

        ax = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 1.3, 2],
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": False}
        ).shift(DOWN * 0.3)
        ax.scale(0.75)
        ax_x_label = ax.get_x_axis_label(Tex(r"$x$ (cm)", font_size=font_size), edge=DOWN, direction=DOWN).shift(DOWN * 0.2)
        ax_y_label = ax.get_y_axis_label(Tex(r"$\mathrm{I(x)}$", font_size=font_size), edge=LEFT, direction=LEFT).shift(LEFT * 0.2)
        self.play(Create(ax), Write(ax_x_label), Write(ax_y_label))
        self.wait()

        slab = VGroup(
            Line(start=ax.c2p(1, 1.3, 0), end=ax.c2p(1, 0, 0)),
            Line(start=ax.c2p(3, 1.3, 0), end=ax.c2p(3, 0, 0)),
            Polygon(
                *[ax.c2p(1, 1.3, 0), ax.c2p(1, 0, 0), ax.c2p(3, 0, 0), ax.c2p(3, 1.3, 0)]
            ).set_fill(color=RED, opacity=0.2).set_stroke(opacity=0),
            Tex(r"$\Sigma=1.0$ cm$^{-1}$", font_size=font_size).set_x(ax.x_axis.n2p(2)[0]).set_y(ax.y_axis.n2p(1.15)[1])
        )
        self.play(Create(slab[0]), Create(slab[1]))
        self.play(FadeIn(slab[2]), Write(slab[3]))
        self.wait()

        constI = Tex(r"$\mathrm{I}(x)=\mathrm{I}(0)e^{-\Sigma x}$", font_size=font_size).next_to(title, DOWN).shift(DOWN * spacer)
        self.play(Write(constI))
        self.wait()

        xvals = np.linspace(ax.x_range[0], ax.x_range[1], 100)
        ivals = np.zeros(len(xvals))
        for i, x in enumerate(xvals):
            if x < 1:
                ivals[i] = 1
            elif x >= 1 and x < 3:
                ivals[i] = np.exp(-(x-1))
            else:
                ivals[i] = np.exp(-(2))
        i_curve = ax.plot_line_graph(
            x_values = xvals,
            y_values = ivals,
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=4,
        )
        self.play(Create(i_curve).set_run_time(3))
        self.wait()

        ilabels = VGroup(
            Tex(r"$\mathrm{I}(0)$", font_size=font_size).move_to(ax.c2p(0.5, 1.1, 0)),
            Tex(r"$\mathrm{I}(0)e^{-(3 - 1) \cdot 1.0}$", font_size=font_size).move_to(ax.c2p(4, 0.25, 0))
        )
        self.play(Create(ilabels))
        self.wait()

        self.play(FadeOut(slab), FadeOut(i_curve), FadeOut(ilabels), FadeOut(constI))
        self.wait()

        # Multislab
        slab = VGroup(
            Line(start=ax.c2p(1, 1.3, 0), end=ax.c2p(1, 0, 0)),
            Line(start=ax.c2p(2, 1.3, 0), end=ax.c2p(2, 0, 0)),
            Line(start=ax.c2p(3, 1.3, 0), end=ax.c2p(3, 0, 0)),
            Polygon(
                *[ax.c2p(1, 1.3, 0), ax.c2p(1, 0, 0), ax.c2p(2, 0, 0), ax.c2p(2, 1.3, 0)]
            ).set_fill(color=RED, opacity=0.2).set_stroke(opacity=0),
            Polygon(
                *[ax.c2p(2, 1.3, 0), ax.c2p(2, 0, 0), ax.c2p(3, 0, 0), ax.c2p(3, 1.3, 0)]
            ).set_fill(color=BLUE, opacity=0.2).set_stroke(opacity=0),
            Tex(r"$\Sigma=0.3$ cm$^{-1}$", font_size=font_size * 0.7).set_x(ax.x_axis.n2p(1.5)[0]).set_y(ax.y_axis.n2p(1.15)[1]),
            Tex(r"$\Sigma=1.0$ cm$^{-1}$", font_size=font_size * 0.7).set_x(ax.x_axis.n2p(2.5)[0]).set_y(ax.y_axis.n2p(1.15)[1])
        )
        self.play(Create(slab[0]), Create(slab[1]), Create(slab[2]))
        self.play(FadeIn(slab[3]), FadeIn(slab[4]), Write(slab[5]), Write(slab[6]))
        self.wait()

        notconstI = Tex(r"$\mathrm{I}(x)=\mathrm{I}(0)\cdot\text{exp}\left(-\int^x_0\Sigma(x')dx'\right)$", font_size=font_size).next_to(title, DOWN).shift(DOWN * spacer)
        self.play(Write(notconstI))
        self.wait()

        xvals = np.linspace(ax.x_range[0], ax.x_range[1], 100)
        ivals = np.zeros(len(xvals))
        for i, x in enumerate(xvals):
            if x < 1:
                ivals[i] = 1
            elif x >= 1 and x < 2:
                ivals[i] = np.exp(-(x-1)*0.3)
            elif x >= 2 and x < 3:
                ivals[i] = np.exp(-(0.3 + (x-2)))
            else:
                ivals[i] = np.exp(-(1.3))
        i_curve = ax.plot_line_graph(
            x_values = xvals,
            y_values = ivals,
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=4,
        )
        self.play(Create(i_curve).set_run_time(3))
        self.wait()

        ilabels = VGroup(
            Tex(r"$\mathrm{I}(0)$", font_size=font_size).move_to(ax.c2p(0.5, 1.1, 0)),
            Tex(r"$\mathrm{I}(0)e^{-\left((2 - 1)\cdot0.3\right)}$", font_size=font_size),
            Tex(r"$\mathrm{I}(0)e^{-((2 - 1)\cdot0.3 + (3 - 2)\cdot 1.0)}$", font_size=font_size).move_to(ax.c2p(4.1, 0.4, 0)),
            DashedLine(start=ax.c2p(2, np.exp(-0.3), 0), end=ax.c2p(3.2, np.exp(-0.3), 0))
        )
        ilabels[1].next_to(ilabels[3], RIGHT)
        self.play(Create(ilabels))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class GeometricAttenuation(Scene):
    def construct(self):
        font_size = 40
        spacer = 0.2
        title = Tex(r"\underline{Geometric attentuation}", font_size=font_size).to_edge(UP).shift(UP * spacer)
        self.play(Write(title))
        self.wait()

        source = VGroup(
            Dot(radius=0.15),
            Tex("Source", font_size=font_size)
        )
        source[0].set_center([0, 0, 0])
        source[1].next_to(source[0], UP)
        self.play(Create(source))
        self.wait()

        r0 = 0.7
        r1 = 3.25
        rays = VGroup(
            *[
                Arrow(start=[r0 * np.cos(theta), r0 * np.sin(theta), 0], end=[r1 * np.cos(theta), r1 * np.sin(theta), 0])
                for theta in np.linspace(0, 2 * PI, 10)
            ]
        )
        self.play(Create(rays))
        self.wait()

        diagram = VGroup(source, rays)
        self.play(diagram.animate.shift(LEFT * 3.5))
        self.wait()

        fluxdef = Tex(r"Flux ($\phi$) is the number of\\particles passing by a location\\per-area, per time.", font_size=font_size).shift(RIGHT * 3.5 + UP)
        self.play(Write(fluxdef))
        self.wait()

        Qdef = Tex(r"$Q =$ Rate of particle emission", font_size=font_size).next_to(fluxdef, DOWN).shift(DOWN * 0.5)

        fluxform = Tex(r"$\phi(r)=\frac{Q}{4\pi r^2}$").next_to(Qdef, DOWN).shift(DOWN * 0.5)
        self.play(Write(Qdef), Write(fluxform))
        self.wait()

        circ1 = DashedVMobject(Circle(radius=1.25).shift(LEFT * 3.5), num_dashes=30)
        circ2 = DashedVMobject(Circle(radius=1.75).shift(LEFT * 3.5).set_stroke(opacity=0.6), num_dashes=14)
        circ3 = DashedVMobject(Circle(radius=2.25).shift(LEFT * 3.5).set_stroke(opacity=0.3), num_dashes=8)
        self.play(Create(circ1))
        self.play(Create(circ2))
        self.play(Create(circ3))
        self.wait()

        material = Circle(radius=2.8).shift(LEFT * 3.5).set_fill(color=BLUE, opacity=0.2).set_stroke(opacity=0).set_z_index(-1)
        self.play(
            Create(material),
            Transform(
                fluxform,
                Tex(r"$\phi(r)=\frac{Q}{4\pi r^2}e^{-\Sigma r}$").next_to(Qdef, DOWN).shift(DOWN * 0.5)
            ),
            Transform(
                title,
                Tex(r"\underline{Geometric \& material attentuation}", font_size=font_size).to_edge(UP).shift(UP * spacer)
            )
        )
        self.wait()

        self.play(
            fluxdef.animate.shift(UP),
            Qdef.animate.shift(UP * 1.5),
            fluxform.animate.shift(UP * 2),
        )
        fluencedef = Tex(r"Fluence ($\Phi$) is the total number of\\particles passing by a location\\ during some time interval, per-area.", font_size=font_size).shift(RIGHT * 3.5 + DOWN * 1.5)
        fluenceform = Tex(r"$\Phi=\int_{t_1}^{t_2}\phi(t)dt$", font_size=font_size).next_to(fluencedef, DOWN)
        self.play(Write(fluencedef), Write(fluenceform))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class HydrogenXS(Scene):
    def construct(self):
        font_size = 40
        spacer = 0.2
        title = Tex(r"\underline{Hydrogen-1 scattering cross section}", font_size=font_size).to_edge(UP).shift(UP * spacer)
        self.play(Write(title))
        self.wait()

        h1 = Isotope(element="H", mass_number=1)
        h1xs = h1.get_xs(incident_particle="n", cross_section="elastic_scatter")

        linax = Axes(
            x_range=[1e-5, 2e7, 5e6],
            y_range=[1e-4, 1.4e3, 200],
            tips=False,
            axis_config={"include_numbers": True}
        ).scale(0.9)
        linax_x_label = linax.get_x_axis_label(Tex(r"Energy (eV)", font_size=40), edge=DOWN, direction=DOWN)
        linax_y_label = linax.get_y_axis_label(Tex(r"$\sigma_s$ (b)", font_size=40), edge=LEFT, direction=LEFT).rotate(90 * DEGREES).to_edge(LEFT).shift(LEFT * 0.3)
        linax_xs_curve = linax.plot_line_graph(
            x_values = h1xs["energy"].m_as("eV"),
            y_values = h1xs["xs"].m_as("barn"),
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=4,
        )
        self.play(Create(linax), Write(linax_x_label), Write(linax_y_label))
        self.wait()
        self.play(Create(linax_xs_curve).set_run_time(3))
        linear_plot = VGroup(linax, linax_xs_curve, linax_x_label, linax_y_label)

        semilogx_ax = Axes(
            x_range=[-5, 7.3, 1],
            y_range=[1e-4, 1.4e3, 200],
            tips=False,
            axis_config={"include_numbers": True},
            x_axis_config={"scaling": LogBase()}
        ).scale(0.9)
        semilogx_ax_x_label = semilogx_ax.get_x_axis_label(Tex(r"Energy (eV)", font_size=40), edge=DOWN, direction=DOWN)
        semilogx_ax_y_label = semilogx_ax.get_y_axis_label(Tex(r"$\sigma_s$ (b)", font_size=40), edge=LEFT, direction=LEFT).rotate(90 * DEGREES).to_edge(LEFT).shift(LEFT * 0.3)
        semilogx_curve = semilogx_ax.plot_line_graph(
            x_values = h1xs["energy"].m_as("eV"),
            y_values = h1xs["xs"].m_as("barn"),
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=4,
        )
        semilogx_plot = VGroup(semilogx_ax, semilogx_curve, semilogx_ax_x_label, semilogx_ax_y_label)
        self.play(Transform(linear_plot, semilogx_plot, run_time=3))
        self.wait()

        thermal_slab = VGroup(
            DashedLine(start=semilogx_ax.c2p(0.4, 1400, 0), end=semilogx_ax.c2p(0.4, 0, 0)),
            Polygon(
                *[semilogx_ax.c2p(1e-5, 1400, 0), semilogx_ax.c2p(1e-5, 0, 0), semilogx_ax.c2p(0.4, 0, 0), semilogx_ax.c2p(0.4, 1400, 0)]
            ).set_fill(color=BLUE, opacity=0.2).set_stroke(opacity=0),
            Tex(r"$\frac{1}{v}$", font_size=45).set_x(semilogx_ax.x_axis.n2p(0.003)[0]).set_y(semilogx_ax.y_axis.n2p(1000)[1])
        )
        thermal_label = Tex("Thermal", font_size=45).align_to(thermal_slab, UP).set_x(thermal_slab.get_x()).shift(DOWN * 0.5)
        self.play(Create(thermal_slab[0]), FadeIn(thermal_slab[1]))
        self.wait()
        self.play(Write(thermal_label))
        self.wait()
        self.play(Write(thermal_slab[2]))
        self.wait()

        ax = Axes(
            x_range=[-5, 7.3, 1],
            y_range=[-1, 4, 2],
            tips=False,
            axis_config={"include_numbers": True},
            x_axis_config={"scaling": LogBase()},
            y_axis_config={"scaling": LogBase()}
        ).scale(0.9)
        ax_x_label = ax.get_x_axis_label(Tex(r"Energy (eV)", font_size=40), edge=DOWN, direction=DOWN)
        ax_y_label = ax.get_y_axis_label(Tex(r"$\sigma_s$ (b)", font_size=40), edge=LEFT, direction=LEFT).rotate(90 * DEGREES).to_edge(LEFT).shift(LEFT * 0.3)
        xs_curve = ax.plot_line_graph(
            x_values = h1xs["energy"].m_as("eV"),
            y_values = h1xs["xs"].m_as("barn"),
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=4,
        )
        loglog_plot = VGroup(ax, xs_curve, ax_x_label, ax_y_label)
        self.play(Transform(linear_plot, loglog_plot, run_time=3))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class UraniumXS(Scene):
    def construct(self):
        def sparkle_at(location, n_sparkles=20, radius=0.2):
            # Create a VGroup to hold all the sparkles
            sparkles = VGroup()

            # Create individual sparkles as small lines
            for val in range(n_sparkles):
                angle = 2 * PI * (val / n_sparkles) + random.random()
                direction = np.array([np.cos(angle), np.sin(angle), 0])
                start_point = location
                end_point = location + direction * radius

                line = Line(start_point, end_point, stroke_width=2, color=YELLOW)
                sparkles.add(line)
            return sparkles

        font_size = 40
        spacer = 0.2
        title = Tex(r"\underline{Uranium-238 fission cross section}", font_size=font_size).to_edge(UP).shift(UP * spacer)
        self.play(Write(title))
        self.wait()

        u235xs = Isotope(element="U", mass_number=235).get_xs(incident_particle="n", cross_section="fission")
        u238xs = Isotope(element="U", mass_number=238).get_xs(incident_particle="n", cross_section="fission")

        ax = Axes(
            x_range=[-5, 7.5, 1],
            y_range=[-8, 2, 2],
            tips=False,
            axis_config={"include_numbers": True},
            x_axis_config={"scaling": LogBase()},
            y_axis_config={"scaling": LogBase()}
        ).scale(0.9)
        ax_x_label = ax.get_x_axis_label(Tex(r"Energy (eV)", font_size=40), edge=DOWN, direction=DOWN)
        ax_y_label = ax.get_y_axis_label(Tex(r"$\sigma_f$ (b)", font_size=40), edge=LEFT, direction=LEFT).rotate(90 * DEGREES).to_edge(LEFT).shift(LEFT * 0.3)
        xs_curve = ax.plot_line_graph(
            x_values = u238xs["energy"].m_as("eV"),
            y_values = u238xs["xs"].m_as("barn"),
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=4,
        )
        self.play(Create(ax), Write(ax_x_label), Write(ax_y_label))
        self.wait()
        self.play(Create(xs_curve).set_run_time(3))
        self.wait()
        plot1 = VGroup(ax, xs_curve, ax_x_label, ax_y_label)

        thermal_slab = VGroup(
            DashedLine(start=ax.c2p(0.4, 50, 0), end=ax.c2p(0.4, 1e-8, 0)),
            Polygon(
                *[ax.c2p(1e-5, 50, 0), ax.c2p(1e-5, 1e-8, 0), ax.c2p(0.4, 1e-8, 0), ax.c2p(0.4, 50, 0)]
            ).set_fill(color=BLUE, opacity=0.2).set_stroke(opacity=0)
        )
        thermal_label = Tex("Thermal", font_size=45).align_to(thermal_slab, UP).set_x(thermal_slab.get_x()).shift(DOWN * 0.25)
        self.play(Create(thermal_slab[0]), FadeIn(thermal_slab[1]), Write(thermal_label))
        self.wait()

        res_slab = VGroup(
            DashedLine(start=ax.c2p(1e6, 50, 0), end=ax.c2p(1e6, 1e-8, 0)),
            Polygon(
                *[ax.c2p(0.4, 50, 0), ax.c2p(0.4, 1e-8, 0), ax.c2p(1e6, 1e-8, 0), ax.c2p(1e6, 50, 0)]
            ).set_fill(color=RED, opacity=0.2).set_stroke(opacity=0)
        )
        res_label = Tex("Resonance region", font_size=45).align_to(res_slab, UP).set_x(res_slab.get_x()).shift(DOWN * 0.25)
        self.play(Create(res_slab[0]), FadeIn(res_slab[1]), Write(res_label))
        self.wait()

        sparkle_positions = [
            ax.c2p(6.3, 0.0015, 0),
            ax.c2p(20.6, 0.015, 0),
            ax.c2p(66, 0.005, 0),
            ax.c2p(725, 0.100, 0),
            ax.c2p(15000, 0.01, 0)
        ]
        sparkle_animations = []
        for pos in sparkle_positions:
            sparkle = sparkle_at(pos)
            sparkle_animations.append(
                AnimationGroup(
                    Create(sparkle).set_rate_func(rate_functions.rush_into),
                    sparkle.animate.scale(1.5),
                    sparkle.animate.set_opacity(0).set_rate_func(rate_functions.exponential_decay),
                    lag_ratio=0.3,
                    run_time=2.5
                )
            )
        sparkle_animations = AnimationGroup(*sparkle_animations, lag_ratio=0.1)
        self.play(sparkle_animations)
        self.wait()

        fast_slab = VGroup(
            DashedLine(start=ax.c2p(3e7, 50, 0), end=ax.c2p(3e7, 1e-8, 0)),
            Polygon(
                *[ax.c2p(1e6, 50, 0), ax.c2p(1e6, 1e-8, 0), ax.c2p(3e7, 1e-8, 0), ax.c2p(3e7, 50, 0)]
            ).set_fill(color=GREEN, opacity=0.2).set_stroke(opacity=0)
        )
        fast_label = Tex(r"Fast!", font_size=45).align_to(fast_slab, UP).set_x(fast_slab.get_x()).shift(DOWN * 0.25)
        self.play(Create(fast_slab[0]), FadeIn(fast_slab[1]), Write(fast_label))
        self.wait()

        ax2 = Axes(
            x_range=[-5, 7.5, 1],
            y_range=[-8, 7, 2],
            tips=False,
            axis_config={"include_numbers": True},
            x_axis_config={"scaling": LogBase()},
            y_axis_config={"scaling": LogBase()}
        ).scale(0.9)
        ax2_x_label = ax2.get_x_axis_label(Tex(r"Energy (eV)", font_size=40), edge=DOWN, direction=DOWN)
        ax2_y_label = ax2.get_y_axis_label(Tex(r"$\sigma_f$ (b)", font_size=40), edge=LEFT, direction=LEFT).rotate(90 * DEGREES).to_edge(LEFT).shift(LEFT * 0.3)
        xs_curve1 = ax2.plot_line_graph(
            x_values = u238xs["energy"].m_as("eV"),
            y_values = u238xs["xs"].m_as("barn"),
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=4,
        )
        xs_curve2 = ax2.plot_line_graph(
            x_values = u235xs["energy"].m_as("eV"),
            y_values = u235xs["xs"].m_as("barn"),
            line_color=BLUE,
            add_vertex_dots=False,
            stroke_width=4,
        )
        plot2 = VGroup(ax2, xs_curve1, ax2_x_label, ax2_y_label)
        self.play(Transform(title, Tex(r"\underline{Uranium fission cross sections}", font_size=font_size).to_edge(UP).shift(UP * spacer)))
        self.play(Transform(plot1, plot2, run_time=3))

        u238_label = Tex("U-238", color=YELLOW).move_to(ax2.c2p(1e-3, 5e-3, 0))
        u235_label = Tex("U-235", color=BLUE).move_to(ax2.c2p(1e-3, 1e2, 0))
        self.play(Write(u238_label))
        self.wait()
        self.play(Create(xs_curve2).set_run_time(3))
        self.wait()
        self.play(Write(u235_label))
        self.wait()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
