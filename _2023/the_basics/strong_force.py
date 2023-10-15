from manim import *
import math

class StrongForceTitleCard(Scene):
    def construct(self):
        section_title = Tex("The strong nuclear force")
        self.wait()
        self.play(Write(section_title))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class CoulombAnimation(Scene):
    # Helper function that calculates the electric field at a single point
    def calculate_e_field_at_point(self, protons, point):
        # Initialize the field to zero
        field_at_point = np.array([0.0, 0.0, 0.0])

        # Calculate the field contribution from each proton
        for proton in protons:
            proton_position = [proton.get_x(), proton.get_y(), proton.get_z()]
            r_ = np.array(point) - np.array(proton_position)
            r_squared = np.linalg.norm(r_) ** 2
            # Prevent division by zero
            field_at_point += r_ / max(r_squared, 0.05)
        return field_at_point

    # Helper function that calculates the overall electric field given some protons
    def calculate_e_field(self, protons):
        e_field = ArrowVectorField(
            lambda point: self.calculate_e_field_at_point(protons, point),
            length_func=lambda norm: 0.5 * norm,  # Adjust the length of the vectors
            color=BLUE
        )
        return e_field

    def construct(self):
        # Helper function to make protons
        def proton():
            proton = Circle(
                radius=0.35,
                color=RED,
            ).set_fill("#7d3129", opacity=1.0)
            return proton

        # Make two protons
        proton1 = proton().shift(LEFT * 2.5)
        proton2 = proton().shift(RIGHT * 2.5)
        self.play(GrowFromCenter(proton1), GrowFromCenter(proton2))
        self.wait()
        proton1_label = Tex("+1 e").next_to(proton1, UP)
        proton2_label = Tex("+1 e").next_to(proton2, UP)
        self.play(Write(proton1_label), Write(proton2_label))
        self.wait()
        self.play(FadeOut(proton1_label), FadeOut(proton2_label))
        self.wait()

        # Show the protons moving closer to one another, then repelled
        animations = [
            proton1.animate.shift([4, 0, 0]).set_rate_func(rate_functions.linear),
            proton2.animate.shift([7, 0, 0]).set_rate_func(rate_functions.ease_in_quad),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.35), run_time=4)
        self.wait()

        # Bring one proton back
        self.play(
            proton1.animate.set_x(0)
        )
        self.wait()

        # Show the single proton's electric field
        e_field = self.calculate_e_field([proton1])
        self.bring_to_back(e_field)
        self.play(
            GrowFromCenter(e_field)
        )
        self.wait()

        # Move first proton to the right
        e_field_updated = self.calculate_e_field([proton().set_x(-1.5)])
        self.play(
            proton1.animate.set_x(-1.5),
            Transform(e_field, e_field_updated)
        )
        self.wait()

        # Bring in second proton to show how it will impact the field
        proton2.set_x(1.5)
        e_field_updated = self.calculate_e_field([proton1, proton().set_x(1.5)])
        self.play(
            GrowFromCenter(proton2),
            Transform(e_field, e_field_updated)
        )
        self.wait()

        # Shift the whole setup to the left
        e_field_updated = self.calculate_e_field([proton().set_x(-4.5), proton().set_x(0.0)])
        self.play(
            proton1.animate.set_x(-4.5),
            proton2.animate.set_x(0.0),
            Transform(e_field, e_field_updated)
        )
        self.wait()

        # Display Coulomb eq
        tex_coulomb = Tex(r"$F=k_e\frac{q_1\cdot q_2}{r^2}$").shift(UP * 2.5 + RIGHT * 4.5)
        tex_coulomb_bkg = BackgroundRectangle(tex_coulomb, color=BLACK, fill_opacity=1.0, buff=0.0)
        self.play(
            FadeIn(tex_coulomb_bkg),
            Write(tex_coulomb)
        )
        self.wait()

        # Set up canvas for plot below equation
        graph_bkg = Rectangle(color=BLACK, height=4.0, width=5.0).next_to(tex_coulomb, DOWN).set_fill(BLACK, opacity=1.0)
        ax = Axes(
            x_range=[0.1, 1.15, 1],
            y_range=[0, 28, 1],
            tips=False,
            axis_config={"include_numbers": False, "include_ticks": False},
            x_length=3.0,
            y_length=2.5
        ).move_to(graph_bkg.get_center())
        ax_x_label = ax.get_x_axis_label(Tex("r"), edge=DOWN, direction=DOWN, buff=0.2)
        ax_y_label = ax.get_y_axis_label(Tex("F"), edge=LEFT, direction=LEFT, buff=0.2)
        graph_canvas = VGroup(
            graph_bkg,
            SurroundingRectangle(graph_bkg, color=YELLOW, buff=0.0)
        )
        self.play(FadeIn(graph_canvas), DrawBorderThenFill(ax), Write(ax_x_label), Write(ax_y_label))
        self.wait()

        # Draw brace
        brace = Brace(
            Line(
                start=proton1.get_center(),
                end=proton2.get_center()
            ).shift(UP * 0.25),
            UP
        )
        brace.add_updater(
            lambda m: m.become(
                Brace(
                    Line(
                        proton1.get_center(),
                        proton2.get_center()
                    ).shift(UP * 0.25),
                    UP
                )
            )
        )
        _, number = label = VGroup(
            Text("r = "),
            DecimalNumber(
                0,
                show_ellipsis=False,
                num_decimal_places=2,
                include_sign=False,
            )
        )
        label.arrange(RIGHT)
        label.next_to(brace, UP)
        label_bkg = Rectangle(color=YELLOW, fill_color=BLACK, height=label.get_height() * 1.7, fill_opacity=1.0, width=label.get_width() * 1.2)
        label_bkg.move_to(label.get_center())
        # always(self.bring_to_front, label)
        number.add_updater(lambda m: m.set_value((proton2.get_x() - proton1.get_x()) / 4.5))
        self.play(
            FadeIn(brace),
            FadeIn(label_bkg),
            Write(label)
        )
        self.wait()

        # Add dot to graph
        dot = Dot(ax.coords_to_point(number.get_value(), number.get_value() ** -2))
        dot.add_updater(lambda m: m.become(Dot(ax.coords_to_point(number.get_value(), number.get_value() ** -2))))
        self.play(
            FadeIn(dot)
        )
        self.wait()

        # This traces the path of the plot
        self.curve = VGroup()
        self.curve.add(Line(dot.get_center(), dot.get_center()))
        def update_curve():
            self.curve.add(Line(self.curve[-1].get_end(), np.array(dot.get_center()), color=YELLOW_D))
            return self.curve
        coulomb_plot = always_redraw(update_curve)
        self.add(coulomb_plot)

        # Shift protons inward, calculate Coulomb force
        self.bring_to_front(dot)
        e_field_updated = self.calculate_e_field([proton().set_x(-2.7), proton().set_x(-1.8)])
        self.play(
            proton1.animate.set_x(-2.7),
            proton2.animate.set_x(-1.8),
            Transform(e_field, e_field_updated),
            run_time=5
        )
        self.wait()

        # Move the protons back
        e_field_updated = self.calculate_e_field([proton().set_x(-4.5), proton().set_x(0)])
        self.play(
            proton1.animate.set_x(-4.5),
            proton2.animate.set_x(0.0),
            Transform(e_field, e_field_updated),
            run_time=5
        )
        self.wait()

        # One more time
        e_field_updated = self.calculate_e_field([proton().set_x(-2.7), proton().set_x(-1.8)])
        self.play(
            proton1.animate.set_x(-2.7),
            proton2.animate.set_x(-1.8),
            Transform(e_field, e_field_updated),
            run_time=5,
            rate_func=rate_functions.double_smooth
        )
        self.wait()
        e_field_updated = self.calculate_e_field([proton().set_x(-4.5), proton().set_x(0)])
        self.play(
            proton1.animate.set_x(-4.5),
            proton2.animate.set_x(0.0),
            Transform(e_field, e_field_updated),
            run_time=5,
            rate_func=rate_functions.exponential_decay
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class StrongForceAnimation(Scene):
    def construct(self):
        # Helper function to make protons
        def proton():
            proton = Circle(
                radius=0.5,
                color=RED,
            ).set_fill("#7d3129", opacity=1.0)
            return proton

        # Helper function to make neutrons
        def neutron():
            neutron = Circle(
                radius=0.5,
                color=GREEN,
            ).set_fill("#416033", opacity=1.0)
            return neutron

        # "How is possible?" bit"
        he3_p1 = proton()
        he3_p2 = proton()
        he3_n = neutron()
        he3 = VGroup(
            he3_p1,
            he3_p2,
            he3_n
        )
        he3_p2.move_to([he3_p2.radius, np.sqrt(3)/2*he3_p2.radius, 0])
        he3_p1.move_to([-he3_p1.radius, np.sqrt(3)/2*he3_p1.radius, 0]),
        he3_n.move_to([0, -np.sqrt(3)/2*he3_n.radius, 0])
        self.play(
            GrowFromCenter(he3)
        )
        tex1 = Tex("How can a nucleus even exist?").next_to(he3, UP * 2)
        self.wait()
        self.play(Write(tex1))
        self.wait()
        self.play(Wiggle(he3), FadeOut(tex1))
        self.play(Wiggle(he3, run_time=0.75))
        self.play(Wiggle(he3, run_time=0.6))
        self.play(
            he3_p1.animate.move_to([-10, 6, 0]),
            he3_p2.animate.move_to([8, 11, 0]),
            he3_n.animate.move_to([-2, -8, 0]),
            rate_func=rate_functions.ease_in_cubic,
            run_time=0.3
        )
        self.wait()

        # Strong force diagram
        ax = Axes(
            x_range=[0, 4, 1],
            y_range=[-1.5, 1.5, 1],
            tips=False,
            y_axis_config={"include_numbers": False, "include_ticks": False},
            x_axis_config={"include_numbers": True,  "font_size": 30},
            x_length=3.0,
            y_length=2.5
        ).scale(2).shift(DOWN)
        ax_x_label = ax.get_x_axis_label(
            Tex("$r$ (fm)", font_size = 50), edge=RIGHT, buff=0.1)
        ax_y_label = ax.get_y_axis_label(
            Tex("$V(r)$"), edge=LEFT + UP, direction=UP, buff=0.2)
        plot_label = Tex(r"\underline{The strong nuclear force}").next_to(ax, UP * 4.5)
        sf = ax.plot(
            lambda x : -0.25 * (-2 * np.exp(-(x - 2)) + (np.exp(-2 * (x - 2))) / (x + 2)) * (math.tanh(x - 1.5) - 1),
            x_range = [0.25, 4],
            color=YELLOW
        )
        self.play(
            Write(plot_label)
        )
        self.wait()
        self.play(
            FadeIn(ax),
            FadeIn(ax_x_label),
            FadeIn(ax_y_label)
        )
        self.wait()
        self.play(Create(sf), run_time=3)
        sf_grp = VGroup(
            ax,
            ax_x_label,
            ax_y_label,
            sf
        )
        self.wait()

        # Discussion of strong force
        self.play(
            sf_grp.animate.shift(LEFT * 3.25)
        )
        self.wait()
        tex1 = VGroup(Tex("Much stronger than the", font_size=35), Tex("other fundamental forces", font_size=35)).arrange(DOWN)
        tex2 = Tex("Acts at very short distances", font_size=35)
        tex3 = VGroup(Tex("Has an attractive and", font_size=35), Tex(
            "repulsive component", font_size=35)).arrange(DOWN)
        tex4 = Tex("Does not care about charge", font_size=35)
        tex_sf = VGroup(tex1, tex2, tex3, tex4).arrange(DOWN, buff=LARGE_BUFF).next_to(ax_x_label, RIGHT).shift(UP * 0.5)
        pos_pot = Rectangle(stroke_width=0.0, fill_color=RED, fill_opacity=0.4, width=ax.x_length*2, height=ax.y_length).move_to(ax.coords_to_point(2, 0.75))
        neg_pot = Rectangle(stroke_width=0.0, fill_color=BLUE, fill_opacity=0.4, width=ax.x_length*2, height=ax.y_length).move_to(ax.coords_to_point(2, -0.75))
        self.play(Write(tex1))
        self.wait()
        self.play(Write(tex2))
        self.wait()
        self.play(Write(tex3))
        self.wait()
        self.play(FadeIn(neg_pot))
        self.wait()
        self.play(FadeOut(neg_pot), FadeIn(pos_pot))
        self.wait()
        self.play(Write(tex4), FadeOut(pos_pot))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

        # Neutrons as glue
        he3_p1 = proton()
        he3_p2 = proton()
        he3_n = neutron()
        he3 = VGroup(
            he3_p1,
            he3_p2,
            he3_n
        )
        he3_p2.move_to([he3_p2.radius, np.sqrt(3)/2*he3_p2.radius, 0])
        he3_p1.move_to([-he3_p1.radius, np.sqrt(3)/2*he3_p1.radius, 0]),
        he3_n.move_to([0, -np.sqrt(3)/2*he3_n.radius, 0])
        self.play(
            GrowFromCenter(he3_p1),
            GrowFromCenter(he3_p2)
        )
        self.wait()
        tex = Tex("Not stable", color=RED).next_to(he3, UP)
        self.play(Write(tex))
        self.wait()
        self.play(
            GrowFromCenter(he3_n),
            Transform(tex, Tex("Stable", color=GREEN).next_to(he3, UP))
        )
        self.wait()
        self.play(
            FadeOut(he3),
            FadeOut(tex)
        )
        self.wait()
        tex2 = VGroup(
            Tex("Neutrons increase the number of nucleons available"),
            Tex("for strong interactions without increasing electrostatic repulsion")
        ).arrange(DOWN)
        tex3 = Tex("Neutrons \"space out\" protons from one another")
        tex4 = VGroup(
            Tex("Neutrons and protons are both fermions, but they"),
            Tex("are distinguishable - so neutrons help nuclei"),
            Tex("cooperate with the Pauli Exclusion Principle")
        ).arrange(DOWN)
        all_tex = VGroup(
            tex2,
            tex3,
            tex4
        ).arrange(DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(tex2))
        self.wait()
        self.play(FadeIn(tex3))
        self.wait()
        self.play(FadeIn(tex4))
        self.wait()
        self.play(FadeOut(all_tex))
        self.wait()