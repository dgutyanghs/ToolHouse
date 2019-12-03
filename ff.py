
# -*- coding:utf-8 -*-

import os
import sys 

# 在终端命令行输入
# python ff.py input.mp4
# 说明："input.mp4" 是你要压缩的文件， 压缩完成后的文件为：“input_H264.mp4"


# os.system("ffmpeg -i %s -c:v libx265 -crf 22  -tag:v hvc1 %s " % (fileName, base + "_H265.mp4"))
# 说明：-crf 28: 28为压缩系数（可取范围0 ～ 51）， 0 为无损， 51：文件最小，但图像质量最低。

def compress():
    if (len(sys.argv) > 1):
        fileName = sys.argv[1]
        baseName = os.path.basename(fileName)
        base = os.path.splitext(baseName)[0]
        print("fileName:", fileName)
        print("baseName:", baseName)
        print("base:", base)
        # ffmpeg -i input.avi -c:v libx265 -crf 28  -tag:v hvc1 output.mp4
        os.system("ffmpeg -i %s -c:v libx265 -crf 22  -tag:v hvc1 %s " % (fileName, base + "_H265.mp4"))
    else:
        print("error format")

compress()




