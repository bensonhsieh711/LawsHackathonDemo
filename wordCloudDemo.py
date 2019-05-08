# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:11:21 2019

@author: BensonHsieh
"""

import matplotlib.pyplot as plt
import jieba.analyse
from wordcloud import WordCloud

jieba.set_dictionary("dict.txt.big")
_stopwords = {}.fromkeys(["沒有", "一個", "什麼", "那個"])


def generate_wordcloud(keywords, stopwords, file_path):
    wc = WordCloud(font_path = 'msyh.ttf', background_color = "white", max_words = 2000, stopwords = _stopwords)
    
    #wc.generate(keywords)
    wc.generate_from_frequencies(keywords)
    plt.imshow(wc)
    plt.axis("off")
    plt.figure(figsize = (10, 6), dpi = 100)
    plt.show()
    wc.to_file(file_path)
    
def get_keywords(file_path, topN):
    keywords = {}
    with open(file_path, "r", encoding="utf8") as f:
        tags = jieba.analyse.extract_tags(f.read(), topK = topN, withWeight = True)
        for tag, weight in tags:
            keywords[tag] = weight
    return keywords

_keywords = get_keywords("lyrics/告白氣球.txt", 10)
#_keywords = get_keywords("lyrics/別讓我走遠.txt", 10)        
print(_keywords)
generate_wordcloud(_keywords, _stopwords, "lyrics/WordCloudDemo.jpg")