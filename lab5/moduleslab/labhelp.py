import numpy as np
from matplotlib import pyplot as plt


def axs_config(axises):
    r"""

        axis correct config for draw_graphics

    """
    for ax in axises.flat:
        ax.minorticks_on()
        ax.set(xlabel='x', ylabel='y')
        ax.grid(b=True, which='major', color='#666666', linestyle='-')
        ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        # ax.label_outer()
    return axises


def arr_sqsh(arr, size):
    r"""

        array squish to size (from 0 position to size)

    """
    return [arr[i] for i in range(int(size))]


def draw_graphics_getindexes(build_graph, build_amplitude, build_phase):
    r"""

        function return correct indexes for user needed subwindows in draw_graphics

    """
    bg_index = 0
    ba_index = 0
    bp_index = 0
    g_size = 0

    if build_graph and not build_amplitude and not build_phase:
        bg_index = 0
        g_size = 1

    if not build_graph and build_amplitude and not build_phase:
        ba_index = 0
        g_size = 1

    if not build_graph and not build_amplitude and build_phase:
        bp_index = 0
        g_size = 1

    if build_graph and build_amplitude and not build_phase:
        bg_index = 0
        ba_index = 1
        g_size = 2

    if build_graph and not build_amplitude and build_phase:
        bg_index = 0
        bp_index = 1
        g_size = 2

    if not build_graph and build_amplitude and build_phase:
        ba_index = 0
        bp_index = 1
        g_size = 2

    if build_graph and build_amplitude and build_phase:
        bg_index = 0
        ba_index = 1
        bp_index = 2
        g_size = 3

    return [bg_index, ba_index, bp_index, g_size]


def draw_graphics(t, funct, discret, time1y, time2y, time1ap, time2ap, build_graph, build_amplitude, build_phase, label_g, label_a, label_p):
    r"""

            This method is called for drawing:
            main function AND/OR phase-frequency characteristic AND/OR phase-frequency characteristic

            Specification for calling!
            Close current window to see next if you called function more than 1 time!


            t: vector
                vector of time
            funct: vector
                vector with function values
            discret: int
                discrete frequency
            time1y, time2y: int
                specify two dots for limitation of drawing main function
            time1ap, time2ap: int
                specify two dots for limitation of drawing characteristics (or characteristic)
            build_graph, build_amplitude, build_phase: boolean
                specify these three values to show graphs for each in row (true for showing, false to not show)
            label_g, label_a, label_p: string
                names of subwindows of graphs for each in row

            Returns: window with settings in function parameters

    """

    freqq = np.fft.fftfreq(len(t), d=1.0 / discret)
    yfft = np.fft.fft(funct)
    yphase = np.unwrap(np.angle(yfft))

    getindexes = draw_graphics_getindexes(build_graph, build_amplitude, build_phase)
    bg_index = getindexes[0]
    ba_index = getindexes[1]
    bp_index = getindexes[2]
    g_size = getindexes[3]

    fig, axs = plt.subplots(g_size, 1, squeeze=False)
    axs = axs_config(axs)

    if build_graph:
        axs[bg_index, 0].set_title(label_g)
        axs[bg_index, 0].plot(t, funct)
        axs[bg_index, 0].set(xlabel='t', ylabel='signal')
        axs[bg_index, 0].set_xlim([time1y, time2y])

    if build_amplitude:
        axs[ba_index, 0].set_title(label_a)
        axs[ba_index, 0].stem(arr_sqsh(freqq, len(freqq) / 2), arr_sqsh(2 / len(yfft) * np.abs(yfft), len(yfft) / 2))
        axs[ba_index, 0].set(xlabel='freq', ylabel='amplitudes of FFT')
        axs[ba_index, 0].set_xlim([time1ap, time2ap])

    if build_phase:
        axs[bp_index, 0].set_title(label_p)
        axs[bp_index, 0].stem(arr_sqsh(freqq, len(freqq) / 2), arr_sqsh(2 / len(yphase) * yphase, len(yphase) / 2))
        axs[bp_index, 0].set(xlabel='freq', ylabel='phase of FFT')
        axs[bp_index, 0].set_xlim([time1ap, time2ap])

    plt.show()
