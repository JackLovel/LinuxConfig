#!/usr/bin/python3
# -*- coding: utf-8 -*-


from datetime import datetime
import os 


def copy(source, target):
    os.system("cp {0} {1}".format(source, target))


def main():
    #now = datetime.now()
    #save_format = "{0}_{1}_{2}".format(
    #    now.year, now.month, now.day)

    target_directory = "~/Desktop/demo/config_backup/"

    try:
        os.makedirs("target_directory")
    except FileExistsError:
        pass
    
    source_file = [
        "~/.bashrc", "~/.zshrc"
    ]
    
    for i in source_file:
        copy(i, target_directory)

    print("Done!")


main()
