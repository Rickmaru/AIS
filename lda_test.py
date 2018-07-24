#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

import csv
from random import random
from janome.tokenizer import Tokenizer
import gensim
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
import matplotlib.pyplot as plt
import numpy as np
from gensim.models import LsiModel
import re
import copy

extd =re.compile('".+?"')

def p_select(epsilon):
    if epsilon > random():
        return True
    else:
        return False

ng_words =["．","*","['","']","）']" ,"いる","い","う","た","ため","する", "れる","時","し","中","れ","しよ","－","部","為","せ","さ","とき","なり"]
def judgger(tok):
    if ('名詞' in tok.part_of_speech or "動詞" in tok.part_of_speech) and "数" not in tok.part_of_speech:
        if tok.surface in ng_words:
            return False
        else:
            return True
    else:
        return False

path = "C:\\Users\\1500570\\Documents\\R\\WS\\ws_ais\\"
fn ="yoin_4_utf879.csv"
#gensimのldaを使うための一時ファイル
wn ="\\autoputto.txt"

rf = csv.reader(open(path+fn,"r+", encoding ="utf-8"))
wf =open(path+wn,"w+", encoding ="utf-8")
summary =csv.writer(open(path+"\\summary.csv", "w+", newline="", encoding ="utf-8"))

num_lines = sum(1 for line in open(path+fn, encoding ="utf-8"))
print(num_lines)
#num_lines =2420

# パラメータ！
"""
jud_fieldN =5
jud_fieldC="死亡"
n_data =200
pro =float(n_data/num_lines)

wfn ="\\" +str(jud_fieldN) +translator.translate(jud_fieldC, dest='en').text.replace(" ","_") +"_" +str(n_data) +".csv"
wf =open(path+wfn, "w+" ,newline="")
"""
t = Tokenizer(path+"\\aisdict_simple2.csv", udic_type="simpledic", udic_enc="utf8")
counter =0
resword ="挟む"
#reswordを無効にする場合はFalse
resw_flag =False
templ = str(num_lines) +"\n"
teido =[]

for line in rf:
    #counter +=1
    source =[]
    #teido.append(line[4])
    """
    source.append(t.tokenize(str(line[0])))
    source.append(t.tokenize(str(line[1])))
    """
    source.append(t.tokenize(str(line[62])))
    source.append(t.tokenize(str(line[67])))
    source.append(t.tokenize(str(line[72])))
    source.append(t.tokenize(str(line[77])))
    if resword in (i for i in source) or resw_flag ==False:
        tmpi =0
        while tmpi < len(source):
            for token in source[tmpi]:
                if judgger(token) ==True:
                    templ +=token.surface +" "
            tmpi +=1
        templ +="\n"
wf.write(templ)


n_t =6
corpus =gensim.corpora.lowcorpus.LowCorpus(path +wn)


print("れっつごーL・D・A")
lda = LdaModel(corpus=corpus, num_topics=n_t, id2word=corpus.id2word)

"""
#コヒーレンス評価
coh =1
left =np.array([i+1 for i in range(30)])
height =np.array([])
while coh <=30:
    print("num of topics =",coh)
    lda = LdaModel(corpus=corpus, num_topics=coh, id2word=corpus.id2word)
    #hdp = gensim.models.HdpModel(corpus=corpus, id2word=corpus.id2word)
    cm = CoherenceModel(model=lda, corpus =corpus, coherence='u_mass')
    height =np.hstack((height,np.float(cm.get_coherence())))
    coh +=1
plt.plot(left, height)
plt.show()
#cm =lda.top_topics(corpus =corpus, texts =corpus, coherence ="u_mass", topn =10)
"""


#トピック間でユニークな語だけを表示
wl =[]
for topic in lda.show_topics(-1, num_words =50):
    tmp =[]
    for words in extd.finditer(topic[1]):
        #print(words.group().replace('"',''))
        tmp.append(words.group().replace('"',''))
    wl.append(tmp)
it =0
while it <n_t:
    it2 =0
    aite =[]
    while it2 <n_t:
        if it2 !=it:
            aite +=wl[it2]
        else:
            pass
        it2 +=1
    print(set(wl[it]).difference(set(aite)))
    it +=1

"""
for topic in hdp.show_topics(-1):
    print(topic)
"""
#hdp =hdp.suggested_lda_model()
"""
for topic in hdp.print_topics(num_topics=20, num_words=10):
    print(topic)
"""
"""
#ドキュメント-トピック分布の結果を出力
tn =0
print("len", len(teido))
for topics_per_document in lda[corpus]:
    tmpy =[0 for i in range(n_t)]
    tmpy.append(teido[tn])
    for tm in topics_per_document:
        tmpy[tm[0]] =tm[1]
    #print(tmpy)
    summary.writerow(tmpy)
    tn +=1
"""
print("end")
