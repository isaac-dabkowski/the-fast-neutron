from manim import *

from resources import Proton, Electron

class QValuesTitleCard(Scene):
    def construct(self):
        section_title = Tex("Q Values")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class QValues(Scene):
    def construct(self):
        # Q value definition
        q_tex = Tex(r"$Q = \text{Energy released during a nuclear process}$")
        self.play(Write(q_tex))
        self.wait()
        self.play(q_tex.animate.shift(UP * 2))
        self.wait()

        # Show energy balance
        energy_balance = Tex(r"$E_f = E_i$").next_to(q_tex, DOWN * 1.5)
        self.play(Write(energy_balance))
        self.wait()
        self.play(Transform(energy_balance, Tex(r"$\text{KE}_f  + M_f c^2 = \text{KE}_i + M_i c^2$").next_to(q_tex, DOWN * 1.5)))
        self.wait()
        self.play(Transform(energy_balance, Tex(r"$\text{KE}_f - \text{KE}_i = M_i c^2 - M_f c^2$").next_to(q_tex, DOWN * 1.5)))
        self.wait()

        # Derive Q value formula
        self.play(Transform(q_tex, Tex(r"$Q = M_i c^2 - M_f c^2$").shift(UP * 2)), FadeOut(energy_balance))
        self.wait()
        self.play(Transform(q_tex, Tex(r"$Q = -\Delta M c^2$").shift(UP * 2)))
        self.wait()

        # Exothermic example
        exo_endo_tex = MathTex("Q > 0: \\text{``Exothermic''}").next_to(q_tex, DOWN * 1.5)
        self.play(Write(exo_endo_tex))
        self.wait()
        x = Electron().sprite[0].set_y(-1).set_x(-10)
        X = Proton().sprite[0].set_y(-1)
        y = Proton().sprite[0].set_y(-1).set_fill_color(PURPLE).set_stroke_color("#56025c").scale(0.7)
        Y = Electron().sprite[0].set_y(-1).set_fill_color(PINK).set_stroke_color("#3e0142").scale(0.7)
        self.play(GrowFromCenter(X))
        self.wait()
        self.play(x.animate.set_x(0), run_time=2, rate_func=rate_functions.linear)
        self.remove(x, X)
        self.add(y, Y)
        self.play(y.animate.move_to([10, 2, 0]), Y.animate.move_to([10, -4, 0]), run_time=0.3, rate_func=rate_functions.linear)
        self.remove(y, Y)
        self.wait()

        # Endothermic example
        self.play(Transform(exo_endo_tex, MathTex("Q < 0: \\text{``Endothermic''}").next_to(q_tex, DOWN * 1.5)))
        x = Electron().sprite[0].set_y(-1).set_x(-10)
        X = Proton().sprite[0].set_y(-1)
        y = Proton().sprite[0].set_y(-1).set_fill_color(PURPLE).set_stroke_color("#56025c")
        Y = Electron().sprite[0].set_y(-1).set_fill_color(PINK).set_stroke_color("#3e0142")
        self.play(GrowFromCenter(X))
        self.wait()
        self.play(x.animate.set_x(0), run_time=0.5, rate_func=rate_functions.linear)
        self.remove(x, X)
        self.add(y, Y)
        self.play(y.animate.move_to([10, 2, 0]), Y.animate.move_to([10, -4, 0]), run_time=3, rate_func=rate_functions.linear)
        self.remove(y, Y)
        self.wait()
        self.play(FadeOut(exo_endo_tex))

        # Show excitation energy
        excite_tex = Tex(r"$M\left(^A_ZX^*\right) = M\left(^A_ZX\right) + \frac{E^*}{c^2}$")
        self.play(Write(excite_tex))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


