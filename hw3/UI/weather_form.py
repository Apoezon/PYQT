# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather_form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_WeatherForm(object):
    def setupUi(self, WeatherForm):
        if not WeatherForm.objectName():
            WeatherForm.setObjectName(u"WeatherForm")
        WeatherForm.resize(500, 700)
        WeatherForm.setMinimumSize(QSize(500, 700))
        WeatherForm.setMaximumSize(QSize(500, 700))
        self.verticalLayout_2 = QVBoxLayout(WeatherForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.latLabel = QLabel(WeatherForm)
        self.latLabel.setObjectName(u"latLabel")

        self.horizontalLayout.addWidget(self.latLabel)

        self.latLineEdit = QLineEdit(WeatherForm)
        self.latLineEdit.setObjectName(u"latLineEdit")
        self.latLineEdit.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout.addWidget(self.latLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lonLabel = QLabel(WeatherForm)
        self.lonLabel.setObjectName(u"lonLabel")

        self.horizontalLayout_2.addWidget(self.lonLabel)

        self.lonLineEdit = QLineEdit(WeatherForm)
        self.lonLineEdit.setObjectName(u"lonLineEdit")
        self.lonLineEdit.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_2.addWidget(self.lonLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.statusLabel = QLabel(WeatherForm)
        self.statusLabel.setObjectName(u"statusLabel")

        self.verticalLayout_2.addWidget(self.statusLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rtLabel = QLabel(WeatherForm)
        self.rtLabel.setObjectName(u"rtLabel")
        self.rtLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.rtLabel)

        self.comboBox = QComboBox(WeatherForm)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.textEdit = QTextEdit(WeatherForm)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.startPushButton = QPushButton(WeatherForm)
        self.startPushButton.setObjectName(u"startPushButton")

        self.horizontalLayout_4.addWidget(self.startPushButton)

        self.stopPushButton = QPushButton(WeatherForm)
        self.stopPushButton.setObjectName(u"stopPushButton")

        self.horizontalLayout_4.addWidget(self.stopPushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(WeatherForm)

        QMetaObject.connectSlotsByName(WeatherForm)
    # setupUi

    def retranslateUi(self, WeatherForm):
        WeatherForm.setWindowTitle(QCoreApplication.translate("WeatherForm", u"WeatherForm", None))
        self.latLabel.setText(QCoreApplication.translate("WeatherForm", u"Latitude", None))
        self.latLineEdit.setText("")
        self.lonLabel.setText(QCoreApplication.translate("WeatherForm", u"Longide", None))
        self.lonLineEdit.setText("")
        self.statusLabel.setText(QCoreApplication.translate("WeatherForm", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.rtLabel.setText(QCoreApplication.translate("WeatherForm", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.startPushButton.setText(QCoreApplication.translate("WeatherForm", u"\u041f\u043e\u043b\u0443\u0447\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.stopPushButton.setText(QCoreApplication.translate("WeatherForm", u"\u041f\u0440\u0438\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0430\u0442\u044c \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435", None))
    # retranslateUi

