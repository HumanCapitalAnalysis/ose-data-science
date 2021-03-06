import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
from matplotlib.ticker import FixedFormatter
from matplotlib.ticker import FixedLocator


def plot_individual_specific_effects(with_parameters=None):

    fig, ax = plt.subplots()
    x = np.linspace(-5, 5, 5000)
    pdf = ss.norm.pdf(x, 0, 1)
    ax.plot(x, pdf)

    ax.set_xlabel(r"$\delta$")
    ax.set_ylabel("Density")
    x_formatter = FixedFormatter(["", "", "", 0.5, "", "", ""])
    x_locator = FixedLocator([-3, -2, -1, 0, 1, 2, 3])
    ax.xaxis.set_major_locator(x_locator)
    ax.xaxis.set_major_formatter(x_formatter)
    ax.set_xlim([-3, 3])
    ax.set_ylim([0, 0.5])
    pos = with_parameters

    if with_parameters and len(set(pos)) != 1:
        ax.axvline(x=pos[0], label="ATE", color="red")
        ax.axvline(x=pos[2], label="ATT", color="orange")
        ax.axvline(x=pos[1], label="ATC", color="green")
        ax.legend()

    elif with_parameters and len(set(pos)) == 1:
        ax.axvline(x=pos[0], linewidth=3, label="ATE = ATT = ATC", color="red")
        ax.legend()


def get_lalonde_data():

    df = pd.read_csv("../../datasets/processed/dehejia_waba/nsw_lalonde.csv")
    df = df[["treat", "re78"]].sample(frac=1)

    df["Y"] = df["re78"]
    df["Y_0"] = df.query("treat == 0")["re78"]
    df["Y_1"] = df.query("treat == 1")["re78"]

    df["D"] = 0
    df.loc[df["treat"] == 1, "D"] = 1

    return df
