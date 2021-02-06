
import PIL.Image as img
import os
import shutil
from tkinter import *
import tkinter.filedialog



def makeImg(oPath):
    o = img.open(oPath)
    sizeAry = [48, 57, 72, 76, 96, 114, 120, 144, 152, 192]
    for wd in sizeAry:
        out = o.resize((wd, wd))
        out.save("F:/_out/icon_"+str(wd)+".png", "png")


def xz():
    filename = tkinter.filedialog.askopenfile()
    lb.config(text="您选择的文件是：" + filename.name)
    makeImg(filename.name)


root = Tk()
root.title("处理图片")
root.geometry('500x300')

lb = Label(root,text = '点击按钮选择文件夹')
# lb.place(x=20,y=100)
lb.pack()
btn = Button(root,text="选择文件夹开始",command=xz)
btn.place(x=200,y=200)
root.mainloop()
