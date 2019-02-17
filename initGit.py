#!/usr/bin/env python3
#-*- conding: utf-8 -*-
"""
用于初始化git环境
"""

import os


def environment_set():
    username = input('enter git name:')
    email = input('enter git mail:')

    os.system('git config --global user.name {}'.format(username.strip()))
    os.system('git config --global user.email {}'.format(email.strip()))


def check_sucess():
    os.system('ssh -T git@github.com')


def key_produce():
    os.system('ssh-keygen -t rsa')


def open_key_file():
    editor = 'gedit'
    home_directory = '/home/w/'
    key_produce_file = os.path.join(home_directory, '.ssh/id_rsa.pub')
    os.system('sudo {0} {1}'.format(editor, key_produce_file))


command = {
    'e': environment_set,
    'k': key_produce,
    'o': open_key_file,
    's': check_sucess,}

def main():
    while True:
        prompt = """\n1.enter e k o s config git environment\n2.enter q to quit\n> """

        enter = input(prompt)
        if enter == 'q':
            break

        function_name = command.get(enter)
        if function_name == None:
            continue
        function_name()

main()
