# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget

#===================================================
# GUI作成
#===================================================
class image_converter(QMainWindow):
    def __init__(self):
        super().__init__()

        #---------------------------------------------------
        # ウィンドウの設定
        #---------------------------------------------------
        # ウィンドウタイトルを設定
        self.setWindowTitle("ディレクトリパス取得のサンプル")
        # ウィンドウの位置とサイズを設定
        self.setGeometry(100, 100, 400, 200)

        #---------------------------------------------------
        # ウィジェットの作成
        #---------------------------------------------------
        widget = QWidget(self)
        self.setCentralWidget(widget)
        # ウィジェットをレイアウトする
        #   これ忘れると、ボタンが表示されない。ハマった…
        layout = QVBoxLayout(widget)

        #---------------------------------------------------
        # ボタンを作成
        #---------------------------------------------------
        # 必要なボタンを作成する
        button_input = QPushButton("ディレクトリを選択")
        button_output = QPushButton("Button B")
        # ボタンのクリック時の挙動を追加する
        button_input.clicked.connect(self.selectDirectory)
        button_output.clicked.connect(self.selectDirectory)

        #---------------------------------------------------
        # レイアウトする
        #---------------------------------------------------
        layout.addWidget(button_input)
        layout.addWidget(button_output)


    def selectDirectory(self):
        options = QFileDialog.Options()
        directory_path = QFileDialog.getExistingDirectory(self, "ディレクトリを選択", options=options)
        print(directory_path)


#===================================================
# ここからウィンドウ作成
#===================================================
def main():
    # Qt Applicationを作成する
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    # formを作ってから表示する
    window = image_converter()
    window.show()

    # Qtループを実行
    sys.exit(app.exec())


if __name__ == "__main__":
    main()