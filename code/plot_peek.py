from kwat.plot import plot_point
from numpy import arange, where


def plot_peek(se, la_, pa):

    da = se.dropna().sort_values().to_frame()

    nu_ = da.values[:, 0]

    da.loc[:, "Rank"] = arange(nu_.size)

    da.loc[:, "Size"] = 2

    da.loc[:, "Color"] = where(nu_ < 0, "#0088ff", "#ff1968")

    da.loc[:, "Score"] = nu_.abs()

    da.loc[:, "Opacity"] = 0.48

    an_ = [ro in la_ for ro in da.index.values]

    da.loc[:, "Annotate"] = an_

    da.loc[an_, ["Size", "Color", "Opacity"]] = [8, "#20d9ba", 1]

    plot_point(da, title="Peek", pa="{}peek.html".format(pa))
