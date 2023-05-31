"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # self.pb = QtWidgets.QPushButton("<h1>Кнопка</h1>", self)
        self.initUi()

    def initUi(self):
        self.label = QtWidgets.QLabel("-----")
        self.label.installEventFilter(self)
        self.label.setText("<h1 style='color: red'> Нестандартная </h1><h1 style='color: blue'> кнопка </h1>")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("border: 1px solid black")
        # self.label.setFont(QtGui.QFont())

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.label and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                print("Нажата левая кнопка мыши")
            if event.button() == QtCore.Qt.MouseButton.RightButton:
                print("Нажата правая кнопка мыши")

        return super(Window, self).event(watched, event)




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
