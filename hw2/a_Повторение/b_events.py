
"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль.
При выводе события указывать время, когда произошло событие.
"""
import time

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.textEdit = QtWidgets.QTextEdit(self)


    def event(self, event: QtCore.QEvent) -> bool:
        print(time.ctime(), event.type())
        if event.type() == QtCore.QEvent.Type.Resize:
            print(event.size())

        return super(Window, self).event(event)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(event.oldPos(), ">>>", event.pos())



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
