#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setting import *

import numpy as np
import random
from datetime import datetime
import openml

from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.datasets.mldata import fetch_mldata

# ランダムな整数を取得
def randint(min_n=0, max_n=1000):
    return np.random.randint(min_n, max_n)

# レポート作成用関数
def get_id(idtype=0, prefix="", suffix=""):
    pattern = '%Y%m%d_%H%M%S_'
    tdatetime = datetime.now()

    if idtype==0:
        pattern = '%Y%m%d_%H%M%S_'
    elif idtype==1:
        pattern = '%m%d_%H%M%S_'

    id_str = tdatetime.strftime(pattern) + str(tdatetime.microsecond//1000)
    return prefix + id_str + suffix

# weighted random choice
def weighted_random_choice(weight, itemset=None):
    n_items = np.array(weight).shape[0]
    population = np.arange(n_items) if itemset is None else itemset
    distribution = (1.0/np.sum(weight))*np.array(weight)

    return np.random.choice(population, p=distribution)

# {0, 1}^d vectorを取得
class VectorDecoder:
    def __init__(self, pipeline):
        self.algnames = sum(pipeline, [])
        self.algInEachSteps = [len(step) for step in pipeline]
        self.d = len(self.algnames)
        self.noneIndex = [i for i, x in enumerate(self.algnames) if x==NONE_NAME]
        print("EXISTING ALGORITHMS:", self.algnames)

    def decode(self, alglist):
        temp = np.zeros(self.d)

        for i, algname_i in enumerate(alglist):
            if algname_i==NONE_NAME:
                # (None in i step) = 1
                temp[self.noneIndex[i]] = 1
            else:
                # (algname in algnames) = 1
                temp[self.algnames.index(algname_i)] = 1

        return temp