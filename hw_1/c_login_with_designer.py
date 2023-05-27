from PySide6 import QtWidgets, QtCore

from hw_1.UI.login_form import Ui_LoginForm


class MyFirstWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)



if __name__=='__main__':
    app = QtWidgets.QApplication() # основной цикл приложения

    win_1 = MyFirstWindow()     # создает окно
    win_1.show()                # показывает окно

    app.exec()
