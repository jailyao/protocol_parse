import sys
from UI import main_window
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ =='__main__':
    QApplication.addLibraryPath('./')
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main_window.Ui_Mainwindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
