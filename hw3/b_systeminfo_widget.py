"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки

######################## З А Ч Е Т ############################

Задача.

Разработать приложение для мониторинга нагрузки системы и системных процессов (аналог диспетчера задач).

Обязательные функции в приложении:

Показ общих сведений о системе (в текстовом виде!):
Название процессора, количество ядер, текущая загрузка
Общий объём оперативной памяти, текущая загрузка оперативаной памяти
Количество, жестких дисков + информация по каждому (общий/занятый объём)
Обеспечить динамический выбор обновления информации (1, 5, 10, 30 сек.)
Показ работающих процессов
Показ работающих служб
Показ задач, которые запускаются с помощью планировщика задач


"""
import time

import psutil
from PySide6 import QtWidgets, QtCore
from hw3.UI.load import Ui_Form

class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)  #  Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None  #  создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def run(self) -> None:  #  переопределить метод run
        if self.delay is None:  #  Если задержка не передана в поток перед его запуском
            self.delay = 1  #  то устанавливайте значение 1

        while True:  #  Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory().percent  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            self.systemInfoReceived.emit([cpu_value, ram_value])  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            print(self.delay)
            time.sleep(self.delay)  # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay


class WindowLoad(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initThreads()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.delayComboBox.addItem("1")
        self.ui.delayComboBox.addItem("5")
        self.ui.delayComboBox.addItem("10")
        self.ui.delayComboBox.addItem("30")

        self.initSignals()



    def initThreads(self) -> None:
        self.thread = SystemInfo()
        self.thread.start()

    def initSignals(self):
        self.thread.systemInfoReceived.connect(self.setValues)
        self.ui.delayComboBox.currentTextChanged.connect(self.setDelay)
        ...

    def setDelay(self):
        delayChanged = int(self.ui.delayComboBox.currentText())
        self.thread.delay = delayChanged


    def setValues(self, systemInfoReceived):
        cpuValue = systemInfoReceived[0]
        ramValue = systemInfoReceived[1]
        self.ui.cpuLabel.setText(f"{str(cpuValue)} %")
        self.ui.cpuProgressBar.setValue(cpuValue)
        self.ui.ramLabel.setText(f"{str(ramValue)} %")
        self.ui.ramProgressBar.setValue(ramValue)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = WindowLoad()
    window.show()
    app.exec()