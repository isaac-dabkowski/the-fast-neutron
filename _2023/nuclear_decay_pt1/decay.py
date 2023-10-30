from manim import *

import mendeleev
import numpy as np
from pint import Q_

from resources import Isotope, AlphaParticle, BetaPlusParticle, BetaMinusParticle, GammaParticle, NeutrinoParticle, AntiNeutrinoParticle, AlphaDecay, BetaMinusDecay, BetaPlusDecay, GammaDecay


def calc_beta_decay_energy_dist(beta_type):
    def calc_F(T, Z, mp):
        mec2 = 0.511
        alpha = 1 / 137
        x = mp * (Z + mp) * alpha * (1 + T / mec2) / np.sqrt(T / mec2 * (2 + T / mec2))
        return 2 * np.pi * x / (1 - np.exp(-2 * np.pi * x))

    Q = 1
    Z = 30
    mec2 = 0.511

    if beta_type == "plus":
        mp = -1
    elif beta_type == "minus":
        mp = 1

    energy = np.linspace(0.000001, Q, 100)
    p = list()
    for T in energy:
        p.append(
            np.sqrt(T ** 2 + 2 * mec2 * T) * (Q - T) ** 2 * (T + mec2) * calc_F(T, Z, mp)
        )
    # Normalization constant
    C = 1 / np.trapz(x=energy, y=p)
    p = [C * p_val for p_val in p]
    return energy, p


class DecayTitleCard(Scene):
    def construct(self):
        section_title = Tex("Radioactive decay")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class DecayAnimation(Scene):
    def construct(self):
        tex = Tex(r"Unstable nuclei shed their excess energy\\by releasing energetic particle(s)")
        self.play(Write(tex))
        self.wait()

        # Alpha
        po210 = Isotope(element="Po", mass_number=210, fill_color="#197d21")
        po210_s = po210.sprite.copy().scale(0.8).shift(DOWN * 2.5 + RIGHT * 2)
        alpha = AlphaParticle()

        alpha_decay = AlphaDecay(parent=po210)
        pb206_s = alpha_decay.daughter.sprite.copy().scale(0.77).set_y(po210_s.get_y()).set_x(po210_s.get_x())
        pb206_s[0].set_fill_color("#424242")

        alpha_s = alpha.sprite.copy().set_y(po210_s.get_y()).set_x(po210_s.get_x())
        self.play(GrowFromCenter(po210_s))
        self.wait(0.6)
        self.play(
            GrowFromCenter(alpha_s),
            alpha_s.animate.shift(RIGHT * 2.5),
            ReplacementTransform(po210_s, pb206_s),
            run_time=0.75
        )

        # Beta -
        c14 = Isotope(element="C", mass_number=14, fill_color="#05446e")
        c14_s = c14.sprite.copy().scale(0.6).shift(UP * 2.25 + RIGHT * 2)
        betam = BetaMinusParticle()
        antineu = AntiNeutrinoParticle()

        beta_minus_decay = BetaMinusDecay(parent=c14)
        n14_s = beta_minus_decay.daughter.sprite.copy().scale(0.6).set_y(c14_s.get_y()).set_x(c14_s.get_x())
        n14_s[0].set_fill_color("#1b755a")

        betam_s = betam.sprite.copy().set_y(c14_s.get_y()).set_x(c14_s.get_x())
        antineu_s = antineu.sprite.copy().set_y(c14_s.get_y()).set_x(c14_s.get_x())
        self.play(GrowFromCenter(c14_s))
        self.wait(0.6)
        self.play(
            GrowFromCenter(betam_s),
            betam_s.animate.shift(RIGHT * 2.5 + UP),
            GrowFromCenter(antineu_s),
            antineu_s.animate.shift(RIGHT * 2.5 + DOWN),
            ReplacementTransform(c14_s, n14_s),
            run_time=0.75
        )

        # Beta +
        mg23 = Isotope(element="Mg", mass_number=23, fill_color="#753c1b")
        mg23_s = mg23.sprite.copy().scale(0.6).shift(UP * 2.25 + LEFT * 2)
        betap = BetaPlusParticle()
        neu = NeutrinoParticle()

        beta_plus_decay = BetaPlusDecay(parent=mg23)
        na23_s = beta_plus_decay.daughter.sprite.copy().scale(
            0.6).set_y(mg23_s.get_y()).set_x(mg23_s.get_x())
        na23_s[0].set_fill_color("#2f2445")

        betap_s = betap.sprite.copy().set_y(mg23_s.get_y()).set_x(mg23_s.get_x())
        neu_s = neu.sprite.copy().set_y(mg23_s.get_y()).set_x(mg23_s.get_x())
        self.play(GrowFromCenter(mg23_s))
        self.wait(0.6)
        self.play(
            GrowFromCenter(betap_s),
            betap_s.animate.shift(LEFT * 2.5 + DOWN),
            GrowFromCenter(neu_s),
            neu_s.animate.shift(LEFT * 2.5 + UP),
            ReplacementTransform(mg23_s, na23_s),
            run_time=0.75
        )

        # Gamma
        pu240 = Isotope(element="Pu", mass_number=240, fill_color="#334727", excited=True)
        pu240_s = pu240.sprite.copy().scale(0.8).shift(DOWN * 2.5 + LEFT * 2)
        gamma = GammaParticle()

        gamma_decay = GammaDecay(parent=pu240, excitation_energy=Q_(1, "MeV"))
        pu240_s2 = gamma_decay.daughter.sprite.copy().scale(0.77).set_y(pu240_s.get_y()).set_x(pu240_s.get_x())
        pu240_s2[0].set_fill_color("#1f2b17").set_stroke_color("#757474")

        gamma_s = gamma.sprite.copy().set_y(pu240_s.get_y()).set_x(pu240_s.get_x())
        self.play(GrowFromCenter(pu240_s))
        self.wait(0.6)
        self.play(
            GrowFromCenter(gamma_s),
            gamma_s.animate.shift(LEFT * 2.5),
            ReplacementTransform(pu240_s, pu240_s2),
            run_time=0.75
        )
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()



class AlphaDecayAnimation(Scene):
    def construct(self):
        # Primer
        title = Tex(r"\underline{Alpha decay}").to_edge(UP).shift(DOWN * 0.5)
        tex1 = Tex(r"An unstable nucleus releases an alpha particle").next_to(title, DOWN)
        tex2 = Tex(r"An alpha particle is just a $^4$He nucleus").next_to(tex1, DOWN)
        tex3 = Tex(r"$^A_ZX \rightarrow ^{A-4}_{A-2}Y + \alpha$").next_to(tex2, DOWN)
        self.play(Write(title))
        self.wait()
        self.play(Write(tex1))
        self.wait()
        self.play(Write(tex2))
        self.wait()
        self.play(Write(tex3))
        self.wait()
        self.play(FadeOut(tex1), FadeOut(tex2), tex3.animate.set_y((tex1.get_y() + tex2.get_y()) / 2))
        self.wait()
        tex4 = Tex(r"$Q = -\Delta M c^2$").next_to(tex3, DOWN * 1.5)
        tex5 = Tex(r"$Q = \left[M\left(^{210}_{84}\text{Po}\right) - M\left(^{206}_{82}\text{Pb}\right) - M\left(^{4}_{2}\text{He}\right)\right] c^2$").next_to(tex4, DOWN * 1.5)
        self.play(Write(tex4))
        self.wait()
        self.play(Transform(tex4, Tex(r"$Q = \left[M\left(^A_ZX\right) - M\left(^{A-4}_{A-2}Y\right) - M\left(^{4}_{2}He\right)\right] c^2$").next_to(tex3, DOWN * 1.5)))
        self.wait()

        # Alpha animation
        po210 = Isotope(element="Po", mass_number=210, fill_color="#197d21")
        po210_s = po210.sprite.copy().scale(0.8).shift(DOWN * 2.5)
        po210_s_copy = po210_s.copy()
        alpha = AlphaParticle()

        alpha_decay = AlphaDecay(parent=po210)
        pb206_s = alpha_decay.daughter.sprite.copy().scale(0.77).set_y(po210_s.get_y())
        pb206_s[0].set_fill_color("#424242")

        alpha_s = alpha.sprite.copy().set_y(po210_s.get_y())
        self.play(GrowFromCenter(po210_s))
        self.wait()
        self.play(
            GrowFromCenter(alpha_s),
            alpha_s.animate.set_x(3.5),
            ReplacementTransform(po210_s, pb206_s),
            run_time=0.75
        )
        self.wait()
        po210_s_copy.set_x(-4.0)
        arrow = Arrow(start=[-2.75, -2.5, 0], end=[-1.25, -2.5, 0], buff=0.0)
        plus = Tex("+").move_to([(pb206_s.get_x() + alpha_s.get_x()) / 1.8, pb206_s.get_y(), 0])
        self.play(GrowFromCenter(po210_s_copy), Create(arrow), Create(plus))
        decay_diagram = VGroup(po210_s_copy, pb206_s, arrow, plus, alpha_s)
        self.wait()

        # Solve for Q
        self.play(Write(tex5))
        self.wait()
        po_mass = str(round(po210.mass.m, 4))
        pb_mass = str(round(alpha_decay.daughter.mass.m, 4))
        alpha_mass = str(round(alpha.mass.m, 4))
        q_val = str(round(alpha_decay.Q.m_as("MeV"), 4))
        self.play(Transform(tex5, Tex(rf"$Q = \left[{po_mass}\text{{ u}} - {pb_mass}\text{{ u}} - {alpha_mass}\text{{ u}}\right] c^2$").next_to(tex4, DOWN * 1.5)))
        self.wait()
        self.play(Transform(tex5, Tex(rf"$Q = \text{{+}}{q_val}\text{{ MeV}}$").next_to(tex4, DOWN * 1.5)))
        self.wait()

        # Do conservation of energy/momentum
        self.play(
            FadeOut(decay_diagram),
            FadeOut(tex4),
            FadeOut(tex5),
            tex3.animate.shift(UP * 0.3)
        )
        cons_eng = Tex(r"$Q = \text{KE}_\text{Y} + \text{KE}_\alpha = \frac{1}{2}m_\text{Y}v_\text{Y}^2 + \frac{1}{2}m_\alpha v_\alpha^2$").next_to(tex3, DOWN * 1.5)
        cons_mom = Tex(r"$m_\text{Y} v_\text{Y} = m_\alpha v_\alpha$").next_to(cons_eng, DOWN * 1.5)
        self.play(Write(cons_eng))
        self.wait()
        self.play(Write(cons_mom))
        self.wait()
        self.play(FadeOut(cons_eng), FadeOut(cons_mom))
        self.wait()
        ke_relations = VGroup(
            Tex(r"$\text{KE}_\text{Y}=\left[\frac{m_\alpha}{m_\text{Y} + m_\alpha}\right]Q$"),
            Tex(r"$\text{KE}_\alpha=\left[\frac{m_\text{Y}}{m_\text{Y} + m_\alpha}\right]Q$")
        ).arrange(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(ke_relations[0]), Write(ke_relations[1]))
        self.wait()
        self.play(FadeIn(decay_diagram))
        self.wait()
        daughter_eng = str(round(alpha_decay.daughter_energy.m_as("MeV"), 4))
        alpha_eng = str(round(alpha_decay.alpha_energy.m_as("MeV"), 4))
        ke_results = VGroup(
            Tex(rf"$\text{{KE}}_\text{{Y}}={daughter_eng}\text{{ MeV}}$"),
            Tex(rf"$\text{{KE}}_\alpha={alpha_eng}\text{{ MeV}}$")
        ).arrange(DOWN, buff=MED_LARGE_BUFF)
        self.play(
            Transform(ke_relations[0], ke_results[0].copy()),
            Transform(ke_relations[1], ke_results[1].copy())
        )
        self.wait()
        self.play(FadeOut(ke_relations), FadeOut(tex3))
        self.wait()

        # Discussion on alpha particles
        tex10 = Tex(r"Alphas carry a lot of energy, but have a very short range").next_to(title, DOWN * 3.5)
        tex11 = Tex(r"Alpha emitters are not dangerous - unless ingested").next_to(tex10, DOWN * 3.5)
        self.play(Write(tex10))
        self.wait()
        self.play(Write(tex11))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class BetaDecayAnimation(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mhchem}")
        # Primer
        title = Tex(r"\underline{Beta decay}").to_edge(UP).shift(DOWN * 0.5)
        tex1 = Tex(r"An unstable nucleus releases a beta particle").next_to(title, DOWN)
        tex2 = Tex(r"Beta decay comes in two forms, $\beta^+$ and $\beta^-$").next_to(tex1, DOWN)
        self.play(Write(title))
        self.wait()
        self.play(Write(tex1))
        self.wait()
        self.play(Write(tex2))
        self.wait()
        self.play(
            Transform(title, Tex(r"\underline{Beta minus decay}").to_edge(UP).shift(DOWN * 0.5)),
            Transform(tex1, Tex(r"An unstable nucleus releases a beta-minus particle").next_to(title, DOWN)),
            FadeOut(tex2)
        )
        self.wait()
        tex3 = Tex(r"$^A_ZX \rightarrow \ce{ ^{A}_{Z+1}Y } + e^- + \bar{\nu}_e$", tex_template=myTemplate).next_to(tex1, DOWN)
        self.play(Write(tex3))
        self.wait()

        # Animation
        c14 = Isotope(element="C", mass_number=14, fill_color="#05446e")
        c14_s = c14.sprite.copy().scale(0.6).shift(DOWN * 2.25)
        c14_s_copy = c14_s.copy()
        betam = BetaMinusParticle()
        antineu = AntiNeutrinoParticle()

        beta_minus_decay = BetaMinusDecay(parent=c14)
        n14_s = beta_minus_decay.daughter.sprite.copy().scale(
            0.6).set_y(c14_s.get_y()).set_x(c14_s.get_x())
        n14_s[0].set_fill_color("#1b755a")

        betam_s = betam.sprite.copy().set_y(c14_s.get_y()).set_x(c14_s.get_x())
        antineu_s = antineu.sprite.copy().set_y(c14_s.get_y()).set_x(c14_s.get_x())
        self.play(GrowFromCenter(c14_s))
        self.wait()
        self.play(
            GrowFromCenter(betam_s),
            betam_s.animate.shift(RIGHT * 2.5 + UP),
            GrowFromCenter(antineu_s),
            antineu_s.animate.shift(RIGHT * 2.5 + DOWN),
            ReplacementTransform(c14_s, n14_s),
            run_time=0.75
        )
        self.wait()
        c14_s_copy.set_x(-4.0)
        arrow = Arrow(start=[-2.75, n14_s.get_y(), 0], end=[-1.25, n14_s.get_y(), 0], buff=0.0)
        plus = Tex("+").move_to([(n14_s.get_x() + betam_s.get_x()) / 1.8, n14_s.get_y(), 0])
        plus2 = Tex("+").move_to([betam_s.get_x() + 1.3, n14_s.get_y(), 0])
        self.play(GrowFromCenter(c14_s_copy), Create(arrow),  Create(plus), betam_s.animate.shift(DOWN), Create(plus2), antineu_s.animate.shift(UP + RIGHT * 2.5))
        decay_diagram = VGroup(c14_s_copy, arrow, n14_s, plus, betam_s, plus2, antineu_s)
        self.wait()

        c_mass = str(round(c14.mass.m, 4))
        n_mass = str(round(beta_minus_decay.daughter.mass.m, 4))
        q_val = str(round(beta_minus_decay.Q.m_as("keV"), 4))
        tex4 = Tex(rf"$Q = \left[M\left(^{{14}}\text{{C}}\right) - M\left(^{{14}}\text{{N}}\right) - M\left(\bar{{\nu}}_{{e}}\right)\right] c^2$").next_to(tex3, DOWN * 1.5)
        self.play(Write(tex4))
        self.wait()
        self.play(Transform(tex4, Tex(rf"$Q = \left[{c_mass}\text{{ u}} - {n_mass}\text{{ u}} -  M\left(\bar{{\nu}}_{{e}}\right)\right] c^2$").next_to(tex3, DOWN * 1.5)))
        self.wait()
        self.play(Transform(tex4, Tex(rf"$Q = \left[{c_mass}\text{{ u}} - {n_mass}\text{{ u}}\right] c^2$").next_to(tex3, DOWN * 1.5)))
        self.wait()
        self.play(Transform(tex4, Tex(rf"$Q = \text{{+}}{q_val}\text{{ keV}}$").next_to(tex3, DOWN * 1.5)))
        self.wait()

        # Beta plus time
        self.play(
            FadeOut(decay_diagram),
            FadeOut(tex4),
            FadeOut(tex3)
        )
        self.wait()
        self.play(
            Transform(title, Tex(r"\underline{Beta plus decay}").to_edge(UP).shift(DOWN * 0.5)),
            Transform(tex1, Tex(r"An unstable nucleus releases a beta-plus particle").next_to(title, DOWN))
        )
        self.wait()
        tex3 = Tex(r"$^A_ZX \rightarrow \ce{ ^{A}_{Z-1}Y } + e^+ + \nu_e$", tex_template=myTemplate).next_to(tex1, DOWN)
        self.play(Write(tex3))
        self.wait()

        # Beta + animation
        mg23 = Isotope(element="Mg", mass_number=23, fill_color="#753c1b")
        mg23_s = mg23.sprite.copy().scale(0.6).shift(DOWN * 2.25)
        mg23_s_copy = mg23_s.copy()
        betap = BetaPlusParticle()
        neu = NeutrinoParticle()

        beta_plus_decay = BetaPlusDecay(parent=mg23)
        na23_s = beta_plus_decay.daughter.sprite.copy().scale(0.6).set_y(mg23_s.get_y()).set_x(mg23_s.get_x())
        na23_s[0].set_fill_color("#2f2445")

        betap_s = betap.sprite.copy().set_y(mg23_s.get_y()).set_x(mg23_s.get_x())
        neu_s = neu.sprite.copy().set_y(mg23_s.get_y()).set_x(mg23_s.get_x())
        self.play(GrowFromCenter(mg23_s))
        self.wait()
        self.play(
            GrowFromCenter(betap_s),
            betap_s.animate.shift(RIGHT * 2.5 + UP),
            GrowFromCenter(neu_s),
            neu_s.animate.shift(RIGHT * 2.5 + DOWN),
            ReplacementTransform(mg23_s, na23_s),
            run_time=0.75
        )
        self.wait()
        mg23_s_copy.set_x(-4.0)
        arrow = Arrow(start=[-2.75, na23_s.get_y(), 0], end=[-1.25, na23_s.get_y(), 0], buff=0.0)
        plus = Tex("+").move_to([(na23_s.get_x() + betap_s.get_x()) / 1.8, na23_s.get_y(), 0])
        plus2 = Tex("+").move_to([betam_s.get_x() + 1.3, na23_s.get_y(), 0])
        self.play(GrowFromCenter(mg23_s_copy), Create(arrow),  Create(plus), betap_s.animate.shift(DOWN), Create(plus2), neu_s.animate.shift(UP + RIGHT * 2.5))
        decay_diagram = VGroup(mg23_s_copy, arrow, na23_s, plus, betap_s, plus2, neu_s)
        self.wait()

        mg_mass = str(round(mg23.mass.m, 4))
        na_mass = str(round(beta_minus_decay.daughter.mass.m, 4))
        betap_mass = str(round(betap.mass.m, 4))
        q_val = str(round(beta_plus_decay.Q.m_as("MeV"), 4))
        tex4 = Tex(rf"$Q = \left[M\left(^{{23}}\text{{Mg}}\right) - M\left(^{{23}}\text{{Na}}\right) - 2M\left(e^{{+}}\right) - M\left(\nu_{{e}}\right)\right] c^2$").next_to(tex3, DOWN * 1.5)
        self.play(Write(tex4))
        self.wait()
        self.play(Transform(tex4, Tex(rf"$Q = \left[{mg_mass}\text{{ u}} - {na_mass}\text{{ u}} - 2\cdot{betap_mass}\text{{ u}} - M\left(\nu_{{e}}\right)\right] c^2$").next_to(tex3, DOWN * 1.5)))
        self.wait()
        self.play(Transform(tex4, Tex(rf"$Q = \left[{mg_mass}\text{{ u}} - {na_mass}\text{{ u}} - 2\cdot{betap_mass}\text{{ u}}\right] c^2$").next_to(tex3, DOWN * 1.5)))
        self.wait()
        self.play(Transform(tex4, Tex(rf"$Q = \text{{+}}{q_val}\text{{ MeV}}$").next_to(tex3, DOWN * 1.5)))
        self.wait()
        self.play(
            FadeOut(decay_diagram),
            FadeOut(tex4),
            FadeOut(tex3),
            FadeOut(tex1)
        )
        self.wait()

        # Energy distribution
        self.play(Transform(title, Tex(r"\underline{Beta decay energy distribution}").to_edge(UP).shift(DOWN * 0.5)))
        self.wait()
        tex1 = Tex(r"We can't say exactly how much energy the beta particle gets").next_to(title, DOWN)
        tex2 = Tex(r"We can only get a probability distribution for its energy").next_to(tex1, DOWN)
        tex3 = Tex(r"$p\left(T_e\right)=C\sqrt{T_e^2+2T_em_ec^2}\left(Q-T_e\right)^2\left(T_e+m_ec^2\right)\cdot F\left(Z,T_e\right)$").next_to(tex2, DOWN * 3)
        tex4 = Tex(r"$C=\text{Normalization constant}$").next_to(tex3, DOWN * 3)
        fermi = Tex(r"$F\left(Z,T_e\right)=\text{Non-relativistic Fermi function}$").next_to(tex4, DOWN)
        self.play(Write(tex1))
        self.wait()
        self.play(Write(tex2))
        self.wait()
        self.play(Write(tex3))
        self.wait()
        self.play(Write(tex4))
        self.wait()
        self.play(Write(fermi))
        self.wait()
        self.play(
            FadeOut(tex1),
            FadeOut(tex2),
            FadeOut(tex4),
            tex3.animate.next_to(title, DOWN),
            fermi.animate.shift(UP * 2.25)
        )
        self.wait()

        # Fermi function section
        self.play(
            Transform(fermi, Tex(r"$F\left(Z,T_e\right)=\frac{2\pi x}{1 - e^{-2\pi x}}$").move_to(fermi.get_center()))
        )
        x_def = Tex(r"$x=\mp Z \frac{e^2}{4\pi \epsilon_0 \hbar c}\frac{1}{\beta}$").next_to(fermi, DOWN)
        self.play(Write(x_def))
        self.wait()
        mp = VGroup(
            Tex(r"$\mp \rightarrow - \text{ if }\beta^+$"),
            Tex(r"$\mp \rightarrow + \text{ if }\beta^-$")
        ).arrange(DOWN, buff=MED_LARGE_BUFF).next_to(x_def, DOWN)
        self.play(Create(mp))
        self.wait()
        fermi_set = VGroup(
            fermi,
            x_def,
            mp
        )
        self.play(fermi_set.animate.shift(LEFT * 3.5))
        self.wait()
        alpha_tex = Tex(r"$\alpha=\frac{e^2}{4\pi \epsilon_0 \hbar c}$").shift(RIGHT * 3.5)
        self.play(Write(alpha_tex))
        self.wait()
        self.play(Transform(alpha_tex, Tex(r"$\alpha=\frac{e^2}{4\pi \epsilon_0 \hbar c}\approx \frac{1}{137}$").shift(RIGHT * 3.5)))
        self.wait()

        # Plot energy PDFs
        self.play(
            FadeOut(alpha_tex),
            fermi_set.animate.shift(RIGHT * 7.5)
        )
        self.wait()
        _, betam_pdf = calc_beta_decay_energy_dist(beta_type="minus")
        energy, betap_pdf = calc_beta_decay_energy_dist(beta_type="plus")
        ax = Axes(
            x_range=[0, 1.2, 1],
            y_range=[0, 1.2 * max([max(betam_pdf), max(betap_pdf)]), 1],
            tips=False,
            y_axis_config={"include_numbers": False, "include_ticks": False},
            x_axis_config={"include_numbers": False, "include_ticks": False},
            x_length=3.0,
            y_length=2.5,
        ).scale(1.75).shift(DOWN + LEFT * 2.75).set_stroke(width=3)
        ax_x_label = ax.get_x_axis_label(
            Tex("$T_e$", font_size=50), edge=DOWN, direction=DOWN, buff=0.3)
        ax_y_label = ax.get_y_axis_label(Tex("$p(T_e)$"), edge=LEFT, direction=LEFT, buff=0.3)
        bpp = ax.plot_line_graph(
            x_values=energy,
            y_values=betap_pdf,
            add_vertex_dots=False,
            stroke_width=3,
        )
        bmp = ax.plot_line_graph(
            x_values=energy,
            y_values=betam_pdf,
            add_vertex_dots=False,
            stroke_width=3,
            stroke_color=BLUE
        )
        self.play(
            FadeIn(ax),
            FadeIn(ax_x_label),
            FadeIn(ax_y_label)
        )
        self.wait()
        legend = VGroup(
            VGroup(
                Line(start=[-2, 1, 0], end=[-1, 1, 0], color=YELLOW),
                Tex(r"$\beta^+$")
            ).arrange(RIGHT),
            VGroup(
                Line(start=[-2, 0.25, 0], end=[-1, 0.25, 0], color=BLUE),
                Tex(r"$\beta^-$")
            ).arrange(RIGHT)
        ).arrange(DOWN).shift(LEFT * 0.75)
        self.play(FadeIn(legend))
        self.wait()
        self.play(Create(bpp), run_time=3)
        self.wait()
        self.play(Create(bmp), run_time=3)
        self.wait()
        pdf_grp = VGroup(
            ax,
            ax_x_label,
            ax_y_label,
            bpp,
            bmp,
            legend
        )
        self.wait()
        self.play(
            FadeOut(pdf_grp),
            FadeOut(fermi_set),
            FadeOut(tex3),
            Transform(title, Tex(r"\underline{Beta decay}").to_edge(UP).shift(DOWN * 0.5))
        )
        self.wait()

        # Discussion on beta particles
        tex10 = Tex(r"Betas, like alphas, do not take much to stop").next_to(title, DOWN * 3.5)
        tex11 = Tex(r"When shielding betas, we need to account for ``bremsstrahlung''").next_to(tex10, DOWN * 3.5)
        tex12 = Tex(r"Using low-Z shielding materials helps with bremsstrahlung").next_to(tex11, DOWN * 3.5)
        self.play(Write(tex10))
        self.wait()
        self.play(Write(tex11))
        self.wait()
        self.play(Write(tex12))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class GammaDecayAnimation(Scene):
    def construct(self):
        # Primer
        title = Tex(r"\underline{Gamma decay}").to_edge(UP).shift(DOWN * 0.5)
        tex1 = Tex(r"An unstable nucleus releases a gamma particle").next_to(title, DOWN)
        tex2 = Tex(r"Gamma decay acts on excited nuclei").next_to(tex1, DOWN)
        tex3 = Tex(r"Gamma decay does not transmute nuclei").next_to(tex2, DOWN)
        tex4 = Tex(r"$^A_ZX^* \rightarrow ^A_ZX+\gamma$").next_to(tex3, DOWN)
        self.play(Write(title))
        self.wait()
        self.play(Write(tex1))
        self.wait()
        self.play(Write(tex2))
        self.wait()
        self.play(Write(tex3))
        self.wait()
        self.play(Write(tex4))
        self.wait()

        # Animation
        pu240 = Isotope(element="Pu", mass_number=240, fill_color="#334727", excited=True)
        pu240_s = pu240.sprite.copy().scale(0.8).shift(DOWN * 2.5)
        gamma = GammaParticle()

        gamma_decay = GammaDecay(parent=pu240, excitation_energy=Q_(1, "MeV"))
        pu240_s2 = gamma_decay.daughter.sprite.copy().scale(0.77).set_y(pu240_s.get_y()).set_x(pu240_s.get_x())
        pu240_s2[0].set_fill_color("#1f2b17").set_stroke_color("#757474")

        gamma_s = gamma.sprite.copy().set_y(pu240_s.get_y()).set_x(pu240_s.get_x())
        self.play(GrowFromCenter(pu240_s))
        self.wait()
        self.play(
            GrowFromCenter(gamma_s),
            gamma_s.animate.shift(RIGHT * 2.5),
            ReplacementTransform(pu240_s, pu240_s2),
            run_time=0.75
        )
        self.play(
            FadeOut(tex1),
            FadeOut(tex2),
            FadeOut(tex3),
            tex4.animate.next_to(title, DOWN)
        )
        pu240_s = pu240.sprite.copy().scale(0.8).shift(DOWN * 2.5).set_x(-3)
        pu240.excited = True
        arrow = Arrow(start=[-1.75, pu240_s.get_y(), 0], end=[-0.25, pu240_s.get_y(), 0], buff=0.0)
        plus = Tex("+").move_to([(pu240_s2.get_x() + gamma_s.get_x()) / 1.8 + 1, gamma_s.get_y(), 0])
        self.play(GrowFromCenter(pu240_s), Create(arrow),  Create(plus), pu240_s2.animate.shift(RIGHT), gamma_s.animate.shift(RIGHT))
        decay_diagram = VGroup(pu240_s, arrow, pu240_s2, plus, gamma_s)
        self.wait()

        tex5 = Tex(r"$Q = \left[M\left(^A_Z\text{X}^*\right) - M\left(^A_Z\text{X}\right)\right] c^2$").next_to(tex4, DOWN * 2.5)
        self.play(Write(tex5))
        self.wait()
        self.play(Transform(tex5, Tex(r"$Q = \left[M\left(^A_Z\text{X}\right) + \frac{E^*}{c^2} - M\left(^A_Z\text{X}\right)\right] c^2$").next_to(tex4, DOWN * 2.5)))
        self.wait()
        self.play(Transform(tex5, Tex(r"$Q = \left[\frac{E^*}{c^2}\right] c^2$").next_to(tex4, DOWN * 2.5)))
        self.wait()
        self.play(Transform(tex5, Tex(r"$Q = E^*$").next_to(tex4, DOWN * 2.5)))
        self.wait()
        self.play(Transform(tex5, Tex(r"$Q = E^* \approx E_\gamma$").next_to(tex4, DOWN * 2.5)))
        self.wait()
        self.play(
            FadeOut(tex4),
            FadeOut(tex5),
            FadeOut(decay_diagram)
        )

        # Discussion on Gamma particles
        tex10 = Tex(r"Gammas are much more difficult to stop than alphas or betas").next_to(title, DOWN * 3.5)
        tex11 = Tex(r"High-Z materials perform best").next_to(tex10, DOWN * 3.5)
        self.play(Write(tex10))
        self.wait()
        self.play(Write(tex11))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class ChartOfNuclides(MovingCameraScene):
    def construct(self):
        ax = Axes(
            x_range=[0, 180, 30],
            y_range=[0, 120, 20],
            tips=False,
            y_axis_config={"include_numbers": True},
            x_axis_config={"include_numbers": True},
            x_length=11.0,
            y_length=7.333,
        ).shift(LEFT * 0.75 + UP * 0.3).scale(0.8)
        ax_x_label = ax.get_x_axis_label(Tex("Number of neutrons", font_size=50), edge=DOWN, direction=DOWN, buff=0.3)
        ax_y_label = ax.get_y_axis_label(Tex("Number of protons").rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.3)
        self.add_foreground_mobject(ax)
        self.play(FadeIn(ax), FadeIn(ax_x_label), FadeIn(ax_y_label))
        self.wait()


        # Get list of all nuclides and their stability/primary decay modes
        iso_data = dict()
        for i in range(1, 119):
            iso_data[i] = list()
            element = mendeleev.element(i)
            for idx, iso in enumerate(element.isotopes):
                # Deal with weird feature of mendeleev dataset where extremely exotic isotopes are labeled as stable
                # The the ratio of protons to neutrons is too exotic, do not allow the isotope to be labeled as stable.
                if iso.is_stable is True and (0.2 < (idx / len(element.isotopes)) < 0.75 or i < 3):
                    mode = "stable"
                else:
                    mode = max(iso.decay_modes, key=lambda x: 0.0 if x.intensity is None else x.intensity).mode
                    if mode == "3p" or mode == "2p":
                        mode = "p"
                    elif mode == "B+SF" or mode == "B+p" or mode == "EC":
                        mode = "B+"
                    elif mode == "2n":
                        mode = "n"
                    elif mode == "2B-":
                        mode = "B-"
                # Deal with weird feature of mendeleev dataset where extremely exotic isotopes are labeled as stable
                # if (idx / len(element.isotopes) < 0.2 or 1 - idx / len(element.isotopes) > 0.8) and 
                iso_data[i].append((iso.mass_number - iso.atomic_number, mode))

        # Put rectangles down for isotopes
        rect_width = ax.c2p(1,0,0)[0] - ax.c2p(0,0,0)[0]
        rect_height = ax.c2p(0,1,0)[1] - ax.c2p(0,0,0)[1]
        iso_sprites = VGroup()
        for Z in iso_data:
            for iso in iso_data[Z]:
                iso_rect = Rectangle(color=YELLOW, width=rect_width, height=rect_height, fill_color="#858585", stroke_width=0.2, fill_opacity=1.0)
                iso_rect.move_to(ax.c2p(iso[0], Z))
                iso_sprites.add(
                    iso_rect
                )
        self.play(Create(iso_sprites), run_time=3)
        self.wait()

        # Illustrate that elements are rows
        fe_line = DashedLine(start=ax.c2p(0, 26), end=ax.c2p(180, 26))
        fe_tex = Tex("Fe").next_to(fe_line.get_end(), RIGHT)
        self.play(Create(fe_line), Create(fe_tex))
        self.wait()
        u_line = DashedLine(start=ax.c2p(0, 92), end=ax.c2p(180, 92))
        u_tex = Tex("U").next_to(u_line.get_end(), RIGHT)
        self.play(Create(u_line), Create(u_tex))
        self.wait()
        self.play(
            FadeOut(fe_line),
            FadeOut(fe_tex),
            FadeOut(u_line),
            FadeOut(u_tex)
        )
        self.wait()

        # Legend
        legend = VGroup(
            VGroup(Rectangle(color=WHITE, width=0.2, height=0.2, stroke_width=1.5), Tex(r"= Stable", font_size=35)).arrange(RIGHT),
            VGroup(Rectangle(color=YELLOW, width=0.2, height=0.2, fill_color=YELLOW, fill_opacity=1.0), Tex(r"= $\alpha$", font_size=35)).arrange(RIGHT),
            VGroup(Rectangle(color=PINK, width=0.2, height=0.2, fill_color=PINK, fill_opacity=1.0), Tex(r"= $\beta^+$/EC", font_size=35)).arrange(RIGHT),
            VGroup(Rectangle(color=BLUE, width=0.2, height=0.2, fill_color=BLUE, fill_opacity=1.0), Tex(r"= $\beta^-$", font_size=35)).arrange(RIGHT),
            VGroup(Rectangle(color=ORANGE, width=0.2, height=0.2, fill_color=ORANGE, fill_opacity=1.0), Tex(r"= $p$", font_size=35)).arrange(RIGHT),
            VGroup(Rectangle(color=PURPLE, width=0.2, height=0.2, fill_color=PURPLE, fill_opacity=1.0), Tex(r"= $n$", font_size=35)).arrange(RIGHT),
            VGroup(Rectangle(color=GREEN, width=0.2, height=0.2, fill_color=GREEN, fill_opacity=1.0), Tex(r"= Fission", font_size=35)).arrange(RIGHT)
        ).arrange(DOWN, center=False, aligned_edge=LEFT, buff=MED_SMALL_BUFF).shift(RIGHT * 5 + UP * 2)

        # Stable isotopes
        self.play(
            FadeIn(legend[0][0]),
            Write(legend[0][1])
        )
        self.wait()
        stable_sprites = VGroup()
        for Z in iso_data:
            for iso in iso_data[Z]:
                if iso[1] == "stable":
                    iso_rect = Rectangle(color=WHITE, width=rect_width, height=rect_height, fill_color=BLACK, stroke_width=0.2, fill_opacity=1.0)
                    iso_rect.move_to(ax.c2p(iso[0], Z))
                    stable_sprites.add(
                        iso_rect
                    )
        self.play(Create(stable_sprites), run_time=3)
        self.wait()

        # Plot N=Z
        nz = ax.plot(
            lambda x : x,
            x_range = [0, 120],
            color=WHITE,
            stroke_width=2.0
        )
        nz_tex = Tex("$N=Z$").move_to(ax.c2p(80, 110))
        self.play(Create(nz), Write(nz_tex), run_time=2)
        self.add_foreground_mobject(nz)
        self.wait()
        self.play(
            self.camera.frame.animate.scale(0.25).move_to(ax.c2p(5, 5)),
            run_time=2
        )
        self.play(
            self.camera.frame.animate.move_to(ax.c2p(70, 50)),
            run_time=10
        )
        self.play(
            self.camera.frame.animate.scale(4.0).move_to([0, 0, 0]),
            run_time=2
        )
        self.wait()

        # Alpha
        self.play(
            FadeIn(legend[1][0]),
            Write(legend[1][1])
        )
        self.wait()
        alpha_sprites = VGroup()
        for Z in iso_data:
            for iso in iso_data[Z]:
                if iso[1] == "A":
                    iso_rect = Rectangle(color=YELLOW, width=rect_width, height=rect_height, fill_color=YELLOW, stroke_width=0.2, fill_opacity=1.0)
                    iso_rect.move_to(ax.c2p(iso[0], Z))
                    alpha_sprites.add(
                        iso_rect
                    )
        self.play(Create(alpha_sprites), run_time=3)
        self.wait()
        # Antimony/tellurium
        self.play(
            self.camera.frame.animate.scale(0.3).move_to(ax.c2p(53, 51)),
            run_time=2
        )
        self.wait()
        # Tellurium 128
        tl128_rect = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2, fill_color=BLUE, fill_opacity=1.0)
        tl128_rect.move_to(ax.c2p(76, 52))
        tl128_tex = Tex(r"$^{128}Tl$", font_size=1.5, color=BLACK).move_to(ax.c2p(76, 52))
        self.play(
            self.camera.frame.animate.scale(0.166666).move_to(ax.c2p(76, 52)),
            FadeIn(tl128_rect),
            FadeIn(tl128_tex),
            run_time=1.5
        )
        self.wait()
        # Berrylium 8
        be8_rect = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2)
        be8_rect.move_to(ax.c2p(4,4))
        be8_tex = Tex(r"$^{8}Be$", font_size=1.5, color=BLACK).move_to(ax.c2p(4, 4))
        self.play(
            self.camera.frame.animate.scale(20).move_to([0, 0, 0]),
            FadeOut(tl128_rect),
            FadeOut(tl128_tex),
            run_time=2
        )
        self.wait()
        self.play(
            self.camera.frame.animate.scale(0.05).move_to(ax.c2p(4, 4)),
            FadeOut(nz),
            FadeIn(be8_rect),
            FadeIn(be8_tex),
            run_time=2
        )
        self.wait()
        self.add_foreground_mobject(nz)
        self.play(
            self.camera.frame.animate.scale(20).move_to([0, 0, 0]),
            FadeOut(be8_rect),
            FadeOut(be8_tex),
            FadeIn(nz),
            run_time=2
        )
        self.wait()

        # Beta + / EC
        self.play(
            FadeIn(legend[2][0]),
            Write(legend[2][1])
        )
        self.wait()
        betap_sprites = VGroup()
        for Z in iso_data:
            for iso in iso_data[Z]:
                if iso[1] == "B+":
                    iso_rect = Rectangle(color=PINK, width=rect_width, height=rect_height, fill_color=PINK, stroke_width=0.2, fill_opacity=1.0)
                    iso_rect.move_to(ax.c2p(iso[0], Z))
                    betap_sprites.add(
                        iso_rect
                    )
        self.play(Create(betap_sprites), run_time=3)
        self.wait()

        # Beta -
        self.play(
            FadeIn(legend[3][0]),
            Write(legend[3][1])
        )
        self.wait()
        betam_sprites = VGroup()
        for Z in iso_data:
            for iso in iso_data[Z]:
                if iso[1] == "B-":
                    iso_rect = Rectangle(color=BLUE, width=rect_width, height=rect_height, fill_color=BLUE, stroke_width=0.2, fill_opacity=1.0)
                    iso_rect.move_to(ax.c2p(iso[0], Z))
                    betam_sprites.add(
                        iso_rect
                    )
        self.play(Create(betam_sprites), run_time=3)
        self.wait()

        # P
        self.play(
            FadeIn(legend[4][0]),
            Write(legend[4][1])
        )
        self.wait()
        p_sprites = VGroup()
        for Z in iso_data:
            for iso in iso_data[Z]:
                if iso[1] == "p":
                    iso_rect = Rectangle(color=ORANGE, width=rect_width, height=rect_height, fill_color=ORANGE, stroke_width=0.2, fill_opacity=1.0)
                    iso_rect.move_to(ax.c2p(iso[0], Z))
                    p_sprites.add(
                        iso_rect
                    )
        self.play(
            self.camera.frame.animate.scale(0.3).move_to(ax.c2p(20, 20)),
            run_time=2
        )
        self.play(Create(p_sprites), run_time=2)
        self.play(
            self.camera.frame.animate.scale(1 / 0.3).move_to([0, 0, 0]),
            run_time=2
        )
        self.wait()

        # N
        self.play(
            FadeIn(legend[5][0]),
            Write(legend[5][1])
        )
        self.wait()
        n_sprites = VGroup()
        for Z in iso_data:
            for iso in iso_data[Z]:
                if iso[1] == "n":
                    iso_rect = Rectangle(color=PURPLE, width=rect_width, height=rect_height, fill_color=PURPLE, stroke_width=0.2, fill_opacity=1.0)
                    iso_rect.move_to(ax.c2p(iso[0], Z))
                    n_sprites.add(
                        iso_rect
                    )
        self.play(
            self.camera.frame.animate.scale(0.3).move_to(ax.c2p(20, 10)),
            run_time=2
        )
        self.play(Create(n_sprites), run_time=2)
        self.play(
            self.camera.frame.animate.scale(1 / 0.3).move_to([0, 0, 0]),
            run_time=2
        )
        self.wait()

        # SF
        self.play(
            FadeIn(legend[6][0]),
            Write(legend[6][1])
        )
        self.wait()
        sf_sprites = VGroup()
        for Z in iso_data:
            for iso in iso_data[Z]:
                if iso[1] == "SF":
                    iso_rect = Rectangle(color=GREEN, width=rect_width, height=rect_height, fill_color=GREEN, stroke_width=0.2, fill_opacity=1.0)
                    iso_rect.move_to(ax.c2p(iso[0], Z))
                    sf_sprites.add(
                        iso_rect
                    )
        self.play(
            self.camera.frame.animate.scale(0.3).move_to(ax.c2p(160, 100)),
            run_time=2
        )
        self.play(Create(sf_sprites), run_time=2)
        self.play(
            self.camera.frame.animate.scale(1 / 0.3).move_to([0, 0, 0]),
            run_time=2
        )
        self.wait()

        # Thorium decay chain
        decay_chain = VGroup()
        th232_r = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2).move_to(ax.c2p(142, 90))
        th232_tex = Tex(r"$^{232}$Th", font_size=1.5, color=BLACK).move_to(ax.c2p(142, 90))
        alpha1_s = AlphaParticle().sprite.scale(0.04).move_to(ax.c2p(142, 91))
        alpha1_s[0].set_stroke_width(0.1).set_stroke_color(BLACK)
        decay_chain.add(th232_r, th232_tex, alpha1_s)
        self.play(
            self.camera.frame.animate.scale(0.05).move_to(ax.c2p(142, 90)),
            run_time=2
        )
        self.play(
            FadeIn(th232_r),
            FadeIn(th232_tex)
        )
        self.wait()
        self.play(FadeIn(alpha1_s))
        # Th232 alpha Ra288
        rad288_r = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2).move_to(ax.c2p(140, 88))
        rad288_tex = Tex(r"$^{228}$Ra", font_size=1.5, color=BLACK).move_to(ax.c2p(140, 88))
        beta1_s = BetaMinusParticle().sprite.scale(0.04).move_to(ax.c2p(140, 89))
        beta1_s[0].set_stroke_width(0.1).set_stroke_color(BLACK)
        arrow1 = Line(start=alpha1_s.get_center(), end=beta1_s.get_center(), stroke_color=BLACK, stroke_width=0.15, buff=0.02).add_tip(tip_length=0.008, tip_width=0.008)
        decay_chain.add(rad288_r, rad288_tex, beta1_s, arrow1)
        self.play(
            self.camera.frame.animate.move_to(ax.c2p(140, 88)),
            FadeIn(rad288_r),
            FadeIn(rad288_tex),
            FadeIn(beta1_s),
            Create(arrow1)
        )
        self.wait()
        # Ra288 beta- Ac288
        ac288_r = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2).move_to(ax.c2p(139, 89))
        ac288_tex = Tex(r"$^{228}$Ac", font_size=1.5, color=BLACK).move_to(ax.c2p(139, 89))
        beta2_s = BetaMinusParticle().sprite.scale(0.04).move_to(ax.c2p(139, 90))
        beta2_s[0].set_stroke_width(0.1).set_stroke_color(BLACK)
        arrow2 = Line(start=beta1_s.get_center(), end=beta2_s.get_center(), stroke_color=BLACK, stroke_width=0.15, buff=0.02).add_tip(tip_length=0.008, tip_width=0.008)
        decay_chain.add(ac288_r, ac288_tex, beta2_s, arrow2)
        self.play(
            self.camera.frame.animate.move_to(ax.c2p(139, 89)),
            FadeIn(ac288_r),
            FadeIn(ac288_tex),
            FadeIn(beta2_s),
            Create(arrow2)
        )
        self.wait()
        # Ac288 beta- Th228
        th288_r = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2).move_to(ax.c2p(138, 90))
        th288_tex = Tex(r"$^{228}$Th", font_size=1.5, color=BLACK).move_to(ax.c2p(138, 90))
        alpha2_s = AlphaParticle().sprite.scale(0.04).move_to(ax.c2p(138, 91))
        alpha2_s[0].set_stroke_width(0.1).set_stroke_color(BLACK)
        arrow3 = Line(start=beta2_s.get_center(), end=alpha2_s.get_center(), stroke_color=BLACK, stroke_width=0.15, buff=0.02).add_tip(tip_length=0.008, tip_width=0.008)
        decay_chain.add(th288_r, th288_tex, alpha2_s, arrow3)
        self.play(
            self.camera.frame.animate.move_to(ax.c2p(138, 90)),
            FadeIn(th288_r),
            FadeIn(th288_tex),
            FadeIn(alpha2_s),
            Create(arrow3)
        )
        self.wait()
        # Th228 alpha Ra224
        ra224_r = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2).move_to(ax.c2p(136, 88))
        ra224_tex = Tex(r"$^{224}$Ra", font_size=1.5, color=BLACK).move_to(ax.c2p(136, 88))
        alpha3_s = AlphaParticle().sprite.scale(0.04).move_to(ax.c2p(136, 89))
        alpha3_s[0].set_stroke_width(0.1).set_stroke_color(BLACK)
        arrow4 = Line(start=alpha2_s.get_center(), end=alpha3_s.get_center(), stroke_color=BLACK, stroke_width=0.15, buff=0.02).add_tip(tip_length=0.008, tip_width=0.008)
        decay_chain.add(ra224_r, ra224_tex, alpha3_s, arrow4)
        self.play(
            self.camera.frame.animate.move_to(ax.c2p(136, 88)),
            FadeIn(ra224_r),
            FadeIn(ra224_tex),
            FadeIn(alpha3_s),
            Create(arrow4)
        )
        self.wait()
        # Ra224 alpha Rn220
        rn220_r = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2).move_to(ax.c2p(134, 86))
        rn220_tex = Tex(r"$^{220}$Rn", font_size=1.5, color=BLACK).move_to(ax.c2p(134, 86))
        alpha4_s = AlphaParticle().sprite.scale(0.04).move_to(ax.c2p(134, 87))
        alpha4_s[0].set_stroke_width(0.1).set_stroke_color(BLACK)
        arrow5 = Line(start=alpha3_s.get_center(), end=alpha4_s.get_center(), stroke_color=BLACK, stroke_width=0.15, buff=0.02).add_tip(tip_length=0.008, tip_width=0.008)
        decay_chain.add(rn220_r, rn220_tex, alpha4_s, arrow5)
        self.play(
            self.camera.frame.animate.move_to(ax.c2p(134, 86)),
            FadeIn(rn220_r),
            FadeIn(rn220_tex),
            FadeIn(alpha4_s),
            Create(arrow5)
        )
        self.wait()
        # Ra220 alpha Po216
        po216_r = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2).move_to(ax.c2p(132, 84))
        po216_tex = Tex(r"$^{216}$Po", font_size=1.5, color=BLACK).move_to(ax.c2p(132, 84))
        alpha5_s = AlphaParticle().sprite.scale(0.04).move_to(ax.c2p(132, 85))
        alpha5_s[0].set_stroke_width(0.1).set_stroke_color(BLACK)
        arrow6 = Line(start=alpha4_s.get_center(), end=alpha5_s.get_center(), stroke_color=BLACK, stroke_width=0.15, buff=0.02).add_tip(tip_length=0.008, tip_width=0.008)
        decay_chain.add(po216_r, po216_tex, alpha5_s, arrow6)
        self.play(
            self.camera.frame.animate.move_to(ax.c2p(132, 84)),
            FadeIn(po216_r),
            FadeIn(po216_tex),
            FadeIn(alpha5_s),
            Create(arrow6)
        )
        self.wait()
        # Po216 alpha Pb212
        pb212_r = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2).move_to(ax.c2p(130, 82))
        pb212_tex = Tex(r"$^{212}$Pb", font_size=1.5, color=BLACK).move_to(ax.c2p(130, 82))
        beta3_s = BetaMinusParticle().sprite.scale(0.04).move_to(ax.c2p(130, 83))
        beta3_s[0].set_stroke_width(0.1).set_stroke_color(BLACK)
        arrow7 = Line(start=alpha5_s.get_center(), end=beta3_s.get_center(), stroke_color=BLACK, stroke_width=0.15, buff=0.02).add_tip(tip_length=0.008, tip_width=0.008)
        decay_chain.add(pb212_r, pb212_tex, beta3_s, arrow7)
        self.play(
            self.camera.frame.animate.move_to(ax.c2p(130, 82)),
            FadeIn(pb212_r),
            FadeIn(pb212_tex),
            FadeIn(beta3_s),
            Create(arrow7)
        )
        self.wait()
        # Pb212 beta- Bi212
        bi212_r = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2).move_to(ax.c2p(129, 83))
        bi212_tex = Tex(r"$^{212}$Bi", font_size=1.5, color=BLACK).move_to(ax.c2p(129, 83))
        beta4_s = BetaMinusParticle().sprite.scale(0.04).move_to(ax.c2p(129, 84))
        beta4_s[0].set_stroke_width(0.1).set_stroke_color(BLACK)
        arrow8 = Line(start=beta3_s.get_center(), end=beta4_s.get_center(), stroke_color=BLACK, stroke_width=0.15, buff=0.02).add_tip(tip_length=0.008, tip_width=0.008)
        decay_chain.add(bi212_r, bi212_tex, beta4_s, arrow8)
        self.play(
            self.camera.frame.animate.move_to(ax.c2p(129, 83)),
            FadeIn(bi212_r),
            FadeIn(bi212_tex),
            FadeIn(beta4_s),
            Create(arrow8)
        )
        self.wait()
        # Bi212 beta- Po212
        po212_r = Rectangle(color=BLACK, width=rect_width, height=rect_height, stroke_width=0.2).move_to(ax.c2p(128, 84))
        po212_tex = Tex(r"$^{212}$Po", font_size=1.5, color=BLACK).move_to(ax.c2p(128, 84))
        alpha6_s = AlphaParticle().sprite.scale(0.04).move_to(ax.c2p(128, 85))
        alpha6_s[0].set_stroke_width(0.1).set_stroke_color(BLACK)
        arrow9 = Line(start=beta4_s.get_center(), end=alpha6_s.get_center(
        ), stroke_color=BLACK, stroke_width=0.15, buff=0.02).add_tip(tip_length=0.008, tip_width=0.008)
        decay_chain.add(po212_r, po212_tex, alpha6_s, arrow9)
        self.play(
            self.camera.frame.animate.move_to(ax.c2p(128, 84)),
            FadeIn(po212_r),
            FadeIn(po212_tex),
            FadeIn(alpha6_s),
            Create(arrow9)
        )
        self.wait()
        # Po212 alpha Pb208
        pb208_r = Rectangle(color=WHITE, width=rect_width, height=rect_height, stroke_width=0.2).move_to(ax.c2p(126, 82))
        pb208_tex = Tex(r"$^{208}$Pb", font_size=1.5, color=WHITE).move_to(ax.c2p(126, 82))
        stable_tex = Tex(r"\underline{Stable}", font_size=1.5, color=BLACK).move_to(ax.c2p(126, 83))
        arrow10 = Line(start=alpha6_s.get_center(), end=stable_tex.get_center(), stroke_color=BLACK, stroke_width=0.15, buff=0.02).add_tip(tip_length=0.008, tip_width=0.008)
        decay_chain.add(pb208_r, pb208_tex, stable_tex, arrow10)
        self.play(
            self.camera.frame.animate.move_to(ax.c2p(126, 82)),
            FadeIn(pb208_r),
            FadeIn(pb208_tex),
            FadeIn(stable_tex),
            Create(arrow10)
        )
        self.wait()
        self.play(self.camera.frame.animate.scale(1.5).move_to(ax.c2p(134, 86)), run_time=2)
        self.wait()
        self.play(
            self.camera.frame.animate.scale(13.3333333).move_to([0, 0, 0]),
            FadeOut(decay_chain),
            run_time=2
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
