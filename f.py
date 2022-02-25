from anim import *


def full_graph(Cx=12.9407958589, Cy=18.3294056036):
    axes = Axes(
        x_range=[0, 1.1*Cx, 1],
        y_range=[0, 1.1*Cy, 2],
        x_length=round(config.frame_height * 1.2) - 2,
        x_axis_config={
            "numbers_to_include": np.arange(2, 12.01, 2),
        },
        y_axis_config={
            "numbers_to_include": np.arange(2, 20.01, 4),
        },
        tips=False,
    )
    axes_labels = axes.get_axis_labels(x_label='Q', y_label='P')

    d_f0 = lambda x: 1 - 0.765*x
    d_f = lambda x: Cy*d_f0(x/Cx)
    d_graph = axes.plot(d_f, color=BLUE, x_range=[0*Cx, 0.85*Cx])
    d_label = axes.get_graph_label(d_graph, 'D', x_val=0.85*Cx, direction=RIGHT / 2)

    mr_f0 = lambda x: 1 - 2 * x
    mr_f = lambda x: Cy*mr_f0(x/Cx)
    mr_graph = axes.plot(mr_f, color=GREEN, x_range=[0*Cx, 0.45*Cx])
    mr_label = axes.get_graph_label(mr_graph, 'MR', x_val=0.45*Cx, direction=RIGHT / 2)

    atc_f0 = lambda x: 2 * ((x - 0.4) ** 2) + 0.5
    atc_f = lambda x: Cy*atc_f0(x/Cx)
    atc_graph = axes.plot(atc_f, color=RED, x_range=[0.05*Cx, 0.75*Cx])
    atc_label = axes.get_graph_label(atc_graph, 'ATC', x_val=0.75*Cx, direction=RIGHT / 2)

    mc_f0 = lambda x: (30 * ((0.1614 - (x - 0.00396)) ** 2) + 0.209) if x <= 0.185 else (1.3 * (x - 0.0538) + 0.05)
    mc_f = lambda x: Cy*mc_f0(x/Cx)
    mc_graph = axes.plot(mc_f, color=YELLOW, x_range=[0.11*Cx, 0.65*Cx, 0.005*Cx])
    mc_label = axes.get_graph_label(mc_graph, 'MC', x_val=0.65*Cx, direction=RIGHT / 2)

    return (axes, axes_labels), (d_f, d_graph, d_label), (mr_f, mr_graph, mr_label), (atc_f, atc_graph, atc_label), (
        mc_f, mc_graph, mc_label)


class MaximizeProfit(Scene):
    def construct(self):
        text = h('Maximizing Profit').shift(DOWN * 3)
        self.play(Write(text))

        ##########
        text2 = h('<u>Maximizing Profit</u>')
        self.play(text.animate.shift(UP * 3), ReplacementTransform(text, text2))

        (ax, al), (d, dg, dl), (mr, mrg, mrl), (atc, atcg, atcl), (mc, mcg, mcl) = full_graph()

        self.play(*[FadeIn(k) for k in (ax, al, dg, dl, mrg, mrl, atcg, atcl, mcg, mcl)])

        t = ValueTracker(0)
        mrd = Dot(point=0)
        mrd.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), mr(t.get_value()))))
        # mcd = Dot(point=0)
        # mcd.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), mc(t.get_value()))))

        # line_1 = ax.get_horizontal_line(ax.i2gp(0, mrg), color=ORANGE)
        # line_2 = ax.get_vertical_line(ax.i2gp(0, mrg), color=ORANGE)
        line_1 = always_redraw(lambda: DashedLine(color=ORANGE))
        line_2 = always_redraw(lambda: DashedLine(color=ORANGE))

        def u1(x):
            v = t.get_value()
            x.put_start_and_end_on(ax.c2p(0, mr(v)), ax.c2p(v, mr(v)))

        def u2(x):
            v = t.get_value()
            x.put_start_and_end_on(ax.c2p(v, 0), ax.c2p(v, mr(v)))

        line_1.add_updater(u1)
        line_2.add_updater(u2)

        x_space = np.linspace(*ax.x_range[:2], 400)
        target_index = 112

        self.add(line_1, line_2, mrd)
        self.play(t.animate.set_value(x_space[target_index]))

        v = t.get_value()
        line_3 = DashedLine(start=ax.c2p(v, d(v)), end=ax.c2p(0, d(v)), color=ORANGE)
        line_4 = DashedLine(start=ax.c2p(v, d(v)), end=ax.c2p(v, 0), color=ORANGE)

        # self.play(Uncreate(line_2))
        self.play(FadeOut(line_2), Create(line_3), Create(line_4))

        self.wait(2)
