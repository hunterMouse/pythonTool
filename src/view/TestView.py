from src.design.test import Ui_Dialog
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests
import zlib

global res,server,pid,appid
res = "http://cqtest-new.shmxplay.com/"
server = "http://47.100.22.247:8888/"
pid = 1000
appid = 1000000005

class TestView(Ui_Dialog):
    def setDeafultCfg(self):
        self.appidTxt.setText(""+str(appid))
        self.pidTxt.setText(""+str(pid))
        self.serverTxt.setText("" + server)
        self.cdnTxt.setText("" + res)
        self.pageTxt.setText("1")
        self.jiangeTxt.setText("1000")
        self.maxPlayerNumTxt.setText("1000")
        self.btnStart.clicked.connect(self.on_click)




    def on_click(self):
        url = res + "cq"+str(appid)+"/layares.dat"
        f = requests.get(url)
        data = f.content
        decompress = zlib.decompressobj(-zlib.MAX_WBITS)
        inflated = decompress.decompress(data)
        # inflated += decompress.flush()
        type = inflated[:8]
        resStr = type.decode("UTF-8")

        print(resStr)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = TestView()
    ui.setupUi(MainWindow)
    ui.setDeafultCfg()
    MainWindow.show()
    sys.exit(app.exec_())
