#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

import csv
from random import random
from janome.tokenizer import Tokenizer
import gensim
import re
import pandas as pd
import numpy as np

df=pd.DataFrame([[1,2,3],[4,5,6],["asa","usa","isa"]], columns=["a","b","c"])
print(np.array(df.b))
print(df[df["c" ]==3].iat[0,1])

unko =re.compile(".+うんち.+")
t = Tokenizer()
counter =0
resword ="挟む"
resw_flag =True

#ng_words =["けど","あ"]
tmp = t.tokenize("食べ放題できたぜat東京駅")
sen ="これはすごくうんこですね"
sen2 ="これはすごくうんちですね"

print(unko.match(sen))
print(unko.match(sen2))
print(bool(unko.match(sen)))
print(bool(unko.match(sen2)))

for line in tmp:
    print(line.part_of_speech.split(",")[1])
    """
    print(type(line.surface))
    if line.surface in ng_words:
        print("NG")
    """



"""
for line in rf:
    #counter +=1
    temp1 = t.tokenize(str(line[57]))
    temp2 = t.tokenize(str(line[58]))
    if resword in temp1 or resword in temp2 or resw_flag ==False:
    for token1 in temp1:
        if judgger(token1) ==True:
            templ +=token1.base_form +" "
    for token2 in temp2:
        if judgger(token2) ==True:
            templ +=token2.base_form +" "
    templ +="\n"
    #if counter ==100:
    #    break
"""