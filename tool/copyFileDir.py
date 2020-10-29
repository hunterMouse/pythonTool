import os
from PIL import Image
import shutil
import sys


def jpgToPng(oPath,tPath,mapName):
    itemlist = os.listdir(oPath)
    minList=[mapName+"_s.jpg",mapName+"_b.jpg",mapName+"_t.jpg"]
    for fName in itemlist:

        boo = fName.find(".jpg")
        boo1 = fName in minList
        if boo >= 0 and boo1 == False:
            im = Image.open(oPath+fName)
            png=tPath+fName;
            tt = png.replace(".jpg",".png",1)
            im.save(tt)
            print("---"+tt)
        else:
            shutil.copy(oPath+fName,tPath+fName)

filrPath = "D:/map/map/"
tPath="D:/map/_out1/"
if os.path.exists(filrPath):
    filelist=os.listdir(filrPath)
    for fName in filelist:
        fpath = filrPath+fName
        if os.path.isfile(fpath):
             print(fName)
        else:
            tDir=tPath+fName
            if not os.path.exists(tDir):
                os.makedirs(tDir)

            jpgToPng(fpath+"/",tDir+"/",fName)
