import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

# Constants
TWO_PI = 2 * np.pi
LIGHT_GREY = (0.3, 0.3, 0.3)
MAX_CHORDS_PLOT = 1000
NUM_CHORDS = 10000
RADIUS = 1
TRIANGLE_SIDE_LENGTH = RADIUS * np.sqrt(3)

def prepare_axes():
    """Set up the plot with circles and proper limits."""

    fig, axes = plt.subplots(nrows=1, ncols=2, subplot_kw={'aspect': 'equal'})
    for ax in axes:
        circle = Circle((0, 0), RADIUS, facecolor='none')
        ax.add_artist(circle)
        ax.set_xlim((-RADIUS, RADIUS))
        ax.set_ylim((-RADIUS, RADIUS))
        ax.axis('off')
    return fig, axes

def plot_chords(method_number):
    # Plot the chords and their midpoints based on the selected method.
    chords, midpoints = generate_chords_method1()

    # Keep track of chords longer than the threshold
    success = [False] * NUM_CHORDS

    fig, axes = prepare_axes()
    for i, chord in enumerate(chords):
        x, y = chord
        if np.hypot(x[0] - x[1], y[0] - y[1]) > TRIANGLE_SIDE_LENGTH:
            success[i] = True
        if i < MAX_CHORDS_PLOT:
            line = Line2D(*chord, color=LIGHT_GREY, alpha=0.1)
            axes[0].add_line(line)
    axes[1].scatter(*midpoints, s=0.2, color=LIGHT_GREY)
    fig.suptitle('Method {}'.format(method_number))

    probability = np.sum(success) / NUM_CHORDS
    print('Method {} Probability: {}'.format(method_number, probability))
    plt.savefig('method{}.png'.format(method_number))
    plt.show()


def get_chords_from_midpoints(midpoints):
    """Return the chords with the provided midpoints."""
    chords = np.zeros((NUM_CHORDS, 2, 2))
    for i, (x0, y0) in enumerate(midpoints.T):
        m = -x0 / y0
        c = y0 + x0 ** 2 / y0
        A, B, C = m ** 2 + 1, 2 * m * c, c ** 2 - RADIUS ** 2
        d = np.sqrt(B ** 2 - 4 * A * C)
        x = np.array(((-B + d), (-B - d))) / 2 / A
        y = m * x + c
        chords[i] = (x, y)
    return chords



def generate_chords_method3():
    """Generate random chords and midpoints using method 3."""
    angles = np.random.random(NUM_CHORDS) * TWO_PI
    radii = np.sqrt(np.random.random(NUM_CHORDS)) * RADIUS
    midpoints = np.array((radii * np.cos(angles), radii * np.sin(angles)))
    chords = get_chords_from_midpoints(midpoints)
    return chords, midpoints

def plot_chords(method_number):
    # Plot the chords and their midpoints based on the selected method.
    if method_number == 1:
        chords, midpoints = generate_chords_method1()
    elif method_number == 2:
        chords, midpoints = generate_chords_method2()
    elif method_number == 3:
        chords, midpoints = generate_chords_method3()

    # Keep track of chords longer than the threshold
    success = [False] * NUM_CHORDS

    fig, axes = prepare_axes()
    for i, chord in enumerate(chords):
        x, y = chord
        if np.hypot(x[0] - x[1], y[0] - y[1]) > TRIANGLE_SIDE_LENGTH:
            success[i] = True
        if i < MAX_CHORDS_PLOT:
            line = Line2D(*chord, color=LIGHT_GREY, alpha=0.1)
            axes[0].add_line(line)
    axes[1].scatter(*midpoints, s=0.2, color=LIGHT_GREY)
    fig.suptitle('Method {}'.format(method_number))

    probability = np.sum(success) / NUM_CHORDS
    print('Method {} Probability: {}'.format(method_number, probability))
    plt.savefig('method{}.png'.format(method_number))
    plt.show()

plot_chords(3)

