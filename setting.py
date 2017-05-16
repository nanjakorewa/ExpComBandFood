#!/usr/bin/env python
# -*- coding: utf-8 -*-
import warnings, os, sys
"""
    システム
"""
API_FILE = "api_key/api_openml.txt" # openml API authentication
PYTHON_VER = int(sys.version[0]) # item/teritem等バージョンごとの確認のため


"""
    探索に利用するアルゴリズム名
"""
# normal
ALG_RAND = "random"
# bandit
ALG_EPSILON = "epsilon"
ALG_COMBAND = "comband"
ALG_COMBAND_IP1 = "ip1"
# algorithm list
ALG_LIST = [ALG_RAND, ALG_COMBAND, ALG_EPSILON, ALG_COMBAND_IP1]

"""
    タスク
"""
FIVE_STAGE_EVALUATION = "5stage evaluation"
# metric list
METRIC_LIST = [FIVE_STAGE_EVALUATION]

"""
    出力先
"""
# ディレクトリ名
DIR_DATA = "data/"
DIR_FIG = "fig/"
DIR_LOG = "log/"
DIR_REPORT = "report/"
# デフォルトの区切り文字
DEFAULT_DELIMINATOR = "\t"

"""
    スコア計算関係
"""
CV_TEST_SIZE = 0.3 # Train/Test split size

"""
    Dict
    パイプラインを管理するdict関係
"""
PARAM = "param" # パラメータのキー
MODEL_NAME = "name" # モデル名のキー
NONE_NAME = "None" # 何もしない時のデフォルト名

"""
    エラー設定・ユーザー定義エラー
"""
warnings.simplefilter("ignore") # Avoid DeprecationWarning

class Error(Exception):
    pass

class DatasetNameError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        print(expression, message)
