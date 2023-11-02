import os
from PIL import Image

#===================================================
# 変数を定義
#===================================================

# 変換前の画像のディレクトリを指定する
dir_name = "img"

# 変換後のディレクトリを指定する
dir_new = "jpg"

# 変換対象の拡張子を指定する
exts = [".png", ".jpg", ".webp", ".bmp"]

# 圧縮率を指定
compression_rate = 90

#===================================================
# ここから処理開始
#===================================================

# 変換前のディレクトリから画像を取得する
files = os.listdir(dir_name)

# webpフォルダがなかったら作る
if os.path.isdir(dir_new):
    pass
else:
    os.mkdir(dir_new)


for file in files:
    # パスを作る
    img_path = os.path.join(dir_name, file)

    # ファイル名だけ取り出す
    img_filename, img_ext = os.path.splitext(os.path.basename(file))

    # .jpgと.pngと.bmpだけ処理対象にする
    if img_ext in exts:
        # 画像を開く
        img = Image.open(img_path)
        
        # 画像サイズを制限してリサイズ
        img.thumbnail((1280, 860))
        
        # webpとして/webpフォルダに保存
        img.save("./" + dir_new + "/" + img_filename + ".jpg", quality=compression_rate)
    else:
        pass
