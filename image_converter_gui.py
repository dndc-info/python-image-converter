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
        # インスタンスを作成
        #---------------------------------------------------
        self.input = self.Directory()
        self.output = self.Directory()

        #---------------------------------------------------
        # ボタンを作成
        #---------------------------------------------------
        # 必要なボタンを作成する
        button_input = QPushButton("画像があるフォルダ")
        button_output = QPushButton("画像を出すフォルダ")
        # ボタンのクリック時の挙動を追加する
        button_input.clicked.connect(self.input.echo_path)
        button_output.clicked.connect(self.output.echo_path)

        #---------------------------------------------------
        # レイアウトする
        #---------------------------------------------------
        layout.addWidget(button_input)
        layout.addWidget(button_output)

    #===================================================
    # 処理を使いまわしたいので
    # ディレクトリパスを取得する処理をClass化する
    #===================================================
    class Directory:
        def __init__(self):
            self.path = ""
            self.options = QFileDialog.Options()

        def echo_path(self):
            self.path = QFileDialog.getExistingDirectory(None, "ディレクトリ選択", options=self.options)
            return(self.path)


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