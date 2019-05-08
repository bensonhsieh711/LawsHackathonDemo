# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:54:09 2019

@author: BensonHsieh
"""

import jieba.analyse

with open("lyrics/告白氣球.txt", "r", encoding = 'utf8') as f:
#with open("lyrics/別讓我走遠.txt", "r", encoding = 'utf8') as f:
    for line in f:
        tags = jieba.analyse.extract_tags(line, topK = 1, withWeight = True)
        for tag, weight in tags:
            print(tag + "," + str(weight))