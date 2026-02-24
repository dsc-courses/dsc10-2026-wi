import numpy as np
import babypandas as bpd
import pandas as pd

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

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

def draw_cutoff(results):
    cutoff = np.percentile(results, 5)
    
    ax = bpd.DataFrame().assign(results=results).plot(kind='hist', bins=np.arange(160, 240, 4), 
                                             density=True, figsize=(10, 5),
                                             title='Empirical Distribution of the Number of Heads in 400 Flips of a Fair Coin')
    for bar in ax.containers[0]:
        x = bar.get_x() + 0.5 * bar.get_width()
        if x < cutoff:
            bar.set_color('#009e73')
    plt.annotate('likely biased\ntowards tails', (160, 0.007), size=16, color='#009e73', weight='bold')
    plt.annotate('likely fair', (225, 0.008), size=16, color='#0072b2', weight='bold');
# -


