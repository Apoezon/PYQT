from PySide6 import QtWidgets, QtCore

class MyFirstWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def initUi(self) -> None:
        """
        Доинициализация Ui
        :return:
        """
        # size = QtCore.QSize(250, 150)
        # self.setFixedSize(size)
        self.setWindowTitle('Моя Первая Программа')
        size = self.size()
        print(size)
        # self.show() # лучше так не делать

    def initSignals(self) -> None:
        """
        инициализация сигналов
        :return:
        """
    def initChild(self):
        pass

    def initDB(self):
        pass

    def initThreads(self):
        ...

if __name__=='__main__':
    app = QtWidgets.QApplication() # основной цикл приложения

    win_1 = MyFirstWindow()     # создает окно
    win_1.show()                # показывает окно

    app.exec()
