import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

#Creamos una clase que referencie una interfaz grafica(pantalla principal)
class pantalla_principal(QMainWindow):
    def __init__(self):#definimos un constructor
        super(pantalla_principal, self).__init__() #cargamos los objetos (asignacion de memoria para elementos de la clase)
        uic.loadUi('designer.ui', self) #cargamos designer
        self.setWindowTitle("Reservas Hotel CTCh") #titulo ventana
        self.botonRes.clicked.connect(self.abrirNuevaVentana)

    
    #Funcion que permita redirigir a nueva ventana
    def abrirNuevaVentana(self):
        nueva_ventana = NuevaVentana()
        nueva_ventana.show()

class NuevaVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nueva Ventana")
        self.setGeometry(100, 100, 300, 200)

        self.botonRes = QPushButton("Haz clic", self)
        self.botonRes.setGeometry(100, 50, 100, 50)
#############arranque
# si el modulo name es igual al principal main se cumple la condicion
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaP = pantalla_principal() #se llama a la clase
    ventanaP.show() #mostramos la ventana
    sys.exit(app.exec())
