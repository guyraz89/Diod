import sys
from PySide2 import QtWidgets, QtCore, QtGui

from mainUI import Ui_MainWindow
from DiodUI import Ui_DiodSettings


class MainApp(QtWidgets.QApplication):
    """ Main application infrastructure """
    def __init__(self, argv):
        super().__init__(argv)
        self.main_window = MainWindow()
        self.main_window.setWindowTitle("Korat Engineering")
        self.main_window.show()


class MainWindow(QtWidgets.QMainWindow):
    """ Main application window """
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # CREATE TWO INSTANCES OF DIOD SETTINGS
        self.diod16w = DiodSettings("980 nm", 16.0)
        self.diod40w = DiodSettings("1470 nm", 40.0)
        # ADD THEM TO THE SETTINGS LAYOUT
        self.ui.SettingsLayout.addWidget(self.diod16w)       
        self.ui.SettingsLayout.addWidget(self.diod40w)        
        # SET MENU BUTTONS SWITCH BETWEEN SETTINGS CALIBRATION AND DIAGNOSTICS
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Diagnostics))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Settings))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Calibration))

        # SET ENABLE/DISABLE OPTIONS FOR BOTH 16 AND 40 W DIOD
        # self.ui.EnableButton.clicked.connect(lambda: print("Enable Button"))

        # SET AIMING BEAM CONTROL
        self.ui.IncrementBeamButton.clicked.connect(self.incrementAimingBeam)
        self.ui.DecrementBeamButton.clicked.connect(self.decrementAimingBeam)


    def incrementAimingBeam(self):
        barValue = self.ui.progressBar.value()
        if barValue >= 100:
            return True
        self.ui.progressBar.setValue(barValue + 20)
    
    def decrementAimingBeam(self):
        barValue = self.ui.progressBar.value()
        if barValue == 0:
            return True
        self.ui.progressBar.setValue(barValue - 20)

class DiodSettings(QtWidgets.QWidget):
    def __init__(self, nm, maxPower):
        super().__init__()
        self.ui = Ui_DiodSettings()
        self.ui.setupUi(self)
        self.power = 0.0
        self.maxPower = maxPower
        
        self.ui.nmLabel.setText(nm)
        self.ui.IncrementPowerButton.clicked.connect(self.incrementPower)
        self.ui.DecrementPowerButton.clicked.connect(self.decrementPower)
        self.ui.CWRadioButton.clicked.connect(self.pulseSelection)
        self.ui.SingleRadioButton.clicked.connect(self.pulseSelection)
        self.ui.RepeatRadioButton.clicked.connect(self.pulseSelection)

    def pulseSelection(self):
        if self.ui.CWRadioButton.isChecked():
            print("CW Pulse")
        if self.ui.SingleRadioButton.isChecked():
            print("Single Pulse")
        if self.ui.RepeatRadioButton.isChecked():
            print("Reapeat Pulse")

    def incrementPower(self):
        if self.power >= self.maxPower:
            return
        self.power = self.power + 1.0
        self.ui.PowerLabel.setText(f"{self.power} Watt")
        
    def decrementPower(self):
        if self.power <= 0.0:
            return
        self.power = self.power - 1.0
        self.ui.PowerLabel.setText(f"{self.power} Watt")
        


if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())