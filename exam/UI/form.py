# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form.ui'
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
    QSizePolicy, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(692, 582)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.delayLabel = QLabel(Form)
        self.delayLabel.setObjectName(u"delayLabel")

        self.horizontalLayout.addWidget(self.delayLabel)

        self.delayComboBox = QComboBox(Form)
        self.delayComboBox.setObjectName(u"delayComboBox")

        self.horizontalLayout.addWidget(self.delayComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabCPU = QWidget()
        self.tabCPU.setObjectName(u"tabCPU")
        self.horizontalLayout_2 = QHBoxLayout(self.tabCPU)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEditCPU = QTextEdit(self.tabCPU)
        self.textEditCPU.setObjectName(u"textEditCPU")

        self.horizontalLayout_2.addWidget(self.textEditCPU)

        self.tabWidget.addTab(self.tabCPU, "")
        self.tabRAM = QWidget()
        self.tabRAM.setObjectName(u"tabRAM")
        self.horizontalLayout_3 = QHBoxLayout(self.tabRAM)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textEditRAM = QTextEdit(self.tabRAM)
        self.textEditRAM.setObjectName(u"textEditRAM")

        self.horizontalLayout_3.addWidget(self.textEditRAM)

        self.tabWidget.addTab(self.tabRAM, "")
        self.tabHDD = QWidget()
        self.tabHDD.setObjectName(u"tabHDD")
        self.horizontalLayout_4 = QHBoxLayout(self.tabHDD)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textEditHDD = QTextEdit(self.tabHDD)
        self.textEditHDD.setObjectName(u"textEditHDD")

        self.horizontalLayout_4.addWidget(self.textEditHDD)

        self.tabWidget.addTab(self.tabHDD, "")
        self.tabProcesses = QWidget()
        self.tabProcesses.setObjectName(u"tabProcesses")
        self.horizontalLayout_5 = QHBoxLayout(self.tabProcesses)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textEditProcesses = QTextEdit(self.tabProcesses)
        self.textEditProcesses.setObjectName(u"textEditProcesses")

        self.horizontalLayout_5.addWidget(self.textEditProcesses)

        self.tabWidget.addTab(self.tabProcesses, "")
        self.tabServices = QWidget()
        self.tabServices.setObjectName(u"tabServices")
        self.horizontalLayout_6 = QHBoxLayout(self.tabServices)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.textEditServices = QTextEdit(self.tabServices)
        self.textEditServices.setObjectName(u"textEditServices")

        self.horizontalLayout_6.addWidget(self.textEditServices)

        self.tabWidget.addTab(self.tabServices, "")
        self.tabScheduler = QWidget()
        self.tabScheduler.setObjectName(u"tabScheduler")
        self.horizontalLayout_7 = QHBoxLayout(self.tabScheduler)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.textEditScheduler = QTextEdit(self.tabScheduler)
        self.textEditScheduler.setObjectName(u"textEditScheduler")

        self.horizontalLayout_7.addWidget(self.textEditScheduler)

        self.tabWidget.addTab(self.tabScheduler, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.delayLabel.setText(QCoreApplication.translate("Form", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f, \u0441", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCPU), QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRAM), QCoreApplication.translate("Form", u"\u041e\u0417\u0423", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHDD), QCoreApplication.translate("Form", u"\u041f\u0417\u0423", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProcesses), QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabServices), QCoreApplication.translate("Form", u"\u0421\u043b\u0443\u0436\u0431\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabScheduler), QCoreApplication.translate("Form", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a", None))
    # retranslateUi

