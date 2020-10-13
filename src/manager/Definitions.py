import json
from typing import Dict, Any
global configDic
configDic = {}
class Definitions(object):
    global configDic
    _instance = None
    @classmethod
    def getJsonCfg(self, fileName):
        print(fileName)
        if fileName in configDic.keys():
            return configDic[fileName]
        else:
            data = open("E:/doc/svn/rxsj/RES目录/res/" + fileName + ".json", encoding='utf-8')
            str_Data = json.load(data)
            return str_Data

    def __new__(cls) -> object:
        if not hasattr(cls, 'instance'):
            cls.instance = super(Definitions, cls).__new__(cls)
        return cls.instance


ds=Definitions()
cfgdata = ds.getJsonCfg("robotinit")
print(cfgdata)
# configDic = {}

# configDic: Dict[Any, Any] = {}

# @staticmethod
# def getJsonCfg(fileName):
#     global configDic
#     if fileName in configDic.keys():
#         return configDic[fileName]
#     else:
#         data = open("E:/doc/svn/rxsj/RES目录/res/"+fileName+".json", encoding='utf-8')
#         str_Data = json.load(data)
#         return str_Data

# strData = getJsonCfg("robotinit")
# print(strData)
