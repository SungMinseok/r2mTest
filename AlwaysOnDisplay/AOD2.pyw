import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
import os

class AlwaysOnTopWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Always On Top Window')
        #self.setGeometry(100, 100, 240, 30)
        screen_w, screen_h = 1920, 1080
        app_w = 400

        # 항상 위로 설정
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # buttons_info = [
        #     ('엑셀OFF', ['D:\BatFile\kill_excel.bat']),
        #     ('크롬OFF', ['D:\\BatFile\\kill_chrome.bat']),
        #     ('그림판OFF', ['D:\\BatFile\\kill_mspaint.bat']),
        #     ('아웃룩OFF', ['D:\\BatFile\\kill_outlook.bat']),
        #     ('!퇴근!', ['D:\\BatFile\\kill_mspaint.bat',
        #                'D:\\BatFile\\kill_excel.bat',
        #                'D:\\BatFile\\kill_chrome.bat',
        #                'D:\\BatFile\\kill_outlook.bat',
        #                'D:\\BatFile\\kill_powerpnt.bat',
        #                'D:\\BatFile\\kill_word.bat',
        #                'D:\\BatFile\\kill_messenger.bat',
        #                'D:\\BatFile\\kill_teams.bat',
        #                ]),
        #     ('R2A', ['D:\\R2A\\R2A.py']),
        #     #('RDM', [f'C:\Users\mssung\OneDrive - Webzen Inc\R2M도구\유료상점CL생성기\RDM.py']),
        #     ('VideoEC', ['D:\\파이썬프로젝트\\r2mTest\\비디오\\VideoEncoder.py']),
        #     ('빌드다운', ['d:\Builds\빌드 다운로드.bat']),
        #     ('R2A_UI최신', ['D:\\BatFile\\kill_mspaint.bat']),
        #     # ('그림판OFF', ['D:\\BatFile\\kill_mspaint.bat']),
        #     # ('그림판OFF', ['D:\\BatFile\\kill_mspaint.bat']),
        #     # ('그림판OFF', ['D:\\BatFile\\kill_mspaint.bat']),
        #     # ('그림판OFF', ['D:\\BatFile\\kill_mspaint.bat']),
        #     # ('그림판OFF', ['D:\\BatFile\\kill_mspaint.bat']),
        #     # ('그림판OFF', ['D:\\BatFile\\kill_mspaint.bat']),
        #     # ('그림판OFF', ['D:\\BatFile\\kill_mspaint.bat'])
        # ]

        self.setGeometry(1920,1060, 81*len(buttons_info), 20)

        # layout = QGridLayout()
        # layout.setSpacing(0)
        # layout.setHorizontalSpacing(0)
        # row, col = 0, 0

        # for i, (button_text, file_path) in enumerate(buttons_info):
        #     button = QPushButton(button_text, self)
        #     if i == 4:  # 5번째 버튼에 스타일 적용
        #         button.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        #     button.clicked.connect(lambda _, path=file_path: self.run_file(path))

        #     layout.addWidget(button, row, col)
        #     col += 1

        #     if col == 5:
        #         row += 1
        #         col = 0

        # self.setLayout(layout)
        

# 초월: 253,179,0
# 전설: 255,0,0
# 영웅: 179,67,217
# 희귀:14,155,217
# 고급:98,197,177
# 일반:178,178,178

        for i, (button_color, button_text, file_path) in enumerate(buttons_info):
            button = QPushButton(button_text, self)
            #button.setStyleSheet("background-color: rgb(47, 117, 181);\ncolor: rgb(255, 255, 255);\nfont: bold")
            #button.setStyleSheet("color: rgb(14, 155, 217);font: bold")
            if button_color == 0 :            
                button.setStyleSheet("background-color: rgb(178, 178, 178);\ncolor: rgb(255, 255, 255);\nfont: bold")

            elif button_color == 1 :
                button.setStyleSheet("background-color: rgb(98, 197, 177);\ncolor: rgb(255, 255, 255);\nfont: bold")
            elif button_color == 2 :
                button.setStyleSheet("background-color: rgb(14, 155, 217);\ncolor: rgb(255, 255, 255);\nfont: bold")
            elif button_color == 3 :
                button.setStyleSheet("background-color: rgb(179, 67, 217);\ncolor: rgb(255, 255, 255);\nfont: bold")
            elif button_color == 4 :
                button.setStyleSheet("background-color: rgb(255, 0, 0);\ncolor: rgb(255, 255, 255);\nfont: bold")
            elif button_color == 5 :
                button.setStyleSheet("background-color: rgb(253, 179, 0);\ncolor: rgb(255, 255, 255);\nfont: bold")
            
            
            button.setGeometry(81 * i , 0, 80, 20)
            button.clicked.connect(lambda _, path=file_path: self.run_file(path))

    def run_file(self, file_paths):
        try:
            for file_path in file_paths :
                if ".py" in file_path:
                    # 디렉토리 경로 추출
                    file_directory = os.path.dirname(file_path)
                    os.chdir(file_directory)
                os.startfile(file_path)
        except Exception as e:
            print("Error:", e)


def parse_config_file(file_path):
    buttons_info = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line:
            parts = line.split(',')
            button_color = int(parts[0])
            button_text = parts[1]
            file_paths = [path.strip() for path in parts[2:]]

            buttons_info.append((button_color, button_text, file_paths))

    return buttons_info

if __name__ == "__main__":
    config_file = "config.txt"
    global buttons_info
    buttons_info = parse_config_file(config_file)

    #for i, (button_color,button_text, file_paths) in enumerate(buttons_info):
    #    print(f"buttons_info[{i}] = ('{button_text}', {file_paths})")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AlwaysOnTopWindow()
    window.show()
    sys.exit(app.exec_())
