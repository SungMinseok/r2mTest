import sys
import cv2
import numpy as np
import pyautogui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class RecordingThread(QThread):
    recordingFinished = pyqtSignal(str)

    def __init__(self, x, y, w, h, fps, title, show_mouse):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.fps = fps
        self.title = title
        self.show_mouse = show_mouse

    def run(self):
        screen_size = (self.w, self.h)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        output_file = f"{self.title}.mp4"
        out = cv2.VideoWriter(output_file, fourcc, self.fps, screen_size)

        try:
            while self.isRunning():
                screenshot = pyautogui.screenshot(region=(self.x, self.y, self.w, self.h))
                frame = np.array(screenshot)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                if self.show_mouse:
                    x_mouse, y_mouse = pyautogui.position()
                    cv2.circle(frame, (x_mouse - self.x, y_mouse - self.y), 5, (0, 0, 255), -1)
                out.write(frame)
        except KeyboardInterrupt:
            pass

        out.release()
        self.recordingFinished.emit(output_file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screen Recorder")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.start_button = QPushButton("Start Recording", self)
        self.start_button.clicked.connect(self.start_recording_clicked)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Recording", self)
        self.stop_button.clicked.connect(self.stop_recording_clicked)
        layout.addWidget(self.stop_button)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.recording_thread = None

    def start_recording_clicked(self):
        if not self.recording_thread or not self.recording_thread.isRunning():
            x = 0  # 설정할 x 좌표
            y = 0  # 설정할 y 좌표
            width = 1920  # 설정할 가로 길이
            height = 1080  # 설정할 세로 길이
            fps = 20  # 프레임 레이트
            title = "recorded_screen"  # 저장할 제목
            show_mouse = True  # 마우스 포인터 보여줄지 여부

            self.recording_thread = RecordingThread(x, y, width, height, fps, title, show_mouse)
            self.recording_thread.recordingFinished.connect(self.on_recording_finished)
            self.recording_thread.start()

    def stop_recording_clicked(self):
        if self.recording_thread and self.recording_thread.isRunning():
            self.recording_thread.quit()

    def on_recording_finished(self, output_file):
        print(f"Recording stopped. Saved as {output_file}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
