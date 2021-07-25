import shutil
import os
from os import path
import zipfile

# 复制一份关键图像识别图片至正确路径
shutil.copyfile('tiyan_clickbox.png', 'dist/main/tiyan_clickbox.png')

# 压缩文件
paths = [r'main.py', r'README.md', r'requirements.txt',
         r'tiyan_clickbox.png', r'使用视频.mp4', r'Windows运行点我.bat', ]

compress_my_work = zipfile.ZipFile('输出.zip', 'w')
for path in paths:
    compress_my_work.write(path,
                           compress_type=zipfile.ZIP_DEFLATED)


compress_my_work.close()

# 追加压缩文件夹dist


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))


zipf = zipfile.ZipFile('输出.zip', 'a', zipfile.ZIP_DEFLATED)
zipdir('dist', zipf)
zipf.close()
