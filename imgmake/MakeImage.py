import PIL.Image as img
import os
import shutil
from tkinter import *
import tkinter.filedialog

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

    # ofx,ofy = calculatesize(oPath+"Placements/")

    imgList=os.listdir(oPath)
    for fName in imgList:
        if(os.path.isfile(oPath+fName)):
            o = img.open("touming1.png")
            p = img.open(oPath+fName)

            # x,y=readOff(oPath+"Placements/"+fName[0:-3]+"txt")
            cropped = p.crop((144, 144, 144+512, 144+512))
            o.paste(cropped, (0, 0))
            # o.paste(p,(512+x,512+y))
            o.save(oPath+"_out/"+fName)



def xz():
    filename = tkinter.filedialog.askdirectory()
    sPath = filename+"/"
    lb.config(text="您选择的文件是：" + sPath)
    dirList =  os.listdir(sPath)
    for dirName in dirList:
        makeImg(sPath+dirName+"/")
    lb.config(text="图片处理完毕")

root = Tk()
root.title("处理图片")
root.geometry('500x300')

lb = Label(root,text = '点击按钮选择文件夹')
# lb.place(x=20,y=100)
lb.pack()
btn = Button(root,text="选择文件夹开始",command=xz)
btn.place(x=200,y=200)
root.mainloop()


