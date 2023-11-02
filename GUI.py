# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(400, 235)
        Dialog.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 361, 102))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.PathInputLabel = QLabel(self.verticalLayoutWidget)
        self.PathInputLabel.setObjectName(u"PathInputLabel")

        self.verticalLayout.addWidget(self.PathInputLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton = QToolButton(self.verticalLayoutWidget)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.OutputPathLabel = QLabel(self.verticalLayoutWidget)
        self.OutputPathLabel.setObjectName(u"OutputPathLabel")

        self.verticalLayout.addWidget(self.OutputPathLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolButton_2 = QToolButton(self.verticalLayoutWidget)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_2.addWidget(self.toolButton_2)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.convert = QPushButton(Dialog)
        self.convert.setObjectName(u"convert")
        self.convert.setGeometry(QRect(20, 170, 361, 51))
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(360, 130, 21, 21))
        self.horizontalSlider = QSlider(Dialog)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(90, 130, 261, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.Extensions = QComboBox(Dialog)
        self.Extensions.addItem("")
        self.Extensions.addItem("")
        self.Extensions.addItem("")
        self.Extensions.addItem("")
        self.Extensions.setObjectName(u"Extensions")
        self.Extensions.setGeometry(QRect(20, 130, 61, 22))
        self.Extensions.setLayoutDirection(Qt.LeftToRight)

        self.retranslateUi(Dialog)
        self.toolButton.clicked.connect(self.toolButton.showMenu)
        self.toolButton_2.clicked.connect(self.toolButton_2.showMenu)
        self.convert.clicked.connect(self.convert.click)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Webp\u306b\u3059\u308b\u3063\u3074\u30fc", None))
        self.PathInputLabel.setText(QCoreApplication.translate("Dialog", u"\u5909\u63db\u5143\u306e\u30d5\u30a9\u30eb\u30c0", None))
        self.toolButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.OutputPathLabel.setText(QCoreApplication.translate("Dialog", u"\u5909\u63db\u5f8c\u306e\u51fa\u529b\u5148", None))
        self.toolButton_2.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.convert.setText(QCoreApplication.translate("Dialog", u"\u5909\u63db", None))
        self.Extensions.setItemText(0, QCoreApplication.translate("Dialog", u"webp", None))
        self.Extensions.setItemText(1, QCoreApplication.translate("Dialog", u"jpg", None))
        self.Extensions.setItemText(2, QCoreApplication.translate("Dialog", u"png", None))
        self.Extensions.setItemText(3, QCoreApplication.translate("Dialog", u"bmp", None))

        self.Extensions.setCurrentText(QCoreApplication.translate("Dialog", u"webp", None))
    # retranslateUi


if __name__ == "__main__":
    # Qt Applicationを作成する
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    # formを作ってから表示する
    ui_dialog = Ui_Dialog()
    ui_dialog.show()

    # Qtループを実行
    sys.exit(app.exec())