# -*- coding:utf-8 -*-

import os

# def file_name_walk(file_dir):
#     for files in os.walk(file_dir):
#         print("files", files)  # 当前路径下所有非目录子文件
    # for root, dirs, files in os.walk(file_dir):
    #     print("root", root)  # 当前目录路径
    #     print("dirs", dirs)  # 当前路径下所有子目录
    #     print("files", files)  # 当前路径下所有非目录子文件

# file_name_walk("./")


# print os.getcwd()
# print os.path.abspath(os.path.dirname(__file__))


def file_name(file_dir): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.mp4':
                # L.append(file)
                L.append(os.path.join(root, file))
    print(L)

    for file in L:
        baseName = os.path.basename(file)
        os.system("ffmpeg -i %s -r 10  %s " % (file, baseName))
        # os.system("ffmpeg -i %s -r 10  %s " % (file, "../compressOK/"+baseName+".mp4"))
        print(file)

    # return L

#将上级目录中的mp4文件压缩，output到当前文件夹：
file_name("../compressDir")

