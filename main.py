import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Test') #제목설정
        self.move(300, 300) #위치
        self.resize(400, 200) #위젯 크기
        self.show() #스크린에 보여주기


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())

