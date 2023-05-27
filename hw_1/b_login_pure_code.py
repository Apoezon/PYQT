from PySide6 import QtWidgets, QtCore

class MyFirstWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui
        :return:
        """
        self.setWindowTitle("Вход в приложение")
        self.setFixedSize(350, 200)

        labelLogin = QtWidgets.QLabel("Логин")
        labelLogin.setMinimumWidth(45)
        labelPassword = QtWidgets.QLabel("Пароль")
        labelPassword.setMinimumWidth(45)
        self.lineEditLogin = QtWidgets.QLineEdit()
        self.lineEditLogin.setPlaceholderText("Введите логин")
        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.lineEditPassword.setPlaceholderText("Введите пароль")

        self.pushButtonRegistration = QtWidgets.QPushButton()
        self.pushButtonRegistration.setText("Registration")
        self.pushButtonOk = QtWidgets.QPushButton()
        self.pushButtonCancel = QtWidgets.QPushButton()
        self.pushButtonOk.setText("Ok")
        self.pushButtonCancel.setText("Cancel")

        #layouts
        layoutLogin = QtWidgets.QHBoxLayout()
        layoutLogin.addWidget(labelLogin)
        layoutLogin.addWidget(self.lineEditLogin)

        layoutPassword = QtWidgets.QHBoxLayout()
        layoutPassword.addWidget(labelPassword)
        layoutPassword.addWidget(self.lineEditPassword)

        layoutRegistration = QtWidgets.QHBoxLayout()
        layoutRegistration.addSpacerItem(QtWidgets.QSpacerItem(
            20, 10,
            QtWidgets.QSizePolicy.Policy.Expanding
        ))
        layoutRegistration.addWidget(self.pushButtonRegistration)

        layourHandle = QtWidgets.QHBoxLayout()
        layourHandle.addSpacerItem(QtWidgets.QSpacerItem(
            20, 10,
            QtWidgets.QSizePolicy.Policy.Expanding
        ))
        layourHandle.addWidget(self.pushButtonOk)
        layourHandle.addWidget(self.pushButtonCancel)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLogin)
        layoutMain.addLayout(layoutPassword)
        layoutMain.addSpacerItem(QtWidgets.QSpacerItem(
            10, 20, hData=QtWidgets.QSizePolicy.Policy.Expanding
        ))
        layoutMain.addLayout(layoutRegistration)
        layoutMain.addLayout(layourHandle)

        self.setLayout(layoutMain)


if __name__=='__main__':
    app = QtWidgets.QApplication() # основной цикл приложения

    win_1 = MyFirstWindow()     # создает окно
    win_1.show()                # показывает окно

    app.exec()
