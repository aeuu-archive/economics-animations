from manim import *


def h(text):
    return MarkupText(text, font_size=30, color=BLUE_B).move_to(UP * 3.2)


def s(text):
    return MarkupText(text, font_size=26, color=GREEN).move_to(UP * 3.2)


def t(text):
    return Text(text, font_size=24)
