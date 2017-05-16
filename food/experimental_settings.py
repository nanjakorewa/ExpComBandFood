#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setting import *

import numpy as np
import sys

from sklearn import metrics

# evaluation metric
def get_eval_metric(taskname):
    if taskname==BINARYCLASS:
        return metrics.roc_auc_score
    elif taskname==MULTICLASS_AC:
        return metrics.accuracy_score
    elif taskname==MULTICLASS_F1:
        return metrics.f1_score
    elif taskname==MULTICLASS_AP:
        return metrics.average_precision_score
    else:
        print("Warning: Use accuracy score!")
        return metrics.accuracy_score

# index -> pipeline, pipeline_dict
def get_exp_setting(index):
    return [_exp0,][index]()

# filter bandit
def _filter_pipeline(pipeline):
    return pipeline

# experimental settings
def _exp0():
    print("EXPERIMENTAL SETTINGS: 0")
    step1 = ['raw food', 'peel']
    step2 = ['diced', 'grind', 'chopped']
    step3 = ['wash', 'wash & boil']
    step4 = ['simmer', 'bake', 'gril']

    pipeline = [step1, step2, step3, step4]
    return _filter_pipeline(pipeline)
