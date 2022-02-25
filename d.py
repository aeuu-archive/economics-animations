from anim import *


def full_graph():
    axes = Axes(
        x_range=[0, 1.1, 1.1],
        y_range=[0, 1.1, 1.1],
        x_length=round(config.frame_height * 1.2) - 2,
        tips=False,
    )
    axes_labels = axes.get_axis_labels(x_label='Q', y_label='P')

    d_graph = axes.plot(lambda x: 1 - x, color=BLUE, x_range=[0, 0.85])
    d_label = axes.get_graph_label(d_graph, 'D', x_val=0.85, direction=RIGHT / 2)

    mr_graph = axes.plot(lambda x: 1 - 2 * x, color=GREEN, x_range=[0, 0.45])
    mr_label = axes.get_graph_label(mr_graph, 'MR', x_val=0.45, direction=RIGHT / 2)

    atc_graph = axes.plot(lambda x: 2 * ((x - 0.4) ** 2) + 0.5, color=RED, x_range=[0.05, 0.75])
    atc_label = axes.get_graph_label(atc_graph, 'ATC', x_val=0.75, direction=RIGHT / 2)

    mc_graph = axes.plot(
        lambda x: (30 * ((0.1614 - (x - 0.00396)) ** 2) + 0.209) if x <= 0.185 else (1.3 * (x - 0.0538) + 0.05),
        color=YELLOW, x_range=[0.11, 0.65, 0.005])
    mc_label = axes.get_graph_label(mc_graph, 'MC', x_val=0.65, direction=RIGHT / 2)

    graph = VGroup(axes, axes_labels)
    d = VGroup(d_graph, d_label)
    mr = VGroup(mr_graph, mr_label)
    atc = VGroup(atc_graph, atc_label)
    mc = VGroup(mc_graph, mc_label)

    return graph, d, mr, atc, mc


def full_mc():
    industry = Axes(
        x_range=[0, 1, 1],
        y_range=[0, 1, 1],
        x_length=round((config.frame_width - 2.25) // 2),
        y_length=round((config.frame_width - 2.25) // 2),
        tips=False,
    ).align_to(ORIGIN, RIGHT).shift(LEFT / 2).shift(DOWN * 0.5)
    industry_title = h('<u>Industry</u>').next_to(industry, UP * 2.4)
    industry_labels = industry.get_axis_labels(x_label='Q', y_label='P')

    d_graph = industry.plot(lambda x: 1 - x, color=RED, x_range=[0.13, 0.87])
    d_label = industry.get_graph_label(d_graph, 'D', x_val=0.87, direction=RIGHT / 2)

    s_graph = industry.plot(lambda x: x, color=GREEN, x_range=[0.13, 0.87])
    s_label = industry.get_graph_label(s_graph, 'S', x_val=0.87, direction=RIGHT / 2)

    firm = Axes(
        x_range=[0, 1.1, 1.1],
        y_range=[0, 1.1, 1.1],
        x_length=round((config.frame_width - 2.25) // 2),
        y_length=round((config.frame_width - 2.25) // 2),
        tips=False,
    ).align_to(ORIGIN, LEFT).shift(RIGHT / 2).shift(DOWN * 0.5)
    firm_title = h('<u>Firm</u>').next_to(firm, UP * 2.4)
    firm_labels = firm.get_axis_labels(x_label='Q', y_label='P')

    mrdarp_graph = firm.plot(lambda x: 0.5, color=BLUE, x_range=[0, 1])
    mrdarp_label = firm.get_graph_label(mrdarp_graph, 'MR=D', x_val=1.2, direction=RIGHT * 1.3 + UP * 0.4)

    mc_graph = firm.plot(lambda x: (0.5 - 0.75 * x) if x < 0.4 else (x - 0.2), color=YELLOW, x_range=[0.1, 1, 0.19])
    mc_label = firm.get_graph_label(mc_graph, 'MC', x_val=1, direction=RIGHT / 2)

    atc_graph = firm.plot(lambda x: (x - 0.55) ** 2 / 1.2 + 0.35, color=RED, x_range=[0.18, 0.9, 0.01])
    atc_label = firm.get_graph_label(atc_graph, 'ATC', x_val=0.9, direction=RIGHT / 2 + DOWN * 0.3)

    graph = VGroup(industry, industry_title, industry_labels, firm, firm_title, firm_labels)
    di = VGroup(d_graph, d_label)
    si = VGroup(s_graph, s_label)
    df = VGroup(mrdarp_graph, mrdarp_label)
    mc = VGroup(mc_graph, mc_label)
    atc = VGroup(atc_graph, atc_label)

    return graph, di, si, df, mc, atc


class Graph(Scene):
    def construct(self):
        text = h('Graphing Monopolies').shift(DOWN * 3)
        self.play(Write(text))

        ##########
        text2 = h('<u>Perfect Competition</u>')
        self.play(text.animate.shift(UP * 3), ReplacementTransform(text, text2))

        mc = VGroup(*full_mc())
        self.play(FadeIn(mc))
        self.play(FadeOut(mc))

        ##########
        text3 = h('<u>Similarities</u>')
        s1 = t('Profit Maximizing Rule: MR = MC').next_to(text3, DOWN).shift(DOWN * 2)
        s2 = t('Shutdown Point Rule').next_to(s1, DOWN)

        self.play(ReplacementTransform(text2, text3))
        self.play(Write(s1), Write(s2))

        self.play(FadeOut(s1), FadeOut(s2))

        title = h('<u>Monopoly Graph</u>')
        self.play(ReplacementTransform(text3, title))

        graph, d, mr, atc, mc = m = full_graph()

        self.play(Create(graph))

        self.play(Create(d))
        self.play(Create(mr))
        self.play(Create(mc))
        self.play(Create(atc))

        self.wait(2)


class Explanation(Scene):
    def construct(self):
        text = h('<u>Why is MR &lt; D?</u>').shift(DOWN * 3)
        self.play(Write(text))
        self.play(text.animate.shift(UP * 3))

        Qd = range(0, 8)
        P = [22-2*Qd[x] for x in range(0, 8)]
        TR = [P[x] * Qd[x] for x in range(0, 8)]
        MR = [TR[x] - TR[x - 1] for x in range(1, 8)]

        table = Table(
            [
                [f'${p}' for p in P],
                [f'{qd}' for qd in Qd],
                [f'${tr}' for tr in TR],
                ['-'] + [f'${mr}' for mr in MR]
            ],
            row_labels=[MathTex(k) for k in ('P', 'Q_d', 'TR', 'MR')],
            include_outer_lines=True,
        ).scale_to_fit_width(config.frame_width - 2)
        self.play(Create(table))

        self.play(Circumscribe(table.get_columns()[2], buff=MED_SMALL_BUFF, fade_out=True, run_time=3))
        self.play(Circumscribe(table.get_columns()[3], buff=MED_SMALL_BUFF, fade_out=True, run_time=3))

        c1 = table.get_cell((4, 3), color=GREEN)
        c2 = table.get_cell((4, 4), color=RED)

        self.play(Create(c1))
        self.play(Create(c2))

        self.play(FadeOut(c1), FadeOut(c2))
        self.play(Circumscribe(table.get_rows()[3], buff=MED_SMALL_BUFF, fade_out=True, run_time=2))

        self.wait(2)
