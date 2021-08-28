from pandas import concat, read_csv


def read_statistic(pa, co, na):

    return concat(
        [
            read_csv(
                "{}compare_{}/{}/{}/statistic.tsv".format(pa, st, co, na),
                sep="\t",
                index_col=0,
            )
            for st in ["feature", "set"]
        ]
    )
