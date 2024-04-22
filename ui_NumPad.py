# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NumPad.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 378)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_6 = QPushButton(Form)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_7 = QPushButton(Form)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_7, 2, 0, 1, 1)

        self.btn_5 = QPushButton(Form)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_8 = QPushButton(Form)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_8, 2, 1, 1, 1)

        self.btn_2 = QPushButton(Form)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_9 = QPushButton(Form)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_9, 2, 2, 1, 1)

        self.btn_4 = QPushButton(Form)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_1 = QPushButton(Form)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_3 = QPushButton(Form)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_3, 0, 2, 1, 1)

        self.btn_0 = QPushButton(Form)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_0, 3, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btn_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btn_0.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

