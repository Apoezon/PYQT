"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""
import time
import requests
from PySide6 import QtWidgets, QtCore
from hw3.UI.weather_form import Ui_WeatherForm
from a_threads import WeatherHandler


class WeatherWindow(QtWidgets.QWidget):
    lat = 25.214356
    lon = 55.428693


    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.ui = Ui_WeatherForm()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem("3")
        self.ui.comboBox.addItem("5")
        self.ui.comboBox.addItem("10")
        self.ui.latLineEdit.setText(str(self.lat))
        self.ui.lonLineEdit.setText(str(self.lon))
        self.ui.statusLabel.setText("Введите Ваши данные широты и долготы!")


        self.initSignals()

    def initSignals(self) -> None:
        """
        Инициируем сигналы
        :return:
        """
        # startPushButton pressed

        self.ui.startPushButton.clicked.connect(self.getData) # -> запускает поток


        self.thread.weatherInfoReceived.connect(self.setValues)
        self.thread.started.connect(self.ui.statusLabel.setText('Получаем данные'))
        self.thread.finished.connect(self.ui.statusLabel.setText('Введите Ваши данные широты и долготы!'))
        self.ui.comboBox.currentTextChanged.connect(self.thread.setDelay(int(self.ui.comboBox.currentText())))
        #stopPushButton
        self.ui.stopPushButton.clicked.connect(self.stopIt)


    def setValues(self, weatherInfoReceived) -> None:
        """
        Устанавливаем записываем данные в поле textEdit
        :param weatherInfoReceived: данные из потока
        :return: None
        """

        lat_recieved = weatherInfoReceived['latitude']
        lon_recieved = weatherInfoReceived['longitude']


        self.ui.textEdit.setText(f'Погода для координат\nШирота: {lat_recieved}\tДолгота: {lon_recieved}\n')

        temperature = weatherInfoReceived['current_weather']['temperature']
        self.ui.textEdit.append(f"Температура, C: {temperature}")
        windspeed = weatherInfoReceived['current_weather']['windspeed']
        winddirection = weatherInfoReceived['current_weather']['winddirection']
        self.ui.textEdit.append(f"Ветер, км/ч: {windspeed} направление: {winddirection}")
        self.ui.textEdit.append(f"Данные по времени:")
        self.ui.textEdit.append(f"Время\t\tТемпература\tВлажность\tИндекс УФ")
        for i in range(24):
            self.ui.textEdit.append(f"{weatherInfoReceived['hourly']['time'][i]}\t{weatherInfoReceived['hourly']['temperature_2m'][i]}\t{weatherInfoReceived['hourly']['relativehumidity_2m'][i]}\t{weatherInfoReceived['hourly']['uv_index'][i]}")

    def initThreads(self) -> None:
        """
        Инициализация потока
        :return: None
        """
        self.thread = WeatherHandler()

    # startPushButton pressed
    def getData(self) -> None:
        """
        Запуск потока для получения данных о погоде
        :return: None
        """
        self.thread.setCoordinates(float(self.ui.latLineEdit.text()), float(self.ui.lonLineEdit.text()))

        if self.coordinates_correct():

            # self.thread.setCoordinates(float(self.ui.latLineEdit.text()), float(self.ui.lonLineEdit.text()))
            # print(float(self.ui.latLineEdit.text()), float(self.ui.lonLineEdit.text()))

            self.ui.startPushButton.setEnabled(False)
            self.ui.latLineEdit.setEnabled(False)
            self.ui.lonLineEdit.setEnabled(False)
            self.ui.comboBox.setEnabled(False)

            delay_value = int(self.ui.comboBox.currentText())
            self.thread.setDelay(delay_value)
            self.thread.setStatus(True)



            # self.thread.lat = float(self.ui.latLineEdit.text())
            # self.thread.lon = float(self.ui.lonLineEdit.text())

            self.ui.statusLabel.setText("Получаем данные!")
            self.thread.start()
        else:
            self.ui.statusLabel.setText("Координаты не корректны!")

    def coordinates_correct(self):
        """
        Функция проверяет корректность введеных в поля latLineEdit и lonLineEdit координат
        :return:
        """
        lat_check = self.ui.latLineEdit.text()
        lon_check = self.ui.lonLineEdit.text()
        if self.is_number(lat_check, 90) and self.is_number(lon_check, 180):
            are_correct = True
        else:
            are_correct = False
        return are_correct

    def is_number(self, str_value, range) -> bool:
        """
        Проверяет правильность ввода координат: они дожны быть числами и не превышать значений +/-90 для широты и
        +/- 180 для долготы.
        :param str_value: строка
        :param range: число, которое не должно превышать
        :return: True, если значения координат правильные
        """
        try:
            num = float(str_value)
            if -range < num < range:
                return True
            else:
                return False
        except ValueError:
            return False


    def stopIt(self) -> None:
        """
        Останавливаем поток путем изменения атрибута __status = 0
        :return: None
        """
        self.ui.startPushButton.setEnabled(True)
        self.ui.latLineEdit.setEnabled(True)
        self.ui.lonLineEdit.setEnabled(True)
        self.ui.comboBox.setEnabled(True)
        self.thread.setStatus(0)


class WeatherHandler(QtCore.QThread):
    weatherInfoReceived = QtCore.Signal(dict)

    def __init__(self, parent=None): #
        super().__init__(parent)

        self.__lat = None #/ 25.214356
        self.__lon = None #/ 55.428693
        self.__delay = 10
        self.__status = None

        self.url = None # f"https://api.open-meteo.com/v1/forecast?latitude={self.lat}&longitude={self.lon}&hourly=temperature_2m,relativehumidity_2m,uv_index&current_weather=true"
        print(self.url)



    def setDelay(self, delay) -> None:
        """
        Устанавливаем атрибут delay
        :param delay:
        :return:
        """
        self.__delay = delay

    def setStatus(self, val):
        """
        Устанавливаем атрибут status
        :param val:
        :return:
        """
        self.__status = val
    def setCoordinates(self, lat, lon):
        self.__lat = lat
        self.__lon = lon
        self.url = f"https://api.open-meteo.com/v1/forecast?latitude={self.__lat}&longitude={self.__lon}&hourly=temperature_2m,relativehumidity_2m,uv_index&current_weather=true"

    def run(self) -> None:
        while self.__status:
            response = requests.get(self.url) #, headers=self.headers, params=self.querystring)
            data = response.json()
            print(data)
            self.weatherInfoReceived.emit(data)
            time.sleep(self.__delay)

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = WeatherWindow()
    window.show()
    app.exec()