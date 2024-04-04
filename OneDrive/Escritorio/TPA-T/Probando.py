import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

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
        self.label = QLabel("Bienvenido al Hotel CTCh", self)
        self.layout.addWidget(self.label)

        self.button_reserve = QPushButton("Hacer reserva", self)
        self.button_reserve.clicked.connect(self.reserve_room)
        self.layout.addWidget(self.button_reserve)

    def reserve_room(self):
        # Aquí puedes abrir una nueva ventana para realizar la reserva
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HotelApp()
    window.show()
    sys.exit(app.exec())
