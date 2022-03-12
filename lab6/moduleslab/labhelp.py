import numpy as np


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


def draw_graphics_getindexes(builds):
    r"""

        function return correct indexes for user needed subwindows in draw_graphics

    """
    res = [0, 0, 0, 0]
    current_pos = 0

    for i in range(3):
        if builds[i]:
            res[i] = current_pos
            current_pos += 1
            res[3] += 1
        else:
            res[i] = -1

    return [res[0], res[1], res[2]], res[3]


def draw_fft_graphics(plot, t, function, fs, builds, times, labels):
    r"""

            This method is called for drawing:
            main function AND/OR phase-frequency characteristic AND/OR phase-frequency characteristic

            Specification for calling!
            read all ATTENTION fields


            plot:
                same as 'plt' from 'from matplotlib import pyplot as plt'
                specify same variable in calls for multiple graphing
            t: vector
                vector of time
            function: vector
                vector with function values
            fs: int
                sampling frequency
            builds: boolean array
                specify these three values to show graphs for each in row (true for showing, false to not show)
                ATTENTION: specify all 3 boolean variables
            times: float arrays in array
                specify time limits for your True settings
                examples:
                    short writings for example:
                    X = True or False
                    func_limits = [func_lim1, func_lim2]
                    ampl_limits = [ampl_lim1, ampl_lim2]
                    phase_limits = [phase_lim1, phase_lim2]

                    universal form for all examples:
                    (X, X, X) = (func_limits, phase_limits, phase_limits)

                    shortened form - specify only that you put True in builds in same order:
                    (True, True, False) = (func_limits, ampl_limits)
                    (True, False, True) = (func_limits, phase_limits)
                    (True, False, False) = (func_limits)
            labels: string array
                names of sub windows of graphs for each in row

            Returns: nothing

    """

    indexes, size = draw_graphics_getindexes(builds)

    if size != 0:
        fig, axs = plot.subplots(size)
        axs = axs_config(axs)
        frequencies = np.fft.fftfreq(len(t), d=1.0 / fs)
        signal_amplitudes = np.abs(np.fft.fft(function))
        signal_phases = np.unwrap(np.angle(np.fft.fft(function)))

        times_arr = [t, frequencies, frequencies]
        functions_arr = [function, signal_amplitudes, signal_phases]
        stems = [False, True, True]
        labels_axis = [['Час, с', 'Частота, Гц', 'Частота, Гц'], ['Амплітуда, В', 'Амплітуда, В', 'Амплітуда, В']]

        for i in range(3):
            if builds[i]:
                axs[indexes[i]].set_title(labels[i])
                if stems[i]:
                    axs[indexes[i]].stem(times_arr[i], functions_arr[i])
                else:
                    axs[indexes[i]].plot(times_arr[i], functions_arr[i])
                axs[indexes[i]].set(xlabel=labels_axis[0][i], ylabel=labels_axis[1][i])
                axs[indexes[i]].set_xlim([times[i][0], times[i][1]])


def multiple_graphs(plot, xs, ys, fs, builds, labels):
    r"""

                This method is called for drawing:
                main function AND/OR phase-frequency characteristic AND/OR phase-frequency characteristic

                Specification for calling!
                read all ATTENTION fields


                plot:
                    same as 'plt' from 'from matplotlib import pyplot as plt'
                    specify same variable in calls for multiple graphing
                t: vector
                    vector of time
                function: vector
                    vector with function values
                fs: int
                    sampling frequency
                builds: boolean array
                    specify these three values to show graphs for each in row (true for showing, false to not show)
                    ATTENTION: specify all 3 boolean variables
                times: float arrays in array
                    specify time limits for your True settings
                    examples:
                        short writings for example:
                        X = True or False
                        func_limits = [func_lim1, func_lim2]
                        ampl_limits = [ampl_lim1, ampl_lim2]
                        phase_limits = [phase_lim1, phase_lim2]

                        universal form for all examples:
                        (X, X, X) = (func_limits, phase_limits, phase_limits)

                        shortened form - specify only that you put True in builds in same order:
                        (True, True, False) = (func_limits, ampl_limits)
                        (True, False, True) = (func_limits, phase_limits)
                        (True, False, False) = (func_limits)
                labels: string array
                    names of sub windows of graphs for each in row

                Returns: nothing

    """

    indexes, size = draw_graphics_getindexes(builds)

    if size != 0:
        fig, axs = plot.subplots(size, len(xs))
        axs = axs_config(axs)
        for j in range(len(xs)):
            frequencies = np.fft.fftfreq(len(xs[j]), d=1.0/fs)
            signal_amplitudes = np.abs(np.fft.fft(ys[j]))
            signal_phases = np.unwrap(np.angle(np.fft.fft(ys[j])))

            times_arr = [xs[j], frequencies, frequencies]
            functions_arr = [ys[j], signal_amplitudes, signal_phases]
            stems = [False, True, True]
            labels_axis = [['Час, с', 'Частота, Гц', 'Частота, Гц'], ['Амплітуда, В', 'Амплітуда, В', 'Амплітуда, В']]

            for i in range(len(stems)):
                if builds[i]:
                    axs[indexes[i], j].set_title(labels[i][j])

                    if stems[i]:
                        axs[indexes[i], j].stem(times_arr[i], functions_arr[i])
                        axs[indexes[i], j].set_xlim(0, fs / 2)
                    else:
                        axs[indexes[i], j].plot(times_arr[i], functions_arr[i])
                        axs[indexes[i], j].set_xlim(0, max(times_arr[0]))

                    if j == 0:
                        axs[indexes[i], j].set(xlabel=labels_axis[0][i], ylabel=labels_axis[1][i])
                    else:
                        axs[indexes[i], j].set(xlabel=labels_axis[0][i], ylabel='')

        fig.align_labels()







