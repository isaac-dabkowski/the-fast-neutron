from manim import *


class BindingEnergyTitleCard(Scene):
    def construct(self):
        section_title = Tex("Nuclear binding energy and the semi-empirical mass formula")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class MassDefect(Scene):
    def construct(self):
        # Helper function to make protons
        def proton():
            proton = Circle(
                radius=0.35,
                color=RED,
            ).set_fill("#7d3129", opacity=1.0)
            return proton

        # Helper function to make neutrons
        def neutron():
            neutron = Circle(
                radius=0.35,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0)
            return neutron

        # Start with nucleons apart from one another
        he4_p1 = proton()
        he4_p2 = proton()
        he4_n1 = neutron()
        he4_n2 = neutron()
        he4 = VGroup(he4_p1, he4_p2, he4_n1, he4_n2).arrange(RIGHT, buff=LARGE_BUFF)
        self.play(GrowFromCenter(he4))
        self.wait()

        # Arrange into nucleus
        self.play(
            he4_p1.animate.move_to([-he4_p1.radius, he4_p1.radius, 0]),
            he4_p2.animate.move_to([he4_p1.radius, -he4_p1.radius, 0]),
            he4_n1.animate.move_to([he4_p1.radius, he4_p1.radius, 0]),
            he4_n2.animate.move_to([-he4_p1.radius, -he4_p1.radius, 0])
        )
        self.play(he4.animate.rotate(np.pi/4))
        self.wait()

        # Predicted mass of nucleus
        tex = Tex(r"\underline{What would you expect the mass of the $^4$He nucleus to be?}").to_edge(UP)
        self.play(Write(tex))
        self.wait()
        self.play(he4.animate.to_edge(LEFT))
        self.wait()
        mp_mn = Tex(r"$m_p = 1.007278$ amu, $m_n = 1.008665$ amu").next_to(tex, DOWN)
        amu_kg = Tex(r"$1\text{ amu} = 1.66054\text{e-}27\text{ kg}$").next_to(mp_mn, DOWN)
        he_mass_calc = VGroup(
            Tex(r"$M\left(^4\text{He}\right)=Z\cdot m_p + (A-Z)\cdot m_n$"),
            Tex(r"$M\left(^4\text{He}\right)=2\cdot m_p + 2\cdot m_n$"),
            Tex(r"$M\left(^4\text{He}\right)=2\cdot (1.007278\text{ u}) + 2\cdot(1.008665\text{ u})$"),
            Tex(r"$M\left(^4\text{He}\right)=4.031883\text{ u}$")
        ).arrange(DOWN, buff=MED_SMALL_BUFF, center=False, aligned_edge=LEFT).next_to(amu_kg, DOWN * 3).shift(RIGHT)
        self.play(Write(mp_mn))
        self.wait()
        self.play(Write(amu_kg))
        self.wait()
        for m in he_mass_calc:
            self.play(Write(m))
            self.wait()
        predicted_mass = he_mass_calc[-1].copy()
        self.play(
            FadeOut(he_mass_calc),
            FadeOut(mp_mn),
            FadeOut(amu_kg),
            Transform(
                predicted_mass,
                Tex("Predicted mass = 4.031883 u").next_to(tex, DOWN * 2)
            )
        )
        self.wait()

        # Reveal actual mass and mass defect
        actual_mass = Tex("Actual mass = 4.001506 u").next_to(predicted_mass, DOWN * 2).align_to(predicted_mass, RIGHT)
        self.play(Write(actual_mass))
        self.wait()
        mass_defect = Tex(r"$\Delta$m = 0.030377 u").next_to(actual_mass, DOWN * 2).align_to(actual_mass, RIGHT)
        self.play(Write(mass_defect))
        self.wait()
        self.play(Transform(mass_defect, Tex("Mass defect = 0.030377 u").next_to(actual_mass, DOWN * 2).align_to(actual_mass, RIGHT)))
        self.wait()

        # Discuss connection between mass defect and binding energy
        md_be =  VGroup(
            Tex("The nucleus is in a stable"),
            Tex("configuration, it would take"),
            Tex("energy input to pull it apart.")
        ).arrange(DOWN, buff=MED_SMALL_BUFF).next_to(mass_defect, DOWN).to_edge(DOWN)
        self.play(Write(md_be))
        self.wait()
        self.play(FadeOut(predicted_mass), FadeOut(actual_mass), mass_defect.animate.next_to(tex, DOWN))
        self.wait()
        einstein_pic = ImageMobject("assets/Einstein.jpg").scale(0.15).shift(DOWN * 0.5)
        einstein_border = SurroundingRectangle(
            einstein_pic,
            color=YELLOW,
            buff=0.0
        )
        self.play(FadeOut(md_be), FadeIn(einstein_pic), FadeIn(einstein_border))
        self.wait()
        be = Tex(r"$E=mc^{2}$").next_to(einstein_border, DOWN)
        self.play(Write(be))
        self.wait()
        self.play(FadeOut(einstein_pic), FadeOut(einstein_border))
        self.wait()
        self.play(Transform(be, Tex(r"$\text{BE}=\Delta m \cdot c^2$").next_to(mass_defect, DOWN * 3.0)))
        self.wait()
        self.play(Transform(be, Tex(r"$\text{BE}=\Delta m \cdot c^2=28.296\text{ MeV}$").next_to(mass_defect, DOWN * 3.0)))
        self.wait()

        # Hint at SEMF
        self.play(FadeOut(mass_defect), FadeOut(be))
        self.wait()
        semf = Tex(r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n$").shift(RIGHT)
        self.play(Write(semf))
        self.wait()
        wrong_line = Line(semf.get_left(), semf.get_right(), color=RED)
        self.play(
            Transform(semf, Tex(r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n$", color=RED).shift(RIGHT)),
            Create(wrong_line)
        )
        self.wait()
        self.play(
            Transform(semf, Tex(
                r"$M\left(^A_ZX\right)=Z\cdot m_p + (A-Z)\cdot m_n - \frac{\text{BE}}{c^2}$").shift(RIGHT)),
            FadeOut(wrong_line)
        )
        self.wait()
        # self.play(*[FadeOut(mob) for mob in self.mobjects])
        # self.wait()
