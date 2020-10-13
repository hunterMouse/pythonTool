import os
import shutil

filrPath = "C:/Users/lianc/Desktop/h5资源修改/战士-天魔神甲-男-压缩/stand/"
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



