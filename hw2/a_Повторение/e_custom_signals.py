"""
Файл для повторения темы генерации сигналов и передачи данных из одного виджета в другой

Напомнить про работу с пользовательскими сигналами.

Предлагается создать 2 формы:
* На первый форме label с надписью "Пройдите регистрацию" и pushButton с текстом "Зарегистрироваться"
* На второй (QDialog) форме:
  * lineEdit с placeholder'ом "Введите логин"
  * lineEdit с placeholder'ом "Введите пароль"
  * pushButton "Зарегистрироваться"

  при нажатии на кнопку, данные из lineEdit'ов передаются в главное окно, в
  котором надпись "Пройдите регистрацию", меняется на "Добро пожаловать {данные из lineEdit с логином}"
  (пароль можно показать в терминале в захешированном виде)
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()

    def initUi(self):

        self.label = QtWidgets.QLabel("Пройдите регистрацию")
        self.pb = QtWidgets.QPushButton("Зарегистрироваться")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pb)

        self.setLayout(layout)

    def initSignals(self):
        self.pb.clicked.connect(self.showRegistrationDialog)

    def showRegistrationDialog(self):
        self.regDialog = RegistrationDialog()
        self.regDialog.registered.connect(self.userIsRegistered)
        self.regDialog.exec()

    def userIsRegistered(self, login_data: tuple):
        self.label.setText(f"Добро пожаловать {login_data[0]}")
        print(login_data[1])

class RegistrationDialog(QtWidgets.QDialog):
    registered = QtCore.Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self):
        self.leLogin = QtWidgets.QLineEdit()
        self.leLogin.setPlaceholderText("Введите логин")

        self.lePassword = QtWidgets.QLineEdit()
        self.lePassword.setPlaceholderText("Введите пароль")
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.pbRegistration = QtWidgets.QPushButton("Зарегистрироваться")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.leLogin)
        layout.addWidget(self.lePassword)
        layout.addWidget(self.pbRegistration)

        self.setLayout(layout)

    def initSignals(self):
        self.pbRegistration.clicked.connect(self.onPBClicked)

    def onPBClicked(self):
        print(self.leLogin.text())
        print(self.lePassword.text())
        self.registered.emit((self.leLogin.text(), self.lePassword.text()))
        self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    # window.registered.connect(lambda signal_value: print(signal_value))
    window.show()

    app.exec()
