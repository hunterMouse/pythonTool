# -*- coding:utf-8 -*-
import os
import shutil



def createFile(cont,sp):
    lis= cont.split(sp)
    if(len(lis)< 2):
        return
    fn=lis[0]
    file = open('C:/Users/lianc/Desktop/上傳/_out/'+fn+'.txt', 'w')
    file.write(cont)
    file.close();




tpath="C:/Users/lianc/Desktop/上傳/all.txt"
with open(tpath,'r', encoding='utf-8') as f:
    all = f.readlines()
    sp=all[4]
    str=""
    for cont in all:
        if(cont.find("段内容后打开百度网盘手机") != -1):
            cont=""
        if(cont==sp ):
            createFile(str,sp)
            str=""
        else:
            str += cont

