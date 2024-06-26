# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QButtonGroup, QPushButton

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_VirtualKeyboard
from ui_mainwindow import Ui_MainWindow
from ui_NumPad import Ui_Form


class NumPad(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.btn_grp = QButtonGroup()
        self.make_btn_grp()

    def make_btn_grp(self):
        buttons = (self.ui.gridLayout.itemAt(i).widget() for i in range(self.ui.gridLayout.count()))
        for btn in buttons:
            self.btn_grp.addButton(btn)


class LinearNumpad(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VirtualKeyboard()
        self.ui.setupUi(self)
        self.parent = parent
        self.btn_grp = QButtonGroup()
        self.make_btn_grp()

    def make_btn_grp(self):
        buttons = (self.ui.gridLayout.itemAt(i).widget() for i in range(self.ui.gridLayout.count()))
        for btn in buttons:
            self.btn_grp.addButton(btn)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.linear_numpad = LinearNumpad(self)
        self.ui.actionNumpad_Linear.triggered.connect(self.show_linear_numpad)
        self.linear_numpad_isShown = False
        self.linear_numpad.btn_grp.buttonClicked.connect(self.recv_key)
        self.numpad = NumPad(self)
        self.numpad.btn_grp.buttonClicked.connect(self.recv_key)
        self.ui.actionNumpad.triggered.connect(self.show_numpad)
        self.setup_keyboards()

    def setup_keyboards(self):
        # This adds the keyboard widget to the main window and hides it
        keyboard_layout = self.ui.centralwidget.layout().itemAt(1)
        keyboard_layout.layout().addWidget(self.linear_numpad)
        w = keyboard_layout.layout().itemAt(0)
        w.widget().hide()

    def recv_key(self, key):
        current_txt = self.ui.txt_input.toPlainText()
        self.ui.txt_input.setPlainText(current_txt + key.text())

    def show_linear_numpad(self):
        main_layout = self.ui.centralwidget.layout().itemAt(1)
        keyboard = main_layout.layout().itemAt(0).widget()
        if not self.linear_numpad_isShown:
            print("Show Keyboard")
            keyboard.show()
        if self.linear_numpad_isShown:
            print("Hide Keyboard")
            keyboard.hide()
        self.linear_numpad_isShown = not self.linear_numpad_isShown

    def show_numpad(self):
        self.numpad.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
