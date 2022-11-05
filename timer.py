import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
         
    def __init__(self):
        global timeImage
        timeImage = ['./images/time10','./images/time9','./images/time8','./images/time7','./images/time6','./images/time5','./images/time4','./images/time3','./images/time2','./images/time1','./images/time12']
        
        super().__init__()
        self.setWindowTitle("Test")
        self.setGeometry(1000, 200, 300, 300)

        # timer 1
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout_fun)
        self.time_cnt =0

        self.time = QLabel(self) #시계 이미지
        
        

    def timeout_fun(self):
        if self.time_cnt > 9:
            self.timer.stop()
        self.time.setGeometry(10,30,600,600)
        self.time.setPixmap(QPixmap(timeImage[self.time_cnt])) #image path
        self.time.resize(600,600)
        #self.time.repaint()
        print("time cnt is %s" %timeImage[self.time_cnt])
        self.time_cnt += 1 
        
    
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()

    app.exec_()