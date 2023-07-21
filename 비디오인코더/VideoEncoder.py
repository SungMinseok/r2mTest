
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QKeySequence,QPixmap, QColor
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout

form_class = uic.loadUiType(f'pyqt5UI.ui')[0]


#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)



        #'''디폴트값설정_텍스트파일'''
        config = {}

        # 텍스트 파일 읽기
        # import os
        # current_script_path = os.path.abspath(__file__)
        # current_script_directory = os.path.dirname(current_script_path)
        # with open(f'{current_script_directory}\config.txt', 'r') as file:
        #     lines = file.readlines()

        with open(f'config.txt', 'r', encoding= 'utf-8') as file:
            lines = file.readlines()
        # 변수에 저장
        for line in lines:
            line = line.strip()  # 공백 및 개행문자 제거
            key, value = line.split('=')
            config[key] = value


        self.input_startsec.setText("0")
        self.input_endsec.setText("0")

        self.input_bitrate.setText(config['bitrate'])
        self.input_resultpath.setText(config['save_folder'])

        #〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓

        
        self.btn_datapath.clicked.connect(self.select_input_file)
        self.input_datapath.setAcceptDrops(True)
        self.input_datapath.dragEnterEvent = self.drag_enter_event
        self.input_datapath.dropEvent = self.drop_event



        self.btn_resultpath.clicked.connect(self.set_directory_path)
        self.btn_execute.clicked.connect(self.activate)

    def select_input_file(self):
        # Open a file dialog to select the data file
        file_filter = "Video files (*.mp4 *.mkv)"
        #file_filter = "엑셀 파일 (*.xlsx)"
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        data_file, _ = QFileDialog.getOpenFileName(self,"데이터 파일 선택", filter= file_filter, options=options)
        self.input_datapath.setText(data_file)

    def set_directory_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        directory_path = QFileDialog.getExistingDirectory(self, "Select Directory", "", options=options)
        if directory_path:
            self.input_resultpath.setText(f'{directory_path}/')

    def drag_enter_event(self, event):
        # 드래그앤드랍 가능한 MIME 타입인지 체크
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def drop_event(self, event):
        # 파일 경로를 가져와서 QLineEdit에 입력
        urls = event.mimeData().urls()
        file_path = urls[0].toLocalFile()
        self.input_datapath.setText(file_path)
        self.get_video_info()

    #230525
    def get_video_info(self):
        video_path = self.input_datapath.text()
        if video_path == "" :
            return
        video_info = sv.get_videoinfo(video_path)
        
        self.input_endsec.setText(str(video_info.duration))

    #230531
    def print_log(self, log):
        self.progressLabel.setText(log)
        QApplication.processEvents()

    def activate(self):
        input_filename = self.input_datapath.text()
        output_path =  self.input_resultpath.text()
        start_sec = float(self.input_startsec.text())
        end_sec = float(self.input_endsec.text())
        
        tempname = self.input_resultname.text()

        if tempname == "":
            tempname = "result"
        
        output_filename = f'{output_path}{tempname}.mp4'

        #if self.combox_contents.currentText() == "유료상점" and self.combox_doctype.currentText() == "CL" :
        try:
            sv.compress_video(input_filename,f'{output_filename}',start_time=start_sec, end_time=end_sec, bitrate="1500k")
        except Exception as e:
            print(e)


import setvideo as sv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QTextEdit, QComboBox


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()