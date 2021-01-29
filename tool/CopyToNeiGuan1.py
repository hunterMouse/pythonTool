import PIL.Image as img
import os
import shutil
from tkinter import *
import tkinter.filedialog


def makeImg(oPath,fname):
    npcdat="E:/cqres-new/cqres/web_test/_out/assets/icon/neiguan/android/"
    npcPng = "E:/cqres-new/cqres/web_test/_out/assets/icon/neiguan/__out/android/"
    fname = fname[:-4]

    if (os.path.exists(npcdat + fname)):
        shutil.rmtree(npcdat + fname)
    os.makedirs(npcdat + fname)

    if (os.path.exists(npcPng + fname)):
        shutil.rmtree(npcPng + fname)
    os.makedirs(npcPng + fname)

    shutil.copy(oPath + "/" + fname + ".dat", npcdat + fname + "/idle.dat")
    shutil.copy(oPath + "/" + fname + ".png", npcPng + fname + "/idle.png")




def xz():
    filename = tkinter.filedialog.askdirectory()
    sPath = filename+""
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