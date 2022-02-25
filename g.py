from anim import *


class Conclusion(Scene):
    def construct(self):
        title = h('<u>Monopolies  Summary</u>')
        self.play(Write(title))

        ##########
        compare = t('Characteristics vs. PC').next_to(title, DOWN).shift(DOWN * 2)
        self.play(Write(compare))

        misconceptions = t('Common Misconceptions').next_to(compare, DOWN)
        self.play(Write(misconceptions))

        ##########
        graphing = t('Graphing Monopolies').next_to(misconceptions, DOWN)
        self.play(Write(graphing))

        ##########
        profit = t('Maximizing Profit').next_to(graphing, DOWN)
        self.play(Write(profit))

        self.play(*[FadeOut(k) for k in (title, compare, misconceptions, graphing, profit)])

        q = MarkupText('<u>Thank you!</u>', font_size=69, color=PURPLE_A)
        self.play(Write(q))

        self.wait(2)
