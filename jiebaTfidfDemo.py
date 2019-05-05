# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import jieba
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
jieba.set_dictionary('dict.txt.big')

corpus = []
with open("lyrics/別讓我走遠.txt", "r", encoding = 'utf8') as f:
    for line in f:
        corpus.append("".join(jieba.cut(line, cut_all = False)))

#frquence matrix        
vactorizer = CountVectorizer()

#a[i][j]: indicate the frquence of term j at document i
freq_matrix = vactorizer.fit_transform(corpus)
transformer = TfidfTransformer()

#caculate TF-IDF
tfidf = transformer.fit_transform(freq_matrix)

#get keyword
words = vactorizer.get_feature_name()

#tfidf matrix
weight = tfidf.toarrary()

print(tfidf.shape)

keyword_index = np.squeeze(np.asarray(np.argmax(weight, axis = 1)))
for i in range(len(weight)):
    print(f"Keyword: {0}, weighting: {1}".format(words[keyword_index[i]], weight[i][keyword_index[i]]))

        