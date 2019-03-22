#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import shutil
import json


class SimpleBackup(object):
    """一个简单文件备份工具

    args:
         config_path: 这是一个存放备份文件路径的地方，
                      如果配置文件里不存在你要路径，那就添加或者删除文件路径到该文件中。
    """
    def __init__(self, target_directory_str):
        self.target_directory = target_directory_str
        self.config_path = os.path.join(os.getcwd(), 'file_path.json')

    def check(self):
        try:
            os.makedirs(self.target_directory)
        except FileExistsError:
            pass

    def copy(self):
        try:
            for file_name in self.file_paths():
                shutil.copy(file_name, self.target_directory)
        except FileNotFoundError:
            print("请写下文件的绝对路径，否则无法找到文件")

    def file_paths(self):
        config_paths = self.config_path
        with open(config_paths, 'r') as f:
            paths_list = json.load(f).get('path')
            return paths_list

    def setup(self):
        self.check()
        self.copy()


def main():
    target_directory = "/home/w/Desktop/demo/config_backup/"
    buckup = SimpleBackup(target_directory)
    buckup.setup()

main()