import os
import shutil
import sys
import re

def sort_key(s):
    # 排序关键字匹配
    # 匹配开头数字序号
    if s:
        r = ""
        try:
            c = re.findall('(\d+)',s)
            for nn in c:
                r+=nn
        except:
            r = "-1"
        return int(r)

def strsort(alist):
    alist.sort(key=sort_key)
    return alist


filrPath = "C:/Users/lianc/Desktop/h5资源修改/zz/idle/"
if os.path.exists(filrPath):
    filelist=os.listdir(filrPath)
    filelist= strsort(filelist)

    xcount=0
    ycount=0
    maxX= 4
    for fName in filelist:
        tName = filrPath+str(xcount)+"_"+str(ycount).zfill(3)+".png"
        os.rename(filrPath+fName,tName)
        ycount += 1
        if ycount > maxX:
            xcount += 1
            ycount=0



