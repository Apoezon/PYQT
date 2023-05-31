import time
"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
        self.initSignals()

    def initUI(self) -> None:
        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirrow = QtWidgets.QLineEdit()
        self.lineEditMirrow.setReadOnly(True)

        self.pushButtonMirror = QtWidgets.QPushButton("Отзеркалить")
        self.pushButtonClearMirror = QtWidgets.QPushButton("Очистить результат")

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEditInput)
        layoutLineEdit.addWidget(self.lineEditMirrow)

        layoutPushButton = QtWidgets.QHBoxLayout()
        layoutPushButton.addWidget(self.pushButtonMirror)
        layoutPushButton.addWidget(self.pushButtonClearMirror)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addLayout(layoutPushButton)

        self.setLayout(layoutMain)

    def initSignals(self):
        self.pushButtonMirror.clicked.connect(self.mirrorText)
        self.pushButtonClearMirror.clicked.connect(self.lineEditMirrow.clear)

        self.lineEditInput.textChanged.connect(self.mirrorText)

        # widjet - signal - connect (ссылка на функция для вызова)


    def mirrorText(self):
        source_text = self.lineEditInput.text()
        self.lineEditMirrow.setText(source_text[::-1])




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
