import os
import shutil
import sys

filrPath = "C:/Users/lianc/Desktop/temp/102101111/"
if os.path.exists(filrPath):
    filelist=os.listdir(filrPath)
    xcount=0;
    ycount=0;
    maxX= 3;
    for fName in filelist:
        tName = filrPath+str(xcount)+"_"+str(ycount)+".png"
        os.rename(filrPath+fName,tName)
        ycount += 1
        if ycount > maxX:
            xcount += 1
            ycount=0



