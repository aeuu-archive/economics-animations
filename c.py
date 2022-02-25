from anim import *


class TrueFalse(Scene):
    def construct(self):
        t1 = h('<u>True or False?</u>')

        # q1 = t('1. All monopolies make a profit').next_to(t1, DOWN).align_to(t1, LEFT).shift(LEFT * 1.3).shift(DOWN)
        # q2 = t('2. Monopolies are usually efficient').next_to(q1, DOWN).align_to(q1, LEFT)
        # q3 = t('3. All monopolies are bad for the economy').next_to(q2, DOWN).align_to(q1, LEFT)
        # q4 = t('4. All monopolies are illegal').next_to(q3, DOWN).align_to(q1, LEFT)
        # q5 = t('5. Monopolies always charge\n\tthe highest price possible').next_to(q4, DOWN).align_to(q1, LEFT)
        # q6 = t('6. The government never prevent\n\tmonopolies from forming').next_to(q5, DOWN).align_to(q1, LEFT)
        q1 = t('All monopolies make a profit').next_to(t1, DOWN).shift(DOWN)
        q2 = t('Monopolies are usually efficient').next_to(q1, DOWN)
        q3 = t('All monopolies are bad for the economy').next_to(q2, DOWN)
        q4 = t('All monopolies are illegal').next_to(q3, DOWN)
        q5 = t('Monopolies always charge the highest price possible').next_to(q4, DOWN)
        q6 = t('The government never prevents monopolies from forming').next_to(q5, DOWN)
        q = (q1, q2, q3, q4, q5, q6)

        self.play(Write(t1))
        self.play(*[Create(k) for k in q])

        for k in q:
            self.play(Create(Line(k.get_left() + LEFT * 0.05, k.get_right() + RIGHT * 0.05, color=RED)))

        self.wait(2)
