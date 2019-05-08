# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:58:30 2019

@author: BensonHsieh
"""

from os import listdir
from os.path import join
import jieba.analyse

files = listdir("lyrics")

for file in files:    
    with open(join("lyrics", file), "rb") as f:    
        tags = jieba.analyse.extract_tags(f.read(), 10)
        print(file + ": " + ", ".join(tags))