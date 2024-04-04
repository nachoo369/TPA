import sys
from PyQt6.QtWidgets import QApplication
from info_hotel import HotelInfoWidget
from habitacion import RoomSelectionWidget
from servicios import AdditionalServicesWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    info_hotel = HotelInfoWidget()
    habitacion = RoomSelectionWidget()
    servicios = AdditionalServicesWidget()

    info_hotel.show()
    habitacion.show()
    servicios.show()

    sys.exit(app.exec())
