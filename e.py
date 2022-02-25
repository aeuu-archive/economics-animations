from anim import *


def part_monopoly(align):
    graph = Axes(
        x_range=[0, 1.2, 1.2],
        y_range=[0, 1.2, 1.2],
        x_length=round((config.frame_height - 1) // 2)*1.8,
        y_length=round((config.frame_height - 1) // 2)*0.9,
        tips=False,
    ).next_to(align, DOWN * 2.5)
    graph_labels = graph.get_axis_labels(x_label='Q', y_label='P')

    l = DashedLine(end=(5.1, 0, 0)).rotate(PI / 2).shift(LEFT * 2.45).align_to(graph, UP)

    mr_graph = graph.plot(lambda x: 0.8-1.6*x, color=RED, x_range=[0, 0.6])
    mr_label = graph.get_graph_label(mr_graph, 'MR', x_val=0.6, direction=RIGHT/2)

    d_graph = graph.plot(lambda x: 0.8-0.7*x, color=BLUE, x_range=[0, 0.8])
    d_label = graph.get_graph_label(d_graph, 'P', x_val=0.8, direction=RIGHT/2)

    graph2 = Axes(
        x_range=[0, 1.2, 1.2],
        y_range=[0, 1.2, 1.2],
        x_length=round((config.frame_height - 1) // 2)*1.8,
        y_length=round((config.frame_height - 1) // 2)*0.9,
        tips=False,
    ).next_to(graph, DOWN * 2.5)
    graph2_labels = graph2.get_axis_labels(x_label='Q', y_label='TR')

    tr_graph = graph2.plot(lambda x: -4*(x**2 - x), color=GREEN, x_range=[0, 1])
    tr_label = graph2.get_graph_label(tr_graph, 'TR', x_val=1, direction=RIGHT/2 + UP)

    r_rect = Rectangle(color=BLUE, fill_color=BLUE, stroke_opacity=0, width=2.225, height=6.15, fill_opacity=0.3).next_to(align, DOWN).align_to(graph, LEFT).shift(RIGHT*0.1).shift(DOWN*0.375)
    r_label = t('elastic').next_to(r_rect, RIGHT + UP).shift(0.6*DOWN + 1.2*LEFT)
    r2_rect = Rectangle(color=GREEN, fill_color=GREEN, stroke_opacity=0, width=2.225, height=6.15, fill_opacity=0.3).next_to(align, DOWN).next_to(r_rect, RIGHT).shift(LEFT*0.2)
    r2_label = t('inelastic').next_to(r2_rect, RIGHT + UP).shift(0.6*DOWN + 1.5*LEFT)
    ue_anim = Circumscribe(l, run_time=2)

    g = VGroup(graph, graph_labels)
    g2 = VGroup(graph2, graph2_labels, l)
    mr = VGroup(mr_graph, mr_label)
    d = VGroup(d_graph, d_label)
    tr = VGroup(tr_graph, tr_label)
    r = VGroup(r_rect, r_label)
    r2 = VGroup(r2_rect, r2_label)

    return g, g2, mr, d, tr, r, r2, ue_anim


class Graph(Scene):
    def construct(self):
        t1 = h('<u>Comparing P, MR and TR</u>')
        g, g2, mr, d, tr, r, r2, ue = part_monopoly(t1)

        gr1 = (g, mr, d)
        for k in gr1:
            k.shift(DOWN * 1.5)

        self.play(Write(t1))

        self.play(Create(g))
        self.play(Create(mr), Create(d))
        self.play(*[k.animate.shift(UP * 1.5) for k in gr1])


        self.play(Create(g2))
        self.play(Create(tr))

        t2 = h('<u>Elasticity</u>')
        self.play(ReplacementTransform(t1, t2))

        self.play(FadeIn(r))
        self.play(FadeIn(r2))
        self.play(ue)
        self.play(FadeOut(r2))

        self.wait(2)
