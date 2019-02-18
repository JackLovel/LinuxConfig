#!/usr/bin/env python3
"""
用于自动化安装一些软件
"""

import os


app_list = [ 'firefox', 'git', 'atom', 'python3-pip', 'python-pip', 'emacs',  'mysql-server', 'mysql-workbench', 'python3-venv', ]


for i in app_list:
	os.system('sudo apt-get -y install {}'.format(i))
