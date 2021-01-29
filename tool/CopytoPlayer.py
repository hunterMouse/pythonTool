import PIL.Image as img
import os
import shutil
from tkinter import *
import tkinter.filedialog


def makeImg(oPath,fname):
    npcdat="E:/cqres-new/cqres/web_test/_out/assets/player/android/"
    npcPng = "E:/cqres-new/cqres/web_test/_out/assets/player/__out/android/"

    if (os.path.exists(npcdat + fname)):
        shutil.rmtree(npcdat + fname)
    os.makedirs(npcdat + fname)

    if (os.path.exists(npcPng + fname)):
        shutil.rmtree(npcPng + fname)
    os.makedirs(npcPng + fname)

    fList = os.listdir(oPath+fname+"/")
    for fName in fList:
        boo = fName.find(".atf")
        boo1 = fName.find(".dat")
        boo2 = fName.find(".png")
        if boo >= 0:
            print("atf 文件不复制")
        elif boo1 >= 0:
            shutil.copy(oPath+fname +"/"+ fName, npcdat + fname + "/"+fName)
        elif boo2 >= 0:
            shutil.copy(oPath+fname + "/" + fName, npcPng +fname+"/"+fName)






def xz():
    filename = tkinter.filedialog.askdirectory()
    sPath = filename+"/"
    lb.config(text="您选择的文件是：" + sPath)
    dirList =  os.listdir(sPath)
    for dirName in dirList:
        makeImg(sPath,dirName)
    lb.config(text="图片处理完毕")



root = Tk()
root.title("拷贝资源")
root.geometry('500x300')

lb = Label(root,text = '点击按钮选择文件夹')
# lb.place(x=20,y=100)
lb.pack()
btn = Button(root,text="选择文件夹开始",command=xz)
btn.place(x=200,y=200)
root.mainloop()