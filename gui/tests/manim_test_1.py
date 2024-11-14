import dearpygui.dearpygui as dpg 
from manim import * 


class OpenGLShow(Scene):
    def construct(self):
        circ = Circle()
        square = Square()
        self.add(circ, square)
        self.interactive_embed()