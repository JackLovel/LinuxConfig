#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
作用：用于自动化安装一些软件
使用说明：1. 在 app_list.txt 中添加软件
          2. 然后在执行 python3 install_app.py
版本： v1.0
时间： 2019-2-28
"""

import os


def get_file_path():
    current_directory = os.getcwd()
    file_name = "./app_list.txt"
    file_path = os.path.join(current_directory, file_name)
    return file_path


def install_app(file_path):
    with open(file_path, "r+") as f:
        for app_name in f.readlines():
            os.system("sudo apt-get install -y {}".format(app_name))


def main():
    file_path = get_file_path()
    install_app(file_path)


main()
