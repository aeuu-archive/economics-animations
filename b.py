from anim import *


class Characteristics(Scene):
    def construct(self):
        t1 = h('<u>Perfect Competition</u>')

        pc1 = t('Many small firms').next_to(t1, DOWN).align_to(t1, LEFT).shift(DOWN * 2)
        pc2 = t('Products are identical').next_to(pc1, DOWN).align_to(pc1, LEFT)
        pc3 = t('Low barriers to entry').next_to(pc2, DOWN).align_to(pc1, LEFT)
        pc4 = t('Firms are price takers').next_to(pc3, DOWN).align_to(pc1, LEFT)
        pc5 = t('No advertising').next_to(pc4, DOWN).align_to(pc1, LEFT)
        pc = (pc1, pc2, pc3, pc4, pc5)

        self.play(Write(t1))

        for k in pc:
            self.play(Write(k))

        ##########

        t2 = h('<u>PC vs Monopoly</u>')
        s1 = s('Perfect Competition').next_to(pc1, UP).align_to(ORIGIN, RIGHT).shift(LEFT)
        s2 = s('Monopoly').next_to(pc1, UP).align_to(ORIGIN, LEFT).shift(RIGHT)

        for k in pc:
            k.generate_target()

        pc1.target.next_to(s1, DOWN).shift(LEFT * 0.2)
        pc2.target.next_to(pc1, DOWN).align_to(pc1.target, LEFT)
        pc3.target.next_to(pc2, DOWN).align_to(pc2.target, LEFT)
        pc4.target.next_to(pc3, DOWN).align_to(pc3.target, LEFT)
        pc5.target.next_to(pc4, DOWN).align_to(pc4.target, LEFT)

        self.play(Transform(t1, t2), Write(s1), Write(s2), *[MoveToTarget(k) for k in pc])

        m1 = t('One large firm').move_to(pc1.get_center()).align_to(s2, LEFT)
        m2 = t('Products are unique').move_to(pc2.get_center()).align_to(m1, LEFT)
        m3 = t('High barriers to entry').move_to(pc3.get_center()).align_to(m2, LEFT)
        m4 = t('Firm is price maker').move_to(pc4.get_center()).align_to(m3, LEFT)
        m5 = t('Some advertising').move_to(pc5.get_center()).align_to(m4, LEFT)
        m = (m1, m2, m3, m4, m5)

        for i, k in enumerate(m):
            a = Arrow(k.get_left() + LEFT * 1.85, k.get_left(), color=RED, stroke_width=3, max_tip_length_to_length_ratio=0.15)

            self.play(Create(a))
            self.play(Write(k))
            self.play(FadeOut(a))

        self.wait(2)
