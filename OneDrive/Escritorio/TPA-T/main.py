from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QMenu
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hotel CTCh')
        #self.setStyleSheet("background-color: #ecdfcd;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setMinimumSize(600, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self.central_widget)

        # Widget de la barra de navegación
        navbar_widget = QWidget()
        navbar_widget.setStyleSheet("background-color: #a4927a;")  
        navbar_layout = QHBoxLayout(navbar_widget)

        # Botón de menú desplegable
        menu_button = QPushButton("Menú")
        menu_button.setStyleSheet("background-color: transparent; border: none; color: white;")
        menu_button.clicked.connect(self.show_menu)
        navbar_layout.addWidget(menu_button)

        layout.addWidget(navbar_widget)

        # Título de bienvenida
        welcome_label = QLabel("¡Bienvenido al Hotel CTCh!")
        welcome_label.setStyleSheet("color: white;")
        welcome_label.setFont(QFont("Arial", 20))
        layout.addWidget(welcome_label)

        # Inspiración para reservar
        inspiration_label = QLabel("¡Disfruta de la naturaleza y el lujo en un solo lugar!")
        inspiration_label.setStyleSheet("color: white;")
        layout.addWidget(inspiration_label)

        # Botón de reservar
        reserve_button = QPushButton("Reservar ya")
        reserve_button.setStyleSheet("background-color: #856c49; color: white;")
        layout.addWidget(reserve_button)

    def show_menu(self):
        menu = QMenu(self)
        menu.addAction("Restaurante")
        menu.addAction("Usuario")

        # Mostrar el menú en las coordenadas del botón de menú
        menu.exec(self.sender().mapToGlobal(self.sender().rect().bottomLeft()))


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
