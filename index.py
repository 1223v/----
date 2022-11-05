import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global timeImage
        timeImage = ['./images/time10','./images/time9','./images/time8','./images/time7','./images/time6','./images/time5','./images/time4','./images/time3','./images/time2','./images/time1','./images/time12']
        
        self.setGeometry(600,200, 1280, 720)
        self.setWindowTitle('끝말잇기')

        self.lineedit = QLineEdit(self)
        #self.lineedit.textChanged.connect(self.change_text)

        #입력
        self.lineedit.returnPressed.connect(self.press_text)
        self.lineedit.setGeometry(560,310,400,100)
        self.lineedit.setObjectName('input')
        self.lineedit.setStyleSheet('QLineEdit#input {border:none; color: white; background-color:transparent; font-size: 40px; font-weight: bold; font-family: cursive;}')


        #출력 
        self.label = QLabel(self)
        self.label.setGeometry(300,400,100,100)
        self.label.setObjectName('text')
        self.label.setStyleSheet('QLabel#text {color: white;  font-size: 45px; font-weight: bold;}')

        
        #유저 아이디
        self.user = QLabel("User1",self) #배열을 넣어서 user 출력
        self.user.setGeometry(820,560,100,60)
        self.user.setObjectName('user')
        self.user.setStyleSheet('QLabel#user {color: white; font-size: 30px; font-weight: bold;}')

        #시작 버튼
        self.btnStart = QPushButton("시작",self)
        self.btnStart.setGeometry(820,560,100,60)
        self.btnStart.clicked.connect(self.onStartButtonClicked)

        # timer 1
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout_fun)
        self.time_cnt =0
        self.time = QLabel(self) #시계 이미지

        oImage=QImage("./images/main.png")
        sImage = oImage.scaled(1280, 720)
        palette = QPalette()
        palette.setBrush(10,QBrush(sImage))
        self.setPalette(palette)



    def onStartButtonClicked(self):
        self.timer.start()
        self.btnStart.setEnabled(False)

    def timeout_fun(self):
        if self.time_cnt > 9:
            self.timer.stop()
        self.time.setGeometry(10,30,600,600)
        self.time.setPixmap(QPixmap(timeImage[self.time_cnt])) #image path
        self.time.resize(600,600)
        #self.time.repaint()
        print("time cnt is %s" %timeImage[self.time_cnt])
        self.time_cnt += 1 

    def change_text(self,txt):
        self.label.setText(txt)
        self.label.adjustSize()

    def press_text(self):
        self.label.setText(self.lineedit.text())
        self.label.adjustSize()
        self.lineedit.clear()

if __name__=="__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()


    sys.exit(app.exec_())