import numpy as np
import babypandas as bpd
import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')
# 2026-01-11(sam): i took these out because i didn't like the way they looked
# plt.rcParams.update({
#     'figure.figsize': (10, 5),
#     'axes.titlesize': 14,
#     'axes.titleweight': 'bold',
#     'axes.labelsize': 12,
#     'axes.labelweight': 'bold',
#     'axes.linewidth': 1.5,
#     'grid.color': '#999999',
#     'grid.alpha': 0.6,

#     # Make all text bold
#     'font.weight': 'bold',
#     'axes.labelweight': 'bold',
#     'xtick.labelsize': 11,
#     'ytick.labelsize': 11,
#     'xtick.major.width': 1.2,
#     'ytick.major.width': 1.2,
#     'xtick.color': 'black',
#     'ytick.color': 'black',
#     'legend.fontsize': 11,
#     'legend.title_fontsize': 12,
# })

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

from IPython.display import display, IFrame, YouTubeVideo

def show_grouping_animation():
    src = "https://docs.google.com/presentation/d/1IBMwlqBtnD-Ml1Zhmqs6pnYV6jcYayr3VGFqN9Dg3xk/embed?start=false&loop=false&delayms=60000&rm=minimal"
    width = 960
    height = 509
    display(IFrame(src, width, height))
