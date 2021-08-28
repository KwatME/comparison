from kwat.gmt import read
from kwat.path import list_directory


def read_set():

    return read(list_directory("../input/set/", ke_=(r".gmt$", r".tsv$")))
