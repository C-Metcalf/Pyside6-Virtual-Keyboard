# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_VirtualKeyboard(object):
    def setupUi(self, VirtualKeyboard):
        if not VirtualKeyboard.objectName():
            VirtualKeyboard.setObjectName(u"VirtualKeyboard")
        VirtualKeyboard.resize(800, 45)
        VirtualKeyboard.setMinimumSize(QSize(0, 45))
        VirtualKeyboard.setMaximumSize(QSize(16777215, 45))
        self.gridLayout = QGridLayout(VirtualKeyboard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_7 = QPushButton(VirtualKeyboard)
        self.btn_7.setObjectName(u"btn_7")

        self.gridLayout.addWidget(self.btn_7, 0, 7, 1, 1)

        self.btn_3 = QPushButton(VirtualKeyboard)
        self.btn_3.setObjectName(u"btn_3")

        self.gridLayout.addWidget(self.btn_3, 0, 3, 1, 1)

        self.btn_8 = QPushButton(VirtualKeyboard)
        self.btn_8.setObjectName(u"btn_8")

        self.gridLayout.addWidget(self.btn_8, 0, 8, 1, 1)

        self.btn_0 = QPushButton(VirtualKeyboard)
        self.btn_0.setObjectName(u"btn_0")

        self.gridLayout.addWidget(self.btn_0, 0, 0, 1, 1)

        self.btn_4 = QPushButton(VirtualKeyboard)
        self.btn_4.setObjectName(u"btn_4")

        self.gridLayout.addWidget(self.btn_4, 0, 4, 1, 1)

        self.btn_2 = QPushButton(VirtualKeyboard)
        self.btn_2.setObjectName(u"btn_2")

        self.gridLayout.addWidget(self.btn_2, 0, 2, 1, 1)

        self.btn_5 = QPushButton(VirtualKeyboard)
        self.btn_5.setObjectName(u"btn_5")

        self.gridLayout.addWidget(self.btn_5, 0, 5, 1, 1)

        self.btn_1 = QPushButton(VirtualKeyboard)
        self.btn_1.setObjectName(u"btn_1")

        self.gridLayout.addWidget(self.btn_1, 0, 1, 1, 1)

        self.btn_6 = QPushButton(VirtualKeyboard)
        self.btn_6.setObjectName(u"btn_6")

        self.gridLayout.addWidget(self.btn_6, 0, 6, 1, 1)

        self.btn_9 = QPushButton(VirtualKeyboard)
        self.btn_9.setObjectName(u"btn_9")

        self.gridLayout.addWidget(self.btn_9, 0, 9, 1, 1)


        self.retranslateUi(VirtualKeyboard)

        QMetaObject.connectSlotsByName(VirtualKeyboard)
    # setupUi

    def retranslateUi(self, VirtualKeyboard):
        VirtualKeyboard.setWindowTitle(QCoreApplication.translate("VirtualKeyboard", u"VirtualKeyboard", None))
        self.btn_7.setText(QCoreApplication.translate("VirtualKeyboard", u"7", None))
        self.btn_3.setText(QCoreApplication.translate("VirtualKeyboard", u"3", None))
        self.btn_8.setText(QCoreApplication.translate("VirtualKeyboard", u"8", None))
        self.btn_0.setText(QCoreApplication.translate("VirtualKeyboard", u"0", None))
        self.btn_4.setText(QCoreApplication.translate("VirtualKeyboard", u"4", None))
        self.btn_2.setText(QCoreApplication.translate("VirtualKeyboard", u"2", None))
        self.btn_5.setText(QCoreApplication.translate("VirtualKeyboard", u"5", None))
        self.btn_1.setText(QCoreApplication.translate("VirtualKeyboard", u"1", None))
        self.btn_6.setText(QCoreApplication.translate("VirtualKeyboard", u"6", None))
        self.btn_9.setText(QCoreApplication.translate("VirtualKeyboard", u"9", None))
    # retranslateUi

