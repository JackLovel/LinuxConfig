########################
# 额外添加的部分
########################

# update system
alias up="sudo apt-get update && sudo apt-get upgrade"

# configure flask
project_directory="/home/w/Documents/CodePro/flask_ex"
alias fd="cd $project_directory"
alias fv="cd $project_directory && . venv/bin/activate"
alias fk="deactivate"
alias fs="fv && . ./init.sh"

# configure mysql 
user_name="flasky"
host_ip="localhost"

alias mL="mysql -h$host_ip -u$user_name -p"

# configure jdk
export JAVA_HOME="~/App/jdk1.8.0_202/"
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH

# BASH config 
alias SB="source ~/.bashrc"
alias OB="vim ~/.bashrc"
