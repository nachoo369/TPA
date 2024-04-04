import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class HotelApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hotel CTCh')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_widgets()

    def create_widgets(self):
        # Texto de bienvenida grande centrado con fondo azul
        self.label_welcome = QLabel("Bienvenido al Hotel CTCh", self)
        self.label_welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_welcome.setStyleSheet("background-color: blue; color: white; font-size: 24px;")
        self.layout.addWidget(self.label_welcome)

        # Botón de reserva verde grande
        self.button_reserve = QPushButton("Hacer reserva", self)
        self.button_reserve.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        self.button_reserve.clicked.connect(self.reserve_room)
        self.layout.addWidget(self.button_reserve)

        # Añadir espacio en blanco para que el botón de reserva se coloque en la parte inferior
        self.layout.addStretch()

    def reserve_room(self):
        # Aquí puedes abrir una nueva ventana para realizar la reserva
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HotelApp()
    window.show()
    sys.exit(app.exec())
