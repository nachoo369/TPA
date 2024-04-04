from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGroupBox

class AdditionalServicesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Servicios Adicionales')

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        services_group = QGroupBox('Servicios Adicionales')
        services_layout = QVBoxLayout()

        # Aquí puedes agregar widgets para los servicios adicionales según sea necesario

        services_group.setLayout(services_layout)

        layout.addWidget(services_group)

        self.setLayout(layout)
