#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

import csv
from janome.tokenizer import Tokenizer
import numpy as np
import pandas as pd

path = "C:\\Users\\1500570\\Documents\\R\\WS\\ws_ais"
fn ="\\5death_200.csv"
unko =open(path+"\\5death_200.arff","w+",newline="",encoding ="utf-8")

rf = csv.reader(open(path+fn,"r+"))
rf2 = csv.reader(open(path+fn,"r+"))
#wf =open(path+"\\output0515_300_2.csv","w+", newline="\n")
#wf = csv.writer(open(path+"\\test.csv","w+", newline=""), delimiter=" ")
resword ="墜落"
resw_flag =False
field_list =[1,2,3]

wt =[]
wc =[]
for i in field_list:
    for line in rf:
        tmp1 =[0 for i in range(len(wt))]
        if line[i] not in wt:
            wt.append(line[i])
            tmp1.append(1)
        else:
            tmp1[wt.index(line[i])] =1
        wc.append(tmp1)
wt =pd.DataFrame([wt])
for line in wc:



ff = True
tete = []
countn =0
# 語彙を抽出するループ。reswordに注意。
for line in rf:
    if countn %500 ==0:
        print("第一カウント",countn)
    """
    #最初の一行飛ばす
    if ff == True:
        ff = False
        continue
    """
    templ = []
    temp = t.tokenize(str(line))
    for token in temp:
        if judgger(token) ==True:
            templ.append(token.base_form)
    #wf.writerow(templ)
    #del(templ[0])
    #del(templ[-1])
    #tete.extend(templ)
    if resword in templ or resw_flag ==False:
        tete.extend(templ)
    else:
        pass
    #print(templ)
    countn +=1

#wtに指定条件に合格した全語彙が収録される
wt = ["原文"]
wt.extend(list(set(tete)))
wt =np.array(wt)
wl =len(wt)
print(wl)
hindo =np.array([0 for un in range(wl)])
ff2 = True
tete2 = []
countn2 =0
# wtは文書×全語彙超のbow。一行のテンポラリ配列はtmtt。
for line2 in rf2:
    if countn2 %10 ==0:
        print("第二カウント", countn2)
    """
    if ff2 == True:
        ff2 = False
        continue
    """
    templ2 = []
    temp2 = t.tokenize(str(line2))
    for token2 in temp2:
        try:
            if judgger(token2) ==True:
                templ2.append(token2.base_form)
                #hindo[int(np.where(wt ==token2.base_form)[0])] +=1
        except:
            pass
    #wf.writerow(templ)
    #del(templ2[0])
    #del(templ2[-1])
    if resword in templ2 or resw_flag ==False:
        pp =0
        tmtt =np.zeros(wl)
        if ff2 ==True:
            ff2 =False
            risuto =list(wt)
        else:
            risuto =list(wt[0])
        while pp <len(templ2):
            px =risuto.index(templ2[pp])
            tmtt[px] =1
            pp +=1
        wt =np.vstack((wt,tmtt))
    countn2 +=1

headder ="@RELATION werewolf_divine\n"
deeta ="@DATA\n"
#unko =csv.writer(open(path+"\\gbregnrenv.csv","w+",newline=""))
oi =1
ooff =True
translator = Translator()
cholist =[]
tmlen =len(wt)
while oi <tmlen:
    if oi %10 ==0:
        print(oi, "/", len(wt))
    panchi =1
    while panchi <len(wt[0]):
        if ooff ==True:
            #tmen =translator.translate(wt[0,panchi], dest='en').text.replace(" ","_")
            tmen =wt[0,panchi]
            """
            jt =False
            while jt ==False:
                if tmen in cholist:
                    tmen +="2"
                else:
                    jt =True
            cholist.append(tmen)
            """
            headder =headder +"@ATTRIBUTE " +tmen +" {0,1}\n"
            #wf.write(wt[0,panchi]+","+tmen+"\n")
        else:
            pass
        if wt[oi,panchi] =="0.0":
            deeta =deeta +"0"
        else:
            deeta =deeta +"1"
        panchi +=1
        if panchi ==len(wt[0]):
            deeta +="\n"
            ooff =False
        else:
            deeta +=","
    oi +=1

unko.write(headder)
unko.write(deeta)
unko.close()
print(wt[1:,:])
print(wt[1:,0])
"""
for fagw in wt:
    unko.writerow(fagw)
"""
print("end")