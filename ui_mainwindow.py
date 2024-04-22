# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNumpad_Linear = QAction(MainWindow)
        self.actionNumpad_Linear.setObjectName(u"actionNumpad_Linear")
        self.actionNumpad = QAction(MainWindow)
        self.actionNumpad.setObjectName(u"actionNumpad")
        self.actionFull = QAction(MainWindow)
        self.actionFull.setObjectName(u"actionFull")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_input = QTextEdit(self.centralwidget)
        self.txt_input.setObjectName(u"txt_input")

        self.verticalLayout.addWidget(self.txt_input)

        self.KeyboardLayout = QVBoxLayout()
        self.KeyboardLayout.setObjectName(u"KeyboardLayout")

        self.verticalLayout.addLayout(self.KeyboardLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuShow_NumPad = QMenu(self.menubar)
        self.menuShow_NumPad.setObjectName(u"menuShow_NumPad")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuShow_NumPad.menuAction())
        self.menuShow_NumPad.addAction(self.actionNumpad_Linear)
        self.menuShow_NumPad.addAction(self.actionNumpad)
        self.menuShow_NumPad.addAction(self.actionFull)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNumpad_Linear.setText(QCoreApplication.translate("MainWindow", u"Numpad Linear", None))
        self.actionNumpad.setText(QCoreApplication.translate("MainWindow", u"Numpad", None))
        self.actionFull.setText(QCoreApplication.translate("MainWindow", u"Full", None))
        self.txt_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Fira Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.menuShow_NumPad.setTitle(QCoreApplication.translate("MainWindow", u"Show Keyboard", None))
    # retranslateUi

