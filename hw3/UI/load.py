# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QProgressBar, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(170, 210)
        Form.setMaximumSize(QSize(170, 210))
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.delayLabel = QLabel(Form)
        self.delayLabel.setObjectName(u"delayLabel")

        self.horizontalLayout_2.addWidget(self.delayLabel)

        self.delayComboBox = QComboBox(Form)
        self.delayComboBox.setObjectName(u"delayComboBox")

        self.horizontalLayout_2.addWidget(self.delayComboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cpuProgressBar = QProgressBar(self.groupBox)
        self.cpuProgressBar.setObjectName(u"cpuProgressBar")
        self.cpuProgressBar.setMinimumSize(QSize(50, 100))
        self.cpuProgressBar.setMaximumSize(QSize(50, 100))
        self.cpuProgressBar.setValue(24)
        self.cpuProgressBar.setOrientation(Qt.Vertical)

        self.verticalLayout.addWidget(self.cpuProgressBar)

        self.cpuLabel = QLabel(self.groupBox)
        self.cpuLabel.setObjectName(u"cpuLabel")

        self.verticalLayout.addWidget(self.cpuLabel)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ramProgressBar = QProgressBar(self.groupBox_2)
        self.ramProgressBar.setObjectName(u"ramProgressBar")
        self.ramProgressBar.setMinimumSize(QSize(50, 100))
        self.ramProgressBar.setMaximumSize(QSize(50, 100))
        self.ramProgressBar.setValue(24)
        self.ramProgressBar.setOrientation(Qt.Vertical)

        self.verticalLayout_2.addWidget(self.ramProgressBar)

        self.ramLabel = QLabel(self.groupBox_2)
        self.ramLabel.setObjectName(u"ramLabel")

        self.verticalLayout_2.addWidget(self.ramLabel)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Load", None))
        self.delayLabel.setText(QCoreApplication.translate("Form", u"Delay, s", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"CPU", None))
        self.cpuLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"RAM", None))
        self.ramLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

