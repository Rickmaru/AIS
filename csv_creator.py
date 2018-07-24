#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

import csv
from random import random
from googletrans import Translator

path = "C:\\Users\\1500570\\Documents\\R\\WS\\ws_ais"
fn ="\\SaigaiJouhou_shibou.csv"

#unko =open(path+"\\骨折_300_1.arff","w+",newline="",encoding ="utf-8")
rf = csv.reader(open(path+fn,"r+"))
#rf2 = csv.reader(open(path+fn,"r+"))

def p_select(epsilon):
    if epsilon > random():
        return True
    else:
        return False

num_lines = sum(1 for line in open(path+fn))
translator =Translator()

# パラメータ！
jud_fieldN =5
jud_fieldC="死亡"
n_data =200
pro =float(n_data/num_lines)

wfn ="\\" +str(jud_fieldN) +translator.translate(jud_fieldC, dest='en').text.replace(" ","_") +"_" +str(n_data) +".csv"
wf =open(path+wfn, "w+" ,newline="")

counter =0
for line in rf:
    if p_select(pro) ==True:
        mtmp =line[57] +line[58] +"\n"
        wf.write(mtmp)

print("end")
