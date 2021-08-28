import itertools
import os
import re

import kwat
import numpy as np
import pandas as pd
from plot_peek import plot_peek
from read_set import read_set
from read_statistic import read_statistic
from separate_and_get_difference import separate_and_get_difference

SETTING = kwat.json.read("setting.json")

PAR = kwat.project.get_root("setting.json")

PAI = "{}/input/".format(PAR)

PAC = "{}/code/".format(PAR)

PAO = "{}/output/".format(PAR)
