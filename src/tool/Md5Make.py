import json
import hashlib
import pickle
import os
import time

import struct

def getmd5(file):
    m = hashlib.md5()
    with open(file,'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()
    return md5code[:10]

def traversalList(oPath,dic,rStr):
    dirList = os.listdir(oPath)
    for cell in dirList:
        fpath = oPath+cell
        if cell == "assets":
            continue
        if os.path.isfile(fpath):
            md5str=getmd5(fpath)
            pkey=fpath.replace(rStr,"")
            dic[pkey] = md5str
        else:
            traversalList(fpath+"/",dic,rStr)

tPath = "E:/cq-cdn/zzcq/"
pathAry=["E:/cq-cdn/zzcq/","E:/cq-cdn/zzcq/assets/loadbg3.jpg","E:/cq-cdn/zzcq/assets/png_m/comp/"]
star_time = time.time()
print("开始时间："+str(star_time))
md5dic = {}
for cpath in pathAry:
    if os.path.isfile(cpath):
        md5str = getmd5(cpath)
        ckey = cpath.replace(tPath, "")
        md5dic[ckey] = md5str
    else:
        traversalList(cpath, md5dic, tPath)

print("文件总数：")
print(len(md5dic))
v2path=tPath+'v2.txt'


sstr = json.dumps(md5dic)
fObj = open(v2path,'w',encoding='utf-8')
fObj.write(sstr)
fObj.close()


totalFile = len(md5dic)
v1path = tPath+'v1.dat'

f = open(tPath+'v1.dat','w', encoding='utf-8')
v2code=getmd5(v2path)
f.write(v2code)
f.close()

end_time = time.time()
print("总共花费时间："+str(end_time-star_time))
print("版本更新完成")
