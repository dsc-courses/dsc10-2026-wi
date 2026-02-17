import numpy as np
import babypandas as bpd
import pandas as pd
from scipy import stats

# +
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')
plt.rcParams.update({
    'figure.figsize': (10, 5),
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'axes.labelweight': 'bold',
    'axes.linewidth': 1.5,
    'grid.color': '#999999',
    'grid.alpha': 0.6,

    # Make all text bold
    'font.weight': 'bold',
    'axes.labelweight': 'bold',
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'xtick.major.width': 1.2,
    'ytick.major.width': 1.2,
    'xtick.color': 'black',
    'ytick.color': 'black',
    'legend.fontsize': 11,
    'legend.title_fontsize': 12,
})

green = (0.0, 0.6196078431372549, 0.45098039215686275)
orange = (0.8352941176470589, 0.3686274509803922, 0.0)
gold = (0.9411764705882353, 0.8941176470588236, 0.25882352941176473)
pink = (0.8, 0.4745098039215686, 0.6549019607843137)
# -

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

# Animations
import time
from IPython.display import display, HTML, IFrame, clear_output
import ipywidgets as widgets

import warnings
warnings.filterwarnings('ignore')

def normal_curve(x, mu=0, sigma=1):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp((- (x - mu) ** 2) / (2 * sigma ** 2))

def draw_normal_curve(mu, sigma):
    plt.figure(figsize=(10, 5))
    norm_x = np.linspace(7, 20)
    norm_y = normal_curve(norm_x, mu, sigma)
    plt.plot(norm_x, norm_y, color='black', linestyle='--', linewidth=4)
    plt.title('Distribution of the Sample Mean (via the CLT)')
    plt.xlim(7, 20);


def normal_area(a, b, bars=False, title=None):
    x = np.linspace(-4, 4)
    y = normal_curve(x)
    ix = (x >= a) & (x <= b)
    plt.plot(x, y, color='black')
    plt.fill_between(x[ix], y[ix], color='#8f6100')
    if bars:
        plt.axvline(a, color='grey')
        plt.axvline(b, color='grey')
    if title:
        plt.title(title)
    else:
        plt.title(f'Area between {np.round(a, 2)} and {np.round(b, 2)}')
    plt.show()

def area_within(z):
    title = f'Proportion of values within {z} SDs of the mean: {np.round(stats.norm.cdf(z) - stats.norm.cdf(-z), 4)}'
    normal_area(-z, z, title=title)   

def show_clt_slides():
    src = "https://docs.google.com/presentation/d/1_CjPpUgqENmW8YgN3YUNkJckh9LyAtqu4UJR7FA_eE8/embed?start=false&loop=false&delayms=3000&rm=minimal"
    width = 960
    height = 509
    display(IFrame(src, width, height))

def estimate_z():
    z = widgets.FloatSlider(value=2, min=0,max=4,step=0.05, description='z')
    ui = widgets.HBox([z])
    out = widgets.interactive_output(area_within, {'z': z})
    display(ui, out)

def plot_many_distributions(sample_sizes, sample_means):
    bins = np.arange(5, 30, 0.5)
    for size in sample_sizes:
        bpd.DataFrame().assign(data=sample_means[size]).plot(kind='hist', bins=bins, density=True, ec='w', title=f'Distribution of the Sample Mean for Samples of Size {size}', figsize=(8, 4), legend=False)
        plt.show();
        time.sleep(1.5)
        if size != sample_sizes[-1]:
            clear_output()
