#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

import csv
import re
import numpy as np
path ="C:\\Users\\1500570\\Documents\\R\\WS\\ws_ais"
rf =csv.reader(open(path+"\\output3.csv", "r+"))
rf2 =open(path+"\\180514_3.xml", "r+")


namename = re.compile("<NAME>.+</NAME>")
ff =re.compile("<FOR>.+</FOR>")
gg =re.compile("<GIVEN>.+</GIVEN>")

kumi_list =[]
for line in rf:
    kumi_list.append(line)
kumi_list=np.array(kumi_list)
k2 =kumi_list[:,1]
print(k2)
#print(int(np.where(k2 =="snow")[0]))
koushin =""

for line2 in rf2:
    temp =namename.search(line2)
    tempf =ff.search(line2)
    tempg =gg.search(line2)
    #print(line2)
    if bool(temp) ==True:
        word =temp.group().replace("<NAME>","").replace("</NAME>","")
        #print(word)
        innde =np.where(k2 ==word)[0]
        if len(innde) ==0:
            koushin +=line2
            continue
        line2 =line2.replace(temp.group(), "<NAME>"+kumi_list[int(innde),0]+"</NAME>")
        #print(line2)
    elif bool(tempf) ==True:
        word =tempf.group().replace("<FOR>","").replace("</FOR>","")
        #print(word)
        innde =np.where(k2 ==word)[0]
        if len(innde) ==0:
            koushin +=line2
            continue
        line2 =line2.replace(tempf.group(), "<FOR>"+kumi_list[int(innde),0]+"</FOR>")
        #print(line2)
    elif bool(tempg) ==True:
        word =tempg.group().replace("<GIVEN>","").replace("</GIVEN>","")
        #print(word)
        innde =np.where(k2 ==word)[0]
        if len(innde) ==0:
            koushin +=line2
            continue
        line2 =line2.replace(tempg.group(), "<GIVEN>"+kumi_list[int(innde),0]+"</GIVEN>")
        #print(line2)
    koushin +=line2

#print(koushin)
unko =open(path+"\\180514_3_ja.xml","w+",newline="", encoding="utf-8")
unko.write(koushin)
unko.close()

#rf.close()
rf2.close()
#print(kumi_list)
print("end")