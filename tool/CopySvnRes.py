import os
import shutil

targetRes="E:/layachuanqi/bin/assets/config/layares.dat"
targetErr="E:/layachuanqi/bin/assets/resource/locale/zh_CN/error.dat"

if(os.path.exists(targetRes)):
    os.remove(targetRes)

if(os.path.exists(targetErr)):
    os.remove(targetErr)

oPath="E:/doc/svnn/1.80 - test - dzy/"
shutil.copy(oPath+"error.dat",targetErr)
shutil.copy(oPath+"RES目录/layares.dat",targetRes)

# targetRes="E:/cqres-new/cqres/web_qa/assets/config/layares.dat"
# targetErr="E:/cqres-new/cqres/web_qa/assets/resource/locale/zh_CN/error.dat"
# shutil.copy(oPath+"error.dat",targetErr)
# shutil.copy(oPath+"RES目录/layares.dat",targetRes)