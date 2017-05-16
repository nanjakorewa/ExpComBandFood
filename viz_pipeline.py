#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import *
from setting import *

import os
import argparse
from graphviz import Digraph
import matplotlib.pyplot as plt

from food.experimental_settings import *

# divede the strings by br
def _divide_str(string, div=10):
    string = string.split(".")[-1]
    
    if len(string)<div:
        return string
    else:
        return string[:div]+"\n"+string[div:]

def main(exp_index, filename):
    # パイプラインの設定
    pipeline = get_exp_setting(exp_index)
    filename = filename

    # 初期化
    G = None
    G = Digraph(format='png')
    G.attr('node', shape='box', size='16,6')

    # ノードの追加
    G.node("X", "X")
    G.node("y", "y")
    G.node("f", "f")
    G.edge("y", "f", len='0.20')

    # 辺の追加
    step_num = len(pipeline)

    # 描写
    for i, step in enumerate(pipeline):
        model_name_list = pipeline[i]
        before_model_name_list = pipeline[i-1]
        
        # None の名前が重複するので番号をつける
        if NONE_NAME in model_name_list:
            model_name_list[model_name_list.index(NONE_NAME)] = NONE_NAME+str(i)

        if i == 0:
            for model_name in model_name_list:
                model_name = _divide_str(model_name)
                G.node(model_name, model_name)
                G.edge("X", model_name, len='2.00')

        elif i > 0:
            for model_name in model_name_list:
                model_name = _divide_str(model_name)
                G.node(model_name, model_name)

                # final pipeline step, add y
                if i==step_num-1:
                    G.edge(model_name, "y", len='1.00')

                # add edge from before steps
                for before_model_name in before_model_name_list:
                    before_model_name = _divide_str(before_model_name)
                    G.edge(before_model_name, model_name, len='2.00')

    # .pngで保存
    G.render(filename)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='viz exp')
    parser.add_argument('-e', dest='exp', metavar='e', type=int, default=0,
                    help='an integer for the exp-settings')
    parser.add_argument('-f', dest='filename', type=str, default=DIR_FIG+get_id(),
                    help='output file name')
    
    args = parser.parse_args()
    main(args.exp, args.filename)
    
    # remove temp file
    os.remove(args.filename)