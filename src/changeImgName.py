import glob
import os
from PIL import Image


def ResizeImage(filein, fileout, width, height, type):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS)
  #resize image with high-quality
  out.save(fileout, type)

inputPath = r'C:/Users/lianc/Desktop/h5资源修改/she3'
fileList = glob.glob(inputPath + '/*')
cnt = 0
cx = 0
for path in fileList:

    if cnt >= 5:
        cx += 1
        cnt = 0

    ren = str(cx)+"_"+str(cnt)

    # ResizeImage(path,path,400,400)
    os.rename(path, inputPath+'/'+ren+path[path.rfind('.'):])
    cnt +=1