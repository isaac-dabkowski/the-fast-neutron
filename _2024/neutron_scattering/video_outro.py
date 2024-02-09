from manim import *

class OutroCard(Scene):
    def construct(self):
        # Text
        tfw = Tex("Thanks for watching!").shift(UP * 0.5)
        # Credit Jonah for music
        jonah_tex = Tex("Music by Jonah Mendelson").shift(DOWN * 0.5)
        # Box for text
        texbox = SurroundingRectangle(VGroup(tfw, jonah_tex), color=YELLOW, fill_color=BLACK, fill_opacity=1.0, buff=0.1)
        # Mascot
        neutron_sprite = ImageMobject("assets/NeutronSprite.png").scale(0.3)
        # Mascot grid
        neutrons = [neutron_sprite for i in range(1, 51)]
        # Calculate the spacing between images
        image_spacing = 0.6
        rows = 5
        cols = 10
        grid_width = cols * (neutron_sprite.width + image_spacing)
        grid_height = rows * (neutron_sprite.height + image_spacing)

        # Position the images in a grid
        neutron_grid = list()
        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                if index < len(neutrons):
                    neutron_grid.append(ImageMobject("assets/NeutronSprite.png").scale(0.3).move_to([(j + 0.5) * (neutrons[0].width + image_spacing) - grid_width / 2, (i + 0.5) * (neutrons[0].height + image_spacing) - grid_height / 2, 0]))

        # Animate
        neutron_animations = AnimationGroup(*[FadeIn(n) for n in neutron_grid], lag_ratio=0.0, run_time=1, rate_func=rate_functions.linear)
        self.play(neutron_animations)
        self.wait()
        self.add_foreground_mobject(tfw)
        self.add_foreground_mobject(jonah_tex)
        self.play(DrawBorderThenFill(texbox, run_time=1))
        self.play(
            Write(tfw, run_time=1),
            Write(jonah_tex, run_time=1),
            
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
