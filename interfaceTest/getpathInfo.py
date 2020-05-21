import os

def get_Path():
    path = os.path.split(os.path.abspath(__file__))[0]
    return path


def get_path1():
    path_1 = os.path.split(os.path.abspath(__file__))[0]
    path_2 = os.path.split(os.path.abspath(__file__))[1]
    return path_1,path_2
if __name__ == '__main__':# 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())
    # print(get_path1())
