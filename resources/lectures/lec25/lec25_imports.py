import numpy as np
import babypandas as bpd
import pandas as pd
from scipy import stats

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-colorblind')

from IPython import get_ipython
get_ipython().run_line_magic('config', "InlineBackend.figure_formats = ['svg']")

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

from IPython.display import display, IFrame, HTML
from ipywidgets import widgets

green = (0.0, 0.6196078431372549, 0.45098039215686275)
orange = (0.8352941176470589, 0.3686274509803922, 0.0)
gold = (0.9411764705882353, 0.8941176470588236, 0.25882352941176473)
pink = (0.8, 0.4745098039215686, 0.6549019607843137)

def standard_units(col):
    return (col - col.mean()) / np.std(col)

def standardize(df):
    """Return a DataFrame in which all columns of df are converted to standard units."""
    df_su = bpd.DataFrame()
    for column in df.columns:
        df_su = df_su.assign(**{column + ' (su)': standard_units(df.get(column))})
    return df_su

def calculate_r(df, x, y):
    '''Returns the average value of the product of x and y, 
       when both are measured in standard units.'''
    x_su = standard_units(df.get(x))
    y_su = standard_units(df.get(y))
    return (x_su * y_su).mean()

def slope(df, x, y):
    '''Returns the slope of the regression line between columns x and y in df (in original units).'''
    r = calculate_r(df, x, y)
    return r * np.std(df.get(y)) / np.std(df.get(x))

def intercept(df, x, y):
    '''Returns the intercept of the regression line between columns x and y in df (in original units).'''
    return df.get(y).mean() - slope(df, x, y) * df.get(x).mean()

# All of the following code is for visualization.
def plot_regression_line(df, x, y, margin=.02, alpha=1, resid=False):
    '''Computes the slope and intercept of the regression line between columns x and y in df (in original units) and plots it.'''
    m = slope(df, x, y)
    b = intercept(df, x, y)
    
    df.plot(kind='scatter', x=x, y=y, s=50, figsize=(10, 5), label='original data', alpha=alpha)
    left = df.get(x).min()*(1 - margin)
    right = df.get(x).max()*(1 + margin)
    domain = np.linspace(left, right, 10)
    plt.plot(domain, m*domain + b, color=orange, label='regression line', lw=4)
    plt.suptitle(format_equation(m, b), fontsize=18)
    plt.legend();
    
    if resid:
        idx = np.random.randint(0, df.shape[0], size=50)
        for i, k in enumerate(idx):
            x = df.get('mom').iloc[k]
            y = df.get('son').iloc[k]
            p = df.get('predicted').iloc[k]
            plt.plot([x,x], [y,p], linewidth=3, color='purple', label='residuals' if i == 0 else None)
        plt.legend();
        print('Correlation:', calculate_r(df, 'mom', 'son'))

def non_linear():
    np.random.seed(23)
    x2 = bpd.DataFrame().assign(
    x=np.arange(-6, 6.1, 0.5) + np.random.normal(size=25), 
    y=np.arange(-6, 6.1, 0.5)**2 + np.random.normal(size=25)
    )
    plot_regression_line(x2, 'x', 'y')

def format_equation(m, b):
    if b > 0:
        return r'$y = %.2fx + %.2f$' % (m, b)
    elif b == 0:
        return r'$y = %.2fx' % m
    else:
        return r'$y = %.2fx %.2f$' % (m, b)

def draw_many_lines(m_boot, b_boot):
    plt.figure(figsize=(10, 5))
    x = np.arange(50, 80)
    ys = []
    for i, (m, b) in enumerate(zip(m_boot[:50], b_boot)):
        ys.append(m * x + b)
        fig = plt.plot(x, m * x + b, linewidth=1)

# Don't worry about how this code works.
def pred_interval(mom, m_boot, b_boot):
    plt.figure(figsize=(8,4))
    x = np.arange(50, 80)
    ys = []
    for i, (m, b) in enumerate(zip(m_boot[:50], b_boot)):
        ys.append(m * x + b)
        plt.plot(x, m * x + b, linewidth=1, alpha=0.5)

    boot_preds = m_boot * mom + b_boot
    l = np.percentile(boot_preds, 2.5)
    r = np.percentile(boot_preds, 97.5)
    plt.plot([mom, mom], [l, r], linewidth=5, color=gold, label='95% prediction interval')
    plt.xlim(50, 80)
    plt.ylim(62, 77)
    plt.title(f'95% prediction interval for the height of a son whose mother is \n{mom} inches tall: {[np.round(l, 3), np.round(r, 3)]}')
    plt.legend()
    plt.show()

def slider_widget(m_boot, b_boot):
    mom_slider = widgets.IntSlider(value=64, min=50, max=78, step=1, description="mom's height")
    ui = widgets.HBox([mom_slider])
    out = widgets.interactive_output(lambda mom: pred_interval(mom, m_boot, b_boot), {'mom': mom_slider})
    display(ui, out)
