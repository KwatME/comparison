from pandas import concat, read_csv


def read_statistic(co, na):

    return concat(
        [
            read_csv(
                "../output/compare_{}/{}/{}/statistic.tsv".format(st, co, na),
                sep="\t",
                index_col=0,
            )
            for st in ["feature", "set"]
        ]
    )
