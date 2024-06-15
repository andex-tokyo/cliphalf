from PIL import Image, ImageFilter
from pathlib import Path
import sys

p = Path(sys.argv[1])
save_dir = Path(str(p) + '/cliphalf')
save_dir.mkdir(exist_ok=True)

# 画像ファイルの拡張子をリストに追加（大文字と小文字の両方）
image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.gif', '*.JPG', '*.JPEG', '*.PNG', '*.BMP', '*.GIF']

# 画像ファイルのみを処理
for ext in image_extensions:
    for picpath in p.glob(ext):
        picname = picpath.stem
        picname_left = str(save_dir) + '/' + picname + 'l.jpg'
        picname_right = str(save_dir) + '/' + picname + 'r.jpg'
        im = Image.open(picpath)
        width, height = im.size
        left_crop_width = int(1062 * (width / 2267))
        right_crop_start = int(1205 * (width / 2267))
        right_crop_end = int(2267 * (width / 2267))
        im.crop((0, 0, left_crop_width, height)).save(picname_left, quality=95)
        im.crop((right_crop_start, 0, right_crop_end, height)).save(picname_right, quality=95)
