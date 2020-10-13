
import json
import hashlib
import shutil
import os


def getmd5(file):
    m = hashlib.md5()
    with open(file,'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()
    print(md5code)
    return md5code[:10]

def changeVer(md5,vkey):
    load_dict={}
    with open(verpath, 'r') as load_f:
        load_dict = json.load(load_f)
    print(load_dict[vkey])
    load_dict[vkey] = "assets/config/layares-"+md5+".dat"
    print(load_dict[vkey])
    with open(verpath, "w") as dump_f:
        json.dump(load_dict, dump_f)
    return ""

print("1、测试服更新")
print("2、正式服更新")
print("3、1.80更新")
print("4、新功能更新")

vkey="assets/config/layares.dat"

str = input("请输入：")
tpath="E:/cqres-new/cqres/web_test/"
rPath="E:/doc/svnn/test/RES目录/"
if int(str) == 2:
    tpath = "E:/cqres-new/cqres/web_online/"
    rPath = "E:/doc/svnn/test/RES目录/"
    print("已选择正式服更新")
elif int(str) == 3:
    tpath = "E:/cqres-new/cqres/web_gold/"
    rPath = "E:/doc/svnn/1.80/RES目录/"
    print("已选择1.80")
elif int(str) == 4:
    tpath = "E:/cqres-new/cqres/web_test_new/"
    rPath = "E:/doc/svnn/test/RES目录/"
    print("已选择新功能更新")
else:
    print("已选择测试服更新")

rPath=rPath+"layares.dat"
verpath = tpath+"version.json"

if os.path.exists(rPath):
    fileMd5 = getmd5(rPath)
    shutil.copyfile(rPath,tpath+"assets/config/layares-"+fileMd5+".dat")
    changeVer(fileMd5,vkey)







