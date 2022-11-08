# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os
os.chdir('/home/fzr/Downloads/')
cmd = 'ls filereport* > tmp'
os.system(cmd)

file_list = np.loadtxt('./tmp', dtype=str)
for file in np.nditer(file_list):
    print(file)

file = '~/Downloads/filereport_read_run_PRJNA111457_json.txt'
df = pd.read_json(file)
print(df.index)
print(df.columns)
for i in df.iteritems()
