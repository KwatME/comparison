from os.path import splitext

from kwat.gmt import read
from kwat.path import list_directory


def read_set():

    return read(
        [
            pa
            for pa in list_directory("../input/set/")
            if splitext(pa)[1] in [".gmt", ".tsv"]
        ]
    )
