"""
Visualize SPICE simulation waveforms.
"""

import matplotlib.pyplot as plt


def voltage(time, values):

    plt.plot(time, values)

    plt.xlabel("Time (s)")

    plt.ylabel("Voltage (V)")

    plt.show()


def current(time, values):

    plt.plot(time, values)

    plt.xlabel("Time (s)")

    plt.ylabel("Current (A)")

    plt.show()
