import numpy as np
import babypandas as bpd
import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')
plt.rcParams['figure.figsize'] = (10, 5)

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

# Animations
import ipywidgets as widgets
from IPython.display import display, HTML

def normal_curve(x, mu=0, sigma=1):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp((- (x - mu) ** 2) / (2 * sigma ** 2))

def show_many_normal_distributions():
    plt.figure(figsize=(10, 5))
    x = np.linspace(-40, 40, 10000)
    # color-blind-safe palette
    pairs = [
        (0, 1, '#D81B60'),   # red
        (10, 1, '#1E88E5'),  # blue
        (-15, 4, '#FFC107'), # orange
        (20, 0.5, '#004D40') # green
    ]

    for pair in pairs:
        y = normal_curve(x, mu=pair[0], sigma=pair[1])
        plt.plot(x, y, color=pair[2], linewidth=3, label=f'Normal(mean={pair[0]}, SD={pair[1]})')

    plt.xlim(-40, 40)
    plt.ylim(0, 1)
    plt.title('Normal Distributions with Different Means and Standard Deviations')
    plt.legend();

def normal_area(a, b, bars=False):
    x = np.linspace(-4, 4, 1000)
    y = normal_curve(x)
    ix = (x >= a) & (x <= b)
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, color='black')
    plt.fill_between(x[ix], y[ix], color='gold')
    if bars:
        plt.axvline(a, color='red')
        plt.axvline(b, color='red')
    plt.title(f'Area between {np.round(a, 2)} and {np.round(b, 2)}')
    plt.show()

def sliders():
    a = widgets.FloatSlider(value=0, min=-4,max=3,step=0.25, description='a')
    b = widgets.FloatSlider(value=1, min=-4,max=4,step=0.25, description='b')
    bars = widgets.Checkbox(value=False, description='bars')
    ui = widgets.HBox([a, b, bars])
    out = widgets.interactive_output(normal_area, {'a': a, 'b': b, 'bars': bars})
    display(ui, out)