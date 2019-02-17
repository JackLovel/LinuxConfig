#!/bin/bash
#########################
# configure douban pipy #
########################

pypiConfigFile=/etc/pip.conf
fileContent="[global]\nindex-url = \
             http://pypi.douban.com/simple/\ntr \
             usted-host = pypi.douban.com"

# if pipy file is not exist, then create
if [ ! -f $pypiConfigFile ];then
  sudo touch $pypiConfigFile
fi

sudo echo -e $fileContent > $pypiConfigFile
