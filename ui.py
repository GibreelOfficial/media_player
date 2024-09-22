from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QSlider, QFileDialog
from media_player import MediaPlayer

class MediaPlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Player")
        self.setGeometry(100, 100, 300, 200)

        self.media_player = MediaPlayer()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Loaded: None")
        self.status_label = QLabel("Status: Idle")
        self.volume_label = QLabel("Volume: 100%")

        self.load_button = QPushButton("Load File")
        self.load_button.clicked.connect(self.load_file)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_media)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_media)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_media)

        self.volume_slider = QSlider()
        self.volume_slider.setOrientation(1)  # 1 for vertical, 0 for horizontal
        self.volume_slider.setValue(100)
        self.volume_slider.valueChanged.connect(self.change_volume)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.load_button)
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.volume_label)
        layout.addWidget(self.volume_slider)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")
        if file_path:
            self.media_player.load_file(file_path)
            self.label.setText(f"Loaded: {file_path.split('/')[-1]}")
            self.status_label.setText("Status: Idle")

    def play_media(self):
        self.media_player.play()
        self.status_label.setText("Playing")

    def pause_media(self):
        self.media_player.pause()
        self.status_label.setText("Paused")

    def stop_media(self):
        self.media_player.stop()
        self.status_label.setText("Stopped")

    def change_volume(self, value):
        self.media_player.change_volume(value)
        self.volume_label.setText(f"Volume: {value}%")
