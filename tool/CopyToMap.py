import os
import shutil


def removeDirFile(rPath):
    rlist = os.listdir(rPath)
    for rname in rlist:
        os.remove(rPath+rname)

def copyDat(orPath,tPath,mapName):
    mmp = mapName+".mmp"
    if os.path.exists(orPath+mmp):
        shutil.copy(orPath+mmp, tPath + mmp)

    smap=mapName+"_s.jpg"
    if os.path.exists(orPath + smap):
        shutil.copy(orPath + smap, tPath + smap)

    tmap = mapName + "_t.jpg"
    if os.path.exists(orPath + tmap):
        shutil.copy(orPath + tmap, tPath + tmap)

    bmap = mapName + "_b.jpg"
    if os.path.exists(orPath + bmap):
        shutil.copy(orPath + bmap, tPath + bmap)

def copyImg(orPath,tPath,mapName):
    rlist = os.listdir(orPath)
    bbmap=mapName+".png"
    for f in rlist:
        if f == bbmap:
            print("取消大图拷贝"+f)
        else:
            shutil.copy(orPath + f, tPath + f)



oPath = "D:/map/_out1/"
tImg="E:/cqres-new/cqres/web_test/_out/assets/__out/map_android/"
tDat="E:/cqres-new/cqres/web_test/_out/assets/map_android/"
filelist=os.listdir(oPath)
for filename in filelist:
    print("----"+filename)
    if os.path.exists(tDat+filename+"/"):
        removeDirFile(tDat+filename+"/")
    else:
        os.makedirs(tDat+filename+"/")

    copyDat(oPath+filename+"/",tDat+filename+"/",filename)

    if os.path.exists(tImg + filename+"/"):
        removeDirFile(tImg + filename+"/")
    else:
        os.makedirs(tImg +filename+"/")

    copyImg(oPath+filename+"/",tImg+filename+"/",filename)


