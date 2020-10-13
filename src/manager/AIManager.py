

class AIManager(object):

    serverList=[]#当前的服务器列表
    robotCtr=[]#后台的机器人配置
    robotNum=0#当前机器人的数量
    robotPlayerData=[]#z最终需要生成的机器人的数据
    def __init__(self):
        ####加载线上配置，生成机器人数据
        self.makeRobotData();

    def makeRobotData(self):
        robotPlayerData = []

    def creatAI(self):
        ##创建ai