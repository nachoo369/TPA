from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGroupBox

class RoomSelectionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Selección de Habitaciones')

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        rooms_group = QGroupBox('Habitaciones')
        rooms_layout = QVBoxLayout()

        room_types = [
            ("Ejecutiva Individual", "$50.000.-", "2 (1 recomendado)"),
            ("Ejecutiva Doble", "$80.000.-", "4 (2 recomendados)"),
            ("Familiar", "$150.000.-", "8 (6 recomendados)"),
            ("PentHouse", "$1.080.000.-", "2 (con invitados temporales indefinidos)")
        ]

        for room_type, price, capacity in room_types:
            room_label = QLabel(f"{room_type}: {price} / Capacidad: {capacity}")
            rooms_layout.addWidget(room_label)

        rooms_group.setLayout(rooms_layout)

        layout.addWidget(rooms_group)

        self.setLayout(layout)
