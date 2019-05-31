#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:45:21 2019

@author: benjaminforleo
"""

# %%
import numpy as np
import pandas as pd
import os

directory = "/Users/benjaminforleo/Box/spring_project/russian_troll_tweets_538/"

files = os.listdir(directory)

files = [i for i in files if i.endswith('.csv')]

# %%
df = pd.DataFrame()

for file in files:
    temp_df = pd.read_csv(directory + file, sep = ",", low_memory = False)
    
    df = pd.concat([df, temp_df])
    
# count how many tweets per handle
counts_by_author = df.groupby("author")[['content']].count().sort_values(by = 'content',
                                                                         ascending = False).reset_index()

df.to_pickle("labeled_tweets.pkl")
