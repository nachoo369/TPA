from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGroupBox

class HotelInfoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Bienvenido al Hotel CTZ')

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        hotel_info_group = QGroupBox('Información del Hotel')
        hotel_info_layout = QVBoxLayout()
        hotel_info_label = QLabel(
            "El Hotel CTCh es un espacio de descanso, relajación y comodidad,\ncon instalaciones basadas en la naturaleza del entorno,\npero con todo el lujo y privacidad de un\nestablecimiento de cinco estrellas.")
        hotel_info_layout.addWidget(hotel_info_label)
        hotel_info_group.setLayout(hotel_info_layout)

        layout.addWidget(hotel_info_group)

        self.setLayout(layout)
        self.setGeometry(100,100,400,400)
