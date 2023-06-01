"""
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
import time, subprocess
from pprint import pprint

import psutil, cpuinfo, os

from PySide6 import QtCore, QtWidgets
from UI.form import Ui_Form


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        """
        Переопределяем метод run и закидываем в него данные из различных сервисов информации и
        с помощью метода .emit передаем в виде словаря данные о системе
        :return: None
        """
        if self.delay is None:
            self.delay = 1

        while True:
            # CPU data
            cpu_name = cpuinfo.get_cpu_info()['brand_raw']  # Название процессора
            core_number = os.cpu_count()                    # количество ядер
            cpu_value = psutil.cpu_percent()                # текущая загрузка

            # RAM data
            ram_total = psutil.virtual_memory().total       # общий объем
            ram_value = psutil.virtual_memory().percent     # текущая загрузка

            # HDD data
            # воспользуемся утилитой WMIC и библиотекой subprocess
            disk_command = "WMIC DISKDRIVE GET caption, index, model, size, interfacetype /VALUE".split()
            disk_command_response = str(subprocess.check_output(disk_command, shell=True)).strip().split('\\n')

            iterator = iter(disk_command_response)

            disk_list = []
            disk_dict_info = {}
            try:
                while True:
                    next_val = next(iterator)
                    # print(next_val)
                    if 'Caption=' in next_val:
                        disk_dict_info = {}
                        disk_dict_info['Caption'] = next_val.split("\\r")[0].split("=")[1]
                    elif 'Index=' in next_val:
                        disk_dict_info['Index'] = next_val.split("\\r")[0].split("=")[1]
                    elif 'InterfaceType=' in next_val:
                        disk_dict_info['InterfaceType'] = next_val.split("\\r")[0].split("=")[1]
                    elif 'Model=' in next_val:
                        disk_dict_info['Model'] = next_val.split("\\r")[0].split("=")[1]
                    elif 'Size=' in next_val:
                        disk_dict_info['Size'] = next_val.split("\\r")[0].split("=")[1]
                        disk_list.append(disk_dict_info)

            except StopIteration:
                pass

            # PARTITIONS data
            partitions_list = []
            partitions = psutil.disk_partitions()
            for partition in partitions:
                partition_dict_info = {}
                # print(partition.device, partition.mountpoint, partition.fstype)
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    # this can be catched due to the disk that
                    # isn't ready
                    continue
                partition_dict_info['mountpoint'] = partition.mountpoint
                partition_dict_info['fstype'] = partition.fstype
                partition_dict_info['total_volume'] = partition_usage.total
                partition_dict_info['used_volume'] = partition_usage.used
                partition_dict_info['used_volume_percent'] = partition_usage.percent

                partitions_list.append(partition_dict_info)

                # print(partition_usage.total, partition_usage.used, partition_usage.percent)
            # print(partitions_list)

            # PROCESSES
            process_list = []
            for proc in psutil.process_iter():
                try:
                    process_name = proc.name()
                    process_id = proc.pid
                    process_list.append([process_id, process_name])
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            # SERVICES
            service_list = []
            service_command = "sc query type=service state=all".split()
            service_command_response = str(subprocess.check_output(service_command, shell=True)).strip().split('\\r\\n')

            iterator = iter(service_command_response)

            try:
                while True:
                    next_val = next(iterator)
                    if 'SERVICE_NAME:' in next_val:
                        service_list.append(next_val.split("\\r")[0].split(": ")[1])
                    elif '\x88\xac\xef_\xe1\xab\xe3\xa6\xa1\xeb' in next_val:
                        service_list.append(next_val.split("\\r")[0].split(": ")[1])

            except StopIteration:
                pass

            self.systemInfoReceived.emit({
                'cpu': [cpu_name, core_number, cpu_value],
                'ram': [ram_total, ram_value],
                'hdd': disk_list,
                'logic_drives': partitions_list,
                'processes': process_list,
                'services': service_list
            })
            time.sleep(self.delay)

class WindowLoad(QtWidgets.QWidget):
    """
    Класс подключает форму form.py
    """

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
        """
        Инициализирует потоки
        :return: None
        """
        self.thread = SystemInfo()
        self.thread.start()

    def initSignals(self) -> None:
        """
        Инициализирует сигналы:
        - от потока thread с помощью метода setValues
        - oт виджета delayComboBox для установки задержки с помощью метода setDelay
        :return: None
        """
        self.thread.systemInfoReceived.connect(self.setValues)
        self.ui.delayComboBox.currentTextChanged.connect(self.setDelay)
        ...

    def setDelay(self) -> None:
        """
        Определяет задержку отображения информации, получая данные из delayComboBox
        :return: None
        """
        delayChanged = int(self.ui.delayComboBox.currentText())
        self.thread.delay = delayChanged


    def setValues(self, systemInfoReceived) -> None:
        """
        Передает данные в различные виджеты
        :param systemInfoReceived: передаваемые значения из потока thread
        :return: None
        """

        # CPU
        self.ui.textEditCPU.setText(f"Название процессора: {systemInfoReceived['cpu'][0]}")
        self.ui.textEditCPU.append(f"Количество ядер: {systemInfoReceived['cpu'][1]}")
        self.ui.textEditCPU.append(f"Загрузка процессора: {systemInfoReceived['cpu'][2]} %")

        # RAM
        total_ram_in_gb = round(systemInfoReceived['ram'][0]/(1024*1024*1024), 2)
        self.ui.textEditRAM.setText(f"Общий объем памяти: {total_ram_in_gb} ГБ ({systemInfoReceived['ram'][0]} байт)")
        self.ui.textEditRAM.append(f"Сейчас загружено: {systemInfoReceived['ram'][1]} %")

        # PROCESSES
        for i in systemInfoReceived['processes']:
            self.ui.textEditProcesses.append(f"{i[0]}\t{i[1]}")

        # HDD
        self.ui.textEditHDD.clear()
        for i in systemInfoReceived['hdd']:
            if i['Size'] != '':
                self.ui.textEditHDD.append(f"Жесткий диск {i['Index']}: {i['Model']}")
                total_rom_in_gb = round(int(i['Size']) / (1024 * 1024 * 1024), 2)
                self.ui.textEditHDD.append(f"Размер: {total_rom_in_gb} ГБ  ({i['Size']} Б)\n")

        # PARTITIONS
        for i in systemInfoReceived['logic_drives']:
            self.ui.textEditHDD.append(f"Логический диск: {i['mountpoint']}")
            self.ui.textEditHDD.append(f"Тип файловой системы: {i['fstype']}")
            total_volume_in_gb = round(i['total_volume']/(1024*1024*1024), 2)
            self.ui.textEditHDD.append(f"Размер диска: {total_volume_in_gb} ГБ ({i['total_volume']} байт)")
            self.ui.textEditHDD.append(f"Занято: {i['used_volume_percent']} %\n")

        # SERVICES
        self.ui.textEditServices.clear()
        for i in systemInfoReceived['services']:
            self.ui.textEditServices.append(f"{i}")

        # SCHEDULER
        self.ui.textEditScheduler.setText("Пока ничего не запланировано!")


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = WindowLoad()
    window.show()
    app.exec()