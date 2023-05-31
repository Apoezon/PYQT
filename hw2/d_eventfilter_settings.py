"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtGui, QtCore

from hw2.ui.d_eventfilter_settings import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem("dec")
        self.ui.comboBox.addItem("oct")
        self.ui.comboBox.addItem("hex")
        self.ui.comboBox.addItem("bin")
        self.initSignals()

        settings = QtCore.QSettings("d_eventfilter_settings")
        saved_value = int(settings.value("saved_value", 0))
        cb_value = settings.value("combo_box_value", "dec")
        # print(saved_value, cb_value)
        self.ui.comboBox.setCurrentText(cb_value)
        self.ui.dial.setValue(saved_value)
        self.ui.lcdNumber.display(saved_value)
        self.ui.horizontalSlider.setValue(saved_value)

    def initSignals(self):
        self.ui.horizontalSlider.valueChanged.connect(self.onSliderMoved)
        self.ui.dial.valueChanged.connect(self.onDialMoved)
        self.ui.comboBox.currentTextChanged.connect(self.comboBoxChanged)
        ...

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.text() == "+":
            # print(event)
            self.ui.dial.setValue(int(self.ui.dial.value())+1)
        elif event.text() == "-":
            # print(event)
            self.ui.dial.setValue(int(self.ui.dial.value())-1)

    def comboBoxChanged(self):
        if self.ui.comboBox.currentText() == "dec":
            self.ui.lcdNumber.setDecMode()
        elif self.ui.comboBox.currentText() == "oct":
            self.ui.lcdNumber.setOctMode()
        elif self.ui.comboBox.currentText() == "hex":
            self.ui.lcdNumber.setHexMode()
        elif self.ui.comboBox.currentText() == "bin":
            self.ui.lcdNumber.setBinMode()

        ...


    def onSliderMoved(self):
        pos = self.ui.horizontalSlider.value()
        self.ui.dial.setSliderPosition(pos)
        self.ui.lcdNumber.display(pos)

    def onDialMoved(self):
        pos = self.ui.dial.value()
        self.ui.horizontalSlider.setSliderPosition(pos)
        self.ui.lcdNumber.display(pos)
        ...

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        settings = QtCore.QSettings("d_eventfilter_settings")
        # print(settings.fileName())
        value = self.ui.lcdNumber.value()
        cb_value = self.ui.comboBox.currentText()
        # print(value)
        # print(cb_value)
        settings.setValue("saved_value", value)
        settings.setValue("combo_box_value", cb_value)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
