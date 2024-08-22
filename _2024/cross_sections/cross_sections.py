from manim import *
from resources import Proton, Electron

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
        # 
        # self.wait()
        # self.play(*[FadeOut(mob) for mob in self.mobjects])
        # self.wait()
