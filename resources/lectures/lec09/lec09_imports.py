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

from IPython.display import display, IFrame

def merging_animation():
    src="https://docs.google.com/presentation/d/1d0G-_P6pLWK83wW3wPetGfzLADRqxO3jO0thK7lhtSE/embed?start=false&loop=false&delayms=3000&rm=minimal"
    width=825
    height=500
    display(IFrame(src, width, height))


def concept_check():
    src="https://docs.google.com/presentation/d/1V0d5kNVWmalLY0SkzZzKDDc_3CDZSE5m6Av0gC-PfJo/embed?start=false&loop=false&delayms=3000&rm=minimal"
    width=825
    height=500
    display(IFrame(src, width, height))


