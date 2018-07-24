#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

import os
import csv
import janome
from janome.tokenizer import Tokenizer
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import gensim
import numpy as np
import copy
import gensim.models.poincare as poin
import gensim.viz.poincare as pviz
import plotly

path = "C:\\Users\\1500570\\Documents\\R\\WS\\ws_ais"
t = Tokenizer()
rf = csv.reader(open(path+"\\SaigaiJouhou_title.csv","r+"))
rf2 = csv.reader(open(path+"\\SaigaiJouhou_title.csv","r+"))
#wf = csv.writer(open(path+"\\test.csv","w+", newline=""), delimiter=" ")
resword ="ダミー"

ff = True
tete = []
countn =0
for line in rf:
    if countn %500 ==0:
        print("第一カウント",countn)
    if ff == True:
        ff = False
        continue
    templ = []
    temp = t.tokenize(str(line))
    for token in temp:
        if '名詞' in token.part_of_speech and '数' not in token.part_of_speech and token.base_form !="*" and token.base_form !="['" and token.base_form !="']":
            templ.append(token.base_form)
        elif "動詞" in token.part_of_speech and token.base_form !="*" and token.base_form !="['" and token.base_form !="']":
            templ.append(token.base_form)
    #wf.writerow(templ)
    #del(templ[0])
    #del(templ[-1])
    if resword in templ:
        tete.extend(templ)
    else:
        tete.extend(templ)
    #print(templ)
    countn +=1
#print(set(tete))
wordlist =list(set(tete))
word_matrix =np.zeros((len(wordlist),len(wordlist)))
wl =len(wordlist)
hindo =np.array([0 for un in range(wl)])

ff2 = True
tete2 = []
countn2 =0
for line2 in rf2:
    if countn2 %10 ==0:
        print("第二カウント", countn2)
    if ff2 == True:
        ff2 = False
        continue
    templ2 = []
    temp2 = t.tokenize(str(line2))
    for token2 in temp2:
        try:
            if '名詞' in token2.part_of_speech and '数' not in token2.part_of_speech and token2.base_form !="*" and token2.base_form !="['" and token2.base_form !="']":
                templ2.append(token2.base_form)
                hindo[wordlist.index(token2.base_form)] +=1
            elif "動詞" in token2.part_of_speech and token2.base_form !="*" and token2.base_form !="['" and token2.base_form !="']":
                templ2.append(token.base_form)
                hindo[wordlist.index(token2.base_form)] +=1
        except:
            pass
    #wf.writerow(templ)
    #del(templ2[0])
    #del(templ2[-1])
    if resword in templ2:
        pp =0
        while pp <len(templ2) -1:
            ii =pp +1
            try:
                px =wordlist.index(templ2[pp])
            except:
                pp +=1
                continue
            while ii <len(templ2):
                try:
                    ix =wordlist.index(templ2[ii])
                    word_matrix[px,ix] +=1
                    word_matrix[ix,px] +=1
                except:
                    pass
                ii +=1
            pp +=1
    else:
        pp =0
        while pp <len(templ2) -1:
            ii =pp +1
            try:
                px =wordlist.index(templ2[pp])
            except:
                pp +=1
                continue
            while ii <len(templ2):
                try:
                    ix =wordlist.index(templ2[ii])
                    word_matrix[px,ix] +=1
                    word_matrix[ix,px] +=1
                except:
                    pass
                ii +=1
            pp +=1
    countn2 +=1

honi =wordlist.index("転倒")
pm =[]
major_words =[]
honp =0
while honp <wl:
    if honp %100 ==0:
        print("第三カウント", honp, "/", str(wl))
    if word_matrix[honi,honp] >30 and hindo[honi] >hindo[honp]:
        pm.append((wordlist[honi],wordlist[honp]))
        if hindo[honi] >40:
            major_words.append(wordlist[honi])
        #print('パターン１')
    elif word_matrix[honi,honp] >30 and hindo[honi] <hindo[honp]:
        pm.append((wordlist[honp],wordlist[honi]))
        if hindo[honp] >40:
            major_words.append(wordlist[honp])
        #print('パターン２')
    elif word_matrix[honi,honp] >30 and word_matrix[honi,honp] ==word_matrix[honp,honi]:
        pm.append((wordlist[honi],wordlist[honp]))
        pm.append((wordlist[honp],wordlist[honi]))
        print("パターン3")
    """
    if word_matrix[honi,honp] >word_matrix[honp,honi]:
        pm.append((wordlist[honi],wordlist[honp]))
        print('パターン１')
    elif word_matrix[honi,honp] <word_matrix[honp,honi]:
        pm.append((wordlist[honp],wordlist[honi]))
        print('パターン２')
    elif word_matrix[honi,honp] !=0 and word_matrix[honi,honp] ==word_matrix[honp,honi]:
        pm.append((wordlist[honi],wordlist[honp]))
        pm.append((wordlist[honp],wordlist[honi]))
    """
    honp +=1

plotly.offline.init_notebook_mode(connected=False)
vizm =poin.PoincareModel(pm, size =2,negative=5)
vizm.train(epochs =50)
plotly.offline.iplot(pviz.poincare_2d_visualization(model =vizm, tree =set(pm), figure_title ="test01", num_nodes=5, show_node_labels =vizm.kv.vocab.keys()))

"""
titi = []
for ten in tete:
    temtem = ""
    for inko in ten:
        temtem = temtem + inko + " "
    titi.append(temtem)

for li in titi:
    print(li)

count_vectorizer = CountVectorizer(max_features=3000)
tf = count_vectorizer.fit_transform(titi)
features = count_vectorizer.get_feature_names()

# print(features)
wfea = csv.writer(open(path+"\\features.csv","w+", newline=""))
wfea.writerow(features)

tfidf_vect = TfidfVectorizer(max_features=3000, norm='l2')
X = tfidf_vect.fit_transform(titi)

# wf3 = csv.writer(open(path+"\\result.csv","w+", newline=""), delimiter=" ")

numpy.savetxt(path+"\\result.csv",X.toarray(),delimiter=",")

# print(features)

reaf = csv.reader(open(path+"\\result.csv","r+"))

mfcoss = []

for line in reaf:
    mfcoss.append(line)

tfidf_matrix = []

def calc_coss(roww1,roww2):
    r1_norm = 0
    r2_norm = 0
    inn = 0
    t1 = 0
    while t1 < len(roww1):
        r1_norm += float(roww1[t1])**2
        r2_norm += float(roww2[t1])**2
        inn += float(roww1[t1])*float(roww2[t1])
        t1 += 1
    return inn/(numpy.sqrt(r1_norm)*numpy.sqrt(r2_norm))

i1 = 0
while i1 < len(mfcoss):
    i2 = 0
    temp = []
    while i2 < len(mfcoss):
        temp.append(calc_coss(mfcoss[i1], mfcoss[i2]))
        i2 += 1
    tfidf_matrix.append(temp)
    i1 += 1

# print(tfidf_matrix)

tfw = csv.writer(open(path+"\\tfidf_res.csv","w+", newline=""))
for line in tfidf_matrix:
    tfw.writerow(line)

print("end")

"""

"""
print(copus)
copus = numpy.array(copus)
# print(copus)
print(len(copus))
"""