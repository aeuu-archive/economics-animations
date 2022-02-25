from anim import *


class Introduction(Scene):
    def construct(self):
        text = h('"Monopoly"').shift(DOWN * 3)
        self.play(Write(text))

        ##########
        self.play(text.animate.shift(UP * 3))

        text2 = t('Board game?').next_to(text, DOWN).shift(DOWN * 2)
        self.play(Write(text2))

        ##########
        text3 = t('Big companies?').next_to(text2, DOWN)
        self.play(Write(text3))

        ##########
        self.play(FadeOut(text2), FadeOut(text3))

        ##########
        title = h('<u>Monopolies and Monopoly Markets</u>')
        self.play(Transform(text, title))

        ##########
        compare = t('Characteristics').next_to(title, DOWN).shift(LEFT * 0.5).shift(DOWN * 2)
        self.play(Write(compare))

        ##########
        graphing = t('Graphing Monopolies').next_to(compare, DOWN).align_to(compare, LEFT)
        self.play(Write(graphing))

        ##########
        profit = t('Maximizing Profit').next_to(graphing, DOWN).align_to(compare, LEFT)
        self.play(Write(profit))

        self.wait(2)
