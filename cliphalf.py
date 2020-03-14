from PIL import Image, ImageFilter
from pathlib import Path
from os import getuid
import sys

p = Path(sys.argv[1])
save_dir = Path(str(p) + '/cliphalf')
save_dir.mkdir(exist_ok=True)
num = 1
for picpath in list(p.glob("*.jpg")):
    picname_left = str(save_dir) + '/' + str(num) + 'l.jpg'
    picname_right = str(save_dir) + '/' + str(num) + 'r.jpg'
    im = Image.open(picpath)
    im.crop((0, 0, 1062, 1535)).save(picname_left, quality=95)
    im.crop((1205, 0, 2267, 1535)).save(picname_right, quality=95)
    num += 1
