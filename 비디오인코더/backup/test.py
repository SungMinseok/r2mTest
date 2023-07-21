

# 이미지 파일 경로

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class ImageDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # QLabel 위젯 생성
        self.label = QLabel(self)

        # QLabel 위젯 크기 설정
        self.label.setFixedSize(200, 200)

        # 이미지 파일 경로
        image_path = 'Accessory_Cash_002.png'

        try:
            # QPixmap 객체 생성
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                print('Error: QPixmap 객체 생성 실패')
                sys.exit()

            # QLabel 위젯에 이미지 설정
            self.label.setPixmap(pixmap)

            # QLabel 위젯에 마우스 이벤트 핸들러 등록
            self.label.mousePressEvent = self.onMousePressEvent
            self.label.mouseReleaseEvent = self.onMouseReleaseEvent

            # QVBoxLayout 레이아웃 생성 및 QLabel 추가
            layout = QVBoxLayout()
            layout.addWidget(self.label)
            self.setLayout(layout)

        except Exception as e:
            print(f'Error: {e}')
            sys.exit()

    def onMousePressEvent(self, event):
        # 마우스 클릭 시 이미지 확대
        self.label.setPixmap(self.label.pixmap().scaled(300, 300, aspectRatioMode=True))

    def onMouseReleaseEvent(self, event):
        # 마우스 릴리즈 시 이미지 원래 크기로 돌아감
        self.label.setPixmap(self.label.pixmap().scaled(200, 200, aspectRatioMode=True))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageDisplay()
    ex.show()
    sys.exit(app.exec_())
