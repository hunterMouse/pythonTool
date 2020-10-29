import PIL.Image as img
import os
import shutil
def calculatesize(path):
    fList = os.listdir(path)
    xList=[]
    yList=[]
    for file in fList:
        tpath=path+file
        with open(tpath,"r") as txt:
            offx = int(txt.readline())
            offy = int(txt.readline())
            xList.append(abs(offx))
            yList.append(abs(offy))

    xList.sort()
    yList.sort()
    return xList[-1],yList[-1]

def readOff(path):
    with open(path, "r") as txt:
        offx = int(txt.readline())
        offy = int(txt.readline())
    return offx,offy






def makeImg(oPath):
    if os.path.exists(oPath+"_out/"):
        shutil.rmtree(oPath+"_out/")

    os.makedirs(oPath+"_out/")

    ofx,ofy = calculatesize(oPath+"Placements/")

    imgList=os.listdir(oPath)
    for fName in imgList:
        if(os.path.isfile(oPath+fName)):
            o = img.open("touming.png")
            p = img.open(oPath+fName)

            x,y=readOff(oPath+"Placements/"+fName[0:-3]+"txt")
            o.paste(p,(512+x,512+y))
            o.save(oPath+"_out/"+fName)

sPath = "C:/Users/lianc/Desktop/h5资源修改/外观/"
dirList =  os.listdir(sPath)
for dirName in dirList:
    makeImg(sPath+dirName+"/")
