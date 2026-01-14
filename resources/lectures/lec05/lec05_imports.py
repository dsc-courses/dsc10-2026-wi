import numpy as np
import babypandas as bpd

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

np.set_printoptions(threshold=20, precision=2, suppress=True)
import pandas as pd
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

from IPython.display import display, IFrame, YouTubeVideo

def show_grouping_animation():
    src = "https://docs.google.com/presentation/d/1IBMwlqBtnD-Ml1Zhmqs6pnYV6jcYayr3VGFqN9Dg3xk/embed?start=false&loop=false&delayms=60000&rm=minimal"
    width = 960
    height = 509
    display(IFrame(src, width, height))
