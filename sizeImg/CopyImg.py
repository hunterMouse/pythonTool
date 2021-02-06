import PIL.Image as img
import os
import shutil
from tkinter import *
import tkinter.filedialog


ttPath="F:/cocos/CoinGame/assets/fruit/"
count=0

def makeImg(oPath):
    imgList=os.listdir(oPath)
    for fName in imgList:
        global count
        count += 1
        shutil.copy(oPath+fName, ttPath+str(count)+fName)

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