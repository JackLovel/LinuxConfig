###################
# 简单的 vim 配置
###################

set number          "显示行号                                                                      
set cursorline      "突出显示当前行
set tabstop=4       "设定tab长度为4
set autoindent      "vim使用自动对起，也就是把当前行的对起格式应用到下一行
set showmatch       "置匹配模式，类似当输入一个左括号时会匹配相应的那个右括号
set ruler           "在编辑过程中，在右下角显示光标位置的状态行
set nocompatible
set writebackup     "正常关闭前 建立备份文件
set nobackup        "正常关闭后 自动删除建立的备份文件
set history=1000    "记录历史的行数
set shortmess=atl   "消除 请按 ENTER 或其它命令继续 在进入vim编辑器前总会出现这行字
set shiftwidth=4
set expandtab
