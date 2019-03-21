#!/bin/bash

source_directory="/home/w/Documents/CodePro/BookNote"
target_directory="/home/w/Documents/CodePro/backupTest"
source_file="/home/w/Documents/CodePro/LinuxConfig/initGit.py"
current_data=${date -Y}.${date -H}

if [ -f "$source_file" ];
then
    cp $source_file 
else
    echo " not found"
fi
case 