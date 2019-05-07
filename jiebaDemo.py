# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:58:09 2019

@author: BensonHsieh
"""

import jieba

seg_list = jieba.cut("我來到公司泡咖啡寫程式", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我來到公司泡咖啡寫程式", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("賣溝阿內打我媽媽")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明喜歡加班，但是都在打switch")  # 搜索引擎模式
print(", ".join(seg_list))