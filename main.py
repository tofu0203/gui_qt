# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from test import Ui_Form


class Test(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def slot1(self):  # イベント処理の関数
        self.ui.label.setText('Hello World!')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
