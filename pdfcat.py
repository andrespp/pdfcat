#!/usr/bin/env python3
import pandas as pd
import subprocess
import fnmatch
import math
import os

# Settings
INPUTDIR='./data/input'
OUTPUTDIR='./data/output'

## Script

# Build dataframe
entries=[]
cols=['filename','original_page', 'new_page']

for i in os.listdir(INPUTDIR):
    if fnmatch.fnmatch(i, '*.pdf'):

        op = int(i[-8:-4])
        if op%2 == 0: # even page
            np = 1
        else: # odd page
            np = 0

        a = [INPUTDIR+'/'+i,        # filename
             op,                    # original page
             np                     # new-file-page
        ]
        entries.append(a)

df = pd.DataFrame(entries, columns=cols).sort_values(by=['original_page'])
df.reset_index(inplace=True, drop=True)

df['file_counter'] = df['original_page'].apply(lambda x: math.ceil(x/2))

print(df)

# Iterate over dataframe to generate files
for i in df['file_counter'].unique():

    # input file list
    file_list = list(df[df['file_counter']==i]['filename'])

    # build command line
    cmd = 'pdftk'.split()
    cmd = [*cmd, *file_list]
    output = OUTPUTDIR + '/' + file_list[0][:-11]
    output = output.replace(INPUTDIR,'')
    cmd = [*cmd, *f'cat output {output}{i:04d}.pdf'.split()]
    #print(f'\n{i}: {cmd}')

    # Run subprocess
    subprocess.run(['echo', *cmd])
    p = subprocess.run(cmd)
    #print(p.returncode)
