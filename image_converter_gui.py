# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

#===================================================
# GUI作成
#===================================================

class DirectoryPathApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # ウィンドウタイトルを設定
        self.setWindowTitle("ディレクトリパス取得のサンプル")
        # ウィンドウの位置とサイズを設定
        self.setGeometry(100, 100, 400, 200)
        # ボタンを作成
        button = QPushButton("ディレクトリを選択")
        button.clicked.connect(self.selectDirectory)

        self.setCentralWidget(button)

    def selectDirectory(self):
        options = QFileDialog.Options()
        directory_path = QFileDialog.getExistingDirectory(self, "ディレクトリを選択", options=options)

        if directory_path:
            print("選択したディレクトリパス:", directory_path)

#===================================================
# ここからウィンドウ作成
#===================================================
if __name__ == "__main__":
    # Qt Applicationを作成する
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    # formを作ってから表示する
    main_window = DirectoryPathApp()
    main_window.show()

    # Qtループを実行
    sys.exit(app.exec())