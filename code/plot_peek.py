from kwat.plot import plot_point
from numpy import absolute, arange, where
from pandas import DataFrame


def plot_peek(se, la_, pa):

    se = se.dropna().sort_values()

    nu_ = se.values

    las_ = se.index.values

    bo_ = [la in la_ for la in las_]

    da = DataFrame(
        data={
            se.name: absolute(nu_),
            "Rank": arange(nu_.size),
            "Size": 2,
            "Color": where(nu_ < 0, "#0088ff", "#ff1968"),
            "Opacity": 0.48,
            "Annotate": bo_,
        },
        index=las_,
    )

    da.loc[bo_, ["Size", "Color", "Opacity"]] = [8, "#20d9ba", 0.8]

    plot_point(da, title="Peek", pa="{}peek.html".format(pa))
