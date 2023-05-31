"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time

# cd hw2\ui
# pyside6-uic c_signals_events.ui -o c_signals_events_form.ui



from PySide6 import QtWidgets, QtCore, QtGui
from hw2.ui.c_signals_events_form import Ui_Form

class Window(QtWidgets.QWidget):


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self):
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoordsClicked)
        self.ui.pushButtonLT.clicked.connect(self.onPushButtonLTClicked)
        self.ui.pushButtonRT.clicked.connect(self.onPushButtonRTClicked)
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonLBClicked)
        self.ui.pushButtonRB.clicked.connect(self.onPushButtonRBClicked)
        self.ui.pushButtonCenter.clicked.connect(self.onPushButtonCenter)

        ...

    def onPushButtonGetDataClicked(self):
        self.ui.plainTextEdit.setPlainText(str(time.ctime()) + " Количество экранов:\t\t" + str(len(QtWidgets.QApplication.screens())))
        self.ui.plainTextEdit.appendPlainText(str(time.ctime()) + " Текущее основное окно:\t\t" + str(QtWidgets.QApplication.activeWindow().windowTitle()))
        self.ui.plainTextEdit.appendPlainText(str(time.ctime()) + " Разрешение экрана:\t\t" + str(QtWidgets.QApplication.primaryScreen().size().width())+" x "+str(QtWidgets.QApplication.primaryScreen().size().height()))
        self.ui.plainTextEdit.appendPlainText(str(time.ctime()) + " окно находится на экране:\t\t" + str(QtWidgets.QApplication.primaryScreen().name())) #primaryScreen()
        self.ui.plainTextEdit.appendPlainText(str(time.ctime()) + " Размеры окна:\t\t\t" + str(self.size().width()) +" x "+ str(self.size().height()))
        self.ui.plainTextEdit.appendPlainText(str(time.ctime()) + " Минимальные размеры окна:\t\t" + str(self.minimumSize().width()) + " x "+ str(self.minimumSize().height()))
        self.ui.plainTextEdit.appendPlainText(str(time.ctime()) + " Текущее положение (координаты) окна:\t" + str(self.pos().x()) + " x "+ str(self.pos().y()))
        self.ui.plainTextEdit.appendPlainText(str(time.ctime()) + " Координаты центра приложения:\t" + str(self.rect().center().x())+" x "+str(self.rect().center().y()))
        # self.ui.plainTextEdit.appendPlainText(str(time.ctime()) + " Состояние окна:\t\t\t" + str(self.windowState().name))

    def onPushButtonMoveCoordsClicked(self):
        x, y = int(self.ui.spinBoxX.text()), int(self.ui.spinBoxY.text())
        print(x, y)
        self.move(x, y)

    def onPushButtonLTClicked(self):
        screenGeometry = QtWidgets.QApplication.primaryScreen().geometry()
        appGeometry = self.geometry()
        print(screenGeometry.topLeft(), appGeometry, screenGeometry.topRight())
        self.move(screenGeometry.topLeft())
        ...

    def onPushButtonRTClicked(self):
        screenGeometry = QtWidgets.QApplication.primaryScreen().geometry()
        appGeometry = self.geometry()
        self.move(screenGeometry.right() - appGeometry.width(), 0)
        ...

    def onPushButtonLBClicked(self):
        screenGeometry = QtWidgets.QApplication.primaryScreen().geometry()
        appGeometry = self.geometry()
        self.move(0, screenGeometry.bottom() - appGeometry.height()-66)
        ...

    def onPushButtonRBClicked(self):
        screenGeometry = QtWidgets.QApplication.primaryScreen().geometry()
        appGeometry = self.geometry()
        self.move(screenGeometry.right() - appGeometry.width(), screenGeometry.bottom() - appGeometry.height()-66)
        ...

    def onPushButtonCenter(self):
        screenGeometry = QtWidgets.QApplication.primaryScreen().geometry()
        appGeometry = self.geometry()
        self.move(screenGeometry.center().x()-self.width()//2, screenGeometry.center().y()-self.height()//2-19)
        ...


    # def getWindowSize(self):
    #     self.ui.plainTextEdit.appendPlainText(str(self.size()))
    #     print(str(self.size()))

    # def event(self, event: QtCore.QEvent) -> bool:
    #     # print(time.ctime(), event)
    #     if event.type() == QtCore.QEvent.Type.Resize:
    #         self.ui.plainTextEdit.appendPlainText(str(time.ctime())+" "+str(event.size()))
    #         print(event.size())
    #     # if event.type() == QtCore.QEvent.Type.Move:
    #     #     self.ui.plainTextEdit.appendPlainText(str(time.ctime()) + " " + str(event.))
    #     #     print(event.size())
    #     return super(Window, self).event(event)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        self.ui.plainTextEdit.appendPlainText(str(time.ctime()) +
                                              "\tПозиция изменилась\t"+ " " +
                                              str(event.oldPos().x())+" : "+str(event.oldPos().y())
                                              + " >>>>> " +
                                              str(event.pos().x())+" : "+str(event.pos().y()))


    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self.ui.plainTextEdit.appendPlainText(str(time.ctime()) +
                                              "\tРазмер изменился\t"+ " " +
                                              str(event.oldSize().width())+" x "+str(event.oldSize().height())
                                              + " >>>>> " +
                                              str(event.size().width())+" x "+str(event.size().height()))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
