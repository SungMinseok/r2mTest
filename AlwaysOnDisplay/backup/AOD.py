import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt
import os

class AlwaysOnTopWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Always On Top Window')
        #self.setGeometry(0, 977, 400, 30)
        screen_w, screen_h = 1920, 1080
        app_w = 400
        self.setGeometry(screen_w*2 - app_w, 977, app_w, 30)

        # 항상 위로 설정
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # 버튼 생성
        self.button1 = QPushButton('엑셀OFF', self)
        self.button1.setGeometry(0, 0, 80, 30)
        self.button1.clicked.connect(self.run_file1)

        self.button2 = QPushButton('크롬OFF', self)
        self.button2.setGeometry(80, 0, 80, 30)
        self.button2.clicked.connect(self.run_file2)

        self.button3 = QPushButton('그림판OFF', self)
        self.button3.setGeometry(160, 0, 80, 30)
        self.button3.clicked.connect(self.run_file3)

        self.button4 = QPushButton('전체OFF', self)
        self.button4.setGeometry(240, 0, 80, 30)
        self.button4.clicked.connect(self.run_file4)

        self.button5 = QPushButton('R2A업로드', self)
        self.button5.setGeometry(320, 0, 80, 30)
        self.button5.clicked.connect(self.run_file5)


    def run_file1(self):
        self.run_file('D:\\BatFile\\kill_excel.bat')

    def run_file2(self):
        self.run_file('D:\\BatFile\\kill_chrome.bat')
        # 다른 파일을 실행하려면 여기에 해당 파일 경로를 넣어주면 됩니다.
        pass

    def run_file3(self):
        self.run_file('D:\\BatFile\\kill_mspaint.bat')
        # 다른 파일을 실행하려면 여기에 해당 파일 경로를 넣어주면 됩니다.
        pass

    def run_file4(self):
        self.run_file('D:\\BatFile\\kill_excel.bat')
        self.run_file('D:\\BatFile\\kill_chrome.bat')
        self.run_file('D:\\BatFile\\kill_mspaint.bat')
        self.run_file('D:\\BatFile\\kill_word.bat')
        self.run_file('D:\\BatFile\\kill_notepad.bat')
        self.run_file('D:\\BatFile\\kill_powerpnt.bat')
        self.run_file('D:\\BatFile\\kill_messenger.bat')
        self.run_file('D:\\BatFile\\kill_outlook.bat')
        # 다른 파일을 실행하려면 여기에 해당 파일 경로를 넣어주면 됩니다.
        pass

    def run_file5(self):
        self.run_file('D:\\BatFile\\R2A_Upload.bat')
        # 다른 파일을 실행하려면 여기에 해당 파일 경로를 넣어주면 됩니다.
        pass

    def run_file(self, file_path):
        try:
            os.startfile(file_path)
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AlwaysOnTopWindow()
    window.show()
    sys.exit(app.exec_())
