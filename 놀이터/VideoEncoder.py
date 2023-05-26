

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 267)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 401, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: bold;color:rgb(0, 0, 0)")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.input_datapath = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_datapath.sizePolicy().hasHeightForWidth())
        self.input_datapath.setSizePolicy(sizePolicy)
        self.input_datapath.setMinimumSize(QtCore.QSize(0, 23))
        self.input_datapath.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.input_datapath.setFont(font)
        self.input_datapath.setPlaceholderText("")
        self.input_datapath.setObjectName("input_datapath")
        self.horizontalLayout_5.addWidget(self.input_datapath)
        self.btn_datapath = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_datapath.sizePolicy().hasHeightForWidth())
        self.btn_datapath.setSizePolicy(sizePolicy)
        self.btn_datapath.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_datapath.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.btn_datapath.setFont(font)
        self.btn_datapath.setStyleSheet("background-color: rgb(155, 194, 230);")
        self.btn_datapath.setObjectName("btn_datapath")
        self.horizontalLayout_5.addWidget(self.btn_datapath)
        self.btn_datapath_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_datapath_2.sizePolicy().hasHeightForWidth())
        self.btn_datapath_2.setSizePolicy(sizePolicy)
        self.btn_datapath_2.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_datapath_2.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.btn_datapath_2.setFont(font)
        self.btn_datapath_2.setStyleSheet("background-color: rgb(155, 194, 230);")
        self.btn_datapath_2.setObjectName("btn_datapath_2")
        self.horizontalLayout_5.addWidget(self.btn_datapath_2)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 70, 401, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: bold;font-color:(255,255,255)")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.input_resultpath = QtWidgets.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_resultpath.sizePolicy().hasHeightForWidth())
        self.input_resultpath.setSizePolicy(sizePolicy)
        self.input_resultpath.setMinimumSize(QtCore.QSize(0, 23))
        self.input_resultpath.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.input_resultpath.setFont(font)
        self.input_resultpath.setPlaceholderText("")
        self.input_resultpath.setObjectName("input_resultpath")
        self.horizontalLayout_6.addWidget(self.input_resultpath)
        self.btn_resultpath = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_resultpath.sizePolicy().hasHeightForWidth())
        self.btn_resultpath.setSizePolicy(sizePolicy)
        self.btn_resultpath.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_resultpath.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.btn_resultpath.setFont(font)
        self.btn_resultpath.setStyleSheet("background-color: rgb(155, 194, 230);")
        self.btn_resultpath.setObjectName("btn_resultpath")
        self.horizontalLayout_6.addWidget(self.btn_resultpath)
        self.btn_resultpath_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_resultpath_2.sizePolicy().hasHeightForWidth())
        self.btn_resultpath_2.setSizePolicy(sizePolicy)
        self.btn_resultpath_2.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_resultpath_2.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.btn_resultpath_2.setFont(font)
        self.btn_resultpath_2.setStyleSheet("background-color: rgb(155, 194, 230);")
        self.btn_resultpath_2.setObjectName("btn_resultpath_2")
        self.horizontalLayout_6.addWidget(self.btn_resultpath_2)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 110, 401, 31))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: bold;font-color:(255,255,255)")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.input_resultname = QtWidgets.QLineEdit(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_resultname.sizePolicy().hasHeightForWidth())
        self.input_resultname.setSizePolicy(sizePolicy)
        self.input_resultname.setMinimumSize(QtCore.QSize(0, 23))
        self.input_resultname.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.input_resultname.setFont(font)
        self.input_resultname.setPlaceholderText("")
        self.input_resultname.setObjectName("input_resultname")
        self.horizontalLayout_8.addWidget(self.input_resultname)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 150, 401, 31))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.input_startsec = QtWidgets.QLineEdit(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_startsec.sizePolicy().hasHeightForWidth())
        self.input_startsec.setSizePolicy(sizePolicy)
        self.input_startsec.setMinimumSize(QtCore.QSize(0, 23))
        self.input_startsec.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.input_startsec.setFont(font)
        self.input_startsec.setObjectName("input_startsec")
        self.horizontalLayout_9.addWidget(self.input_startsec)
        self.input_endsec = QtWidgets.QLineEdit(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_endsec.sizePolicy().hasHeightForWidth())
        self.input_endsec.setSizePolicy(sizePolicy)
        self.input_endsec.setMinimumSize(QtCore.QSize(0, 23))
        self.input_endsec.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.input_endsec.setFont(font)
        self.input_endsec.setObjectName("input_endsec")
        self.horizontalLayout_9.addWidget(self.input_endsec)
        self.input_bitrate = QtWidgets.QLineEdit(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_bitrate.sizePolicy().hasHeightForWidth())
        self.input_bitrate.setSizePolicy(sizePolicy)
        self.input_bitrate.setMinimumSize(QtCore.QSize(0, 23))
        self.input_bitrate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.input_bitrate.setFont(font)
        self.input_bitrate.setObjectName("input_bitrate")
        self.horizontalLayout_9.addWidget(self.input_bitrate)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 190, 401, 31))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.progressLabel = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressLabel.setFont(font)
        self.progressLabel.setObjectName("progressLabel")
        self.horizontalLayout_10.addWidget(self.progressLabel)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget_5)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_10.addWidget(self.checkBox)
        self.btn_execute = QtWidgets.QPushButton(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_execute.sizePolicy().hasHeightForWidth())
        self.btn_execute.setSizePolicy(sizePolicy)
        self.btn_execute.setMinimumSize(QtCore.QSize(80, 0))
        self.btn_execute.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_execute.setFont(font)
        self.btn_execute.setStyleSheet("background-color: rgb(47, 117, 181);\n"
"color: rgb(255, 255, 255);\n"
"font: bold")
        self.btn_execute.setObjectName("btn_execute")
        self.horizontalLayout_10.addWidget(self.btn_execute)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sesang Encoder (Video Encoder)"))
        self.label.setText(_translate("MainWindow", "대상 비디오"))
        self.btn_datapath.setText(_translate("MainWindow", "..."))
        self.btn_datapath_2.setText(_translate("MainWindow", "열기"))
        self.label_2.setText(_translate("MainWindow", "저장 폴더"))
        self.btn_resultpath.setText(_translate("MainWindow", "..."))
        self.btn_resultpath_2.setText(_translate("MainWindow", "열기"))
        self.label_4.setText(_translate("MainWindow", "저장할 이름"))
        self.input_startsec.setPlaceholderText(_translate("MainWindow", "시작지점(초)"))
        self.input_endsec.setPlaceholderText(_translate("MainWindow", "종료지점(초)"))
        self.input_bitrate.setPlaceholderText(_translate("MainWindow", "비트레이트(k)"))
        self.progressLabel.setText(_translate("MainWindow", "준비상태"))
        self.checkBox.setText(_translate("MainWindow", "작업 후 폴더 열기"))
        self.btn_execute.setText(_translate("MainWindow", "실행 (F2)"))
        self.btn_execute.setShortcut(_translate("MainWindow", "F2"))






#region ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■유지부

        '''디폴트값설정'''
        self.input_startsec.setText("0")
        self.input_endsec.setText("0")


        
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

        data_file, _ = QFileDialog.getOpenFileName(MainWindow,"데이터 파일 선택", filter= file_filter, options=options)
        self.input_datapath.setText(data_file)

    def set_directory_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        directory_path = QFileDialog.getExistingDirectory(MainWindow, "Select Directory", "", options=options)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


#endregion