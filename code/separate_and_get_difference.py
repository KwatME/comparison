from kwat.array_array import get_sum_difference
from kwat.function import separate_and_apply


def separate_and_get_difference(bo_, ar):

    return separate_and_apply(bo_, ar, get_sum_difference)
