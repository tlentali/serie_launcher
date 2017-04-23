#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import pandas as pd
import numpy as np
import webbrowser

df = pd.read_csv('saison_episode.csv')
url = "http://onwatchseries.to/episode/friends_s" + str(df["saison"].iloc[0]) \
      + "_e" + str(df["episode"].iloc[0]) + ".html"

# open in a new tab, if possible
new = 2

# open a public URL, in this case, the webbrowser docs
webbrowser.open(url, new=new)

df["episode"].iloc[0] += 1
if df["episode"].iloc[0] > 25:
    df["episode"].iloc[0] = 1
    df["saison"].iloc[0] += 1

df = df[["episode", "saison"]]
df.to_csv('saison_episode.csv', index=False)
