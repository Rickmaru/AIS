#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

import csv

path = "C:\\Users\\1500570\\Documents\\R\\WS\\ais"
fn ="\\SaigaiJouhou.csv"
unko =open(path+"\\5_28_30_all.arff","w+",newline="",encoding ="utf-8")

rf = csv.reader(open(path+fn,"r+"))
#rf2 = csv.reader(open(path+fn,"r+"))
#wf =open(path+"\\output0515_300_2.csv","w+", newline="\n")
#wf = csv.writer(open(path+"\\test.csv","w+", newline=""), delimiter=" ")
resword ="墜落"
resw_flag =False
field_list =[5,28,30]
quo =10

wt =[]
wc =[]
ff =True
coun =0
for line in rf:
    coun +=1
    if ff ==True:
        ff =False
        continue
    elif coun %quo ==0:
        tmp1 =[0 for i in range(len(wt))]
        for i in field_list:
            if str(i)+line[i] not in wt and line[i] !="":
                wt.append(str(i)+line[i])
                tmp1.append(1)
            elif line[i] =="":
                pass
            else:
                tmp1[wt.index(str(i)+line[i])] =1
        wc.append(tmp1)
    else:
        continue
#wc =pd.DataFrame([wc])
print(wc)
#print(wc.ix[[0],[1]])
#print(wt)

headder ="@RELATION werewolf_divine\n"
deeta ="@DATA\n"
#unko =csv.writer(open(path+"\\gbregnrenv.csv","w+",newline=""))
oi =0
tmlen =len(wt)
while oi <tmlen:
    if oi %10 ==0:
        print(oi, "/", tmlen)
    tmen =wt[oi]
    headder =headder +"@ATTRIBUTE " +tmen +" {0,1}\n"
    oi +=1

oj =0
while oj <len(wc):
    if oj %100 ==0:
        print(oj,"/",len(wc))
    ok =0
    while ok <tmlen:
        if ok <len(wc[oj]):
            deeta +=str(wc[oj][ok])
        else:
            deeta +=str(0)
        ok +=1
        if ok ==tmlen:
            deeta +="\n"
        else:
            deeta +=","
    oj +=1

unko.write(headder)
unko.write(deeta)
unko.close()

print("end")