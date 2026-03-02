import numpy as np
import babypandas as bpd
import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

from IPython import get_ipython
get_ipython().run_line_magic('config', "InlineBackend.figure_formats = ['svg']")

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

from IPython.display import display, IFrame, HTML

def show_permutation_testing_intro():
    src="https://docs.google.com/presentation/d/1_bT-CPK7u8bItbDmTie1-IBgMp7k3e9YMA_v7ICequM/embed?start=false&loop=false&delayms=60000&rm=minimal"
    width = 965
    height = 635
    display(IFrame(src, width, height))

def show_permutation_testing_summary():
    src = "https://docs.google.com/presentation/d/13grhudxd3_KBmY26tGimeYWYZNCo0BU-Nz4LsUyOI_M/embed?start=false&loop=false&delayms=60000&rm=minimal"
    width = 960
    height = 569
    display(IFrame(src, width, height))
