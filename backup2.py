#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import shutil


class SimpleBackup(object):
    """一个简单文件备份工具"""
    def __init__(self, source_files_list, target_directory_str):
        self.source_files = source_files_list
        self.target_directory = target_directory_str

    def check(self):
        try:
            os.makedirs(self.target_directory)
        except FileExistsError:
            print("目标目录或者文件不存在")

    def copy(self):
        try:
            for file_name in self.source_files:
                shutil.copy(file_name, self.target_directory)
        except FileNotFoundError:
            print("请写下文件的绝对路径，否则无法找到文件")

    def setup(self):
        self.check()
        self.copy()


def main():
    source_file = [
        "/home/w/.bashrc",
        "/home/w/.zshrc"
    ]
    target_directory = "/home/w/Desktop/demo/config_backup/"
    buckup = SimpleBackup(source_file, target_directory)
    buckup.setup()

main()