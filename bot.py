import os, ast, shutil, random, time, sys
import colorama
from colorama import init,Fore,Back,Style
from module.clear import *

init(autoreset=True)

os.system('')

##配置检测##
if os.path.exists(".end.dev"):
    temp = 1
else:
    temp = open('.end.dev','w')
    temp.write("{"+f'\n\t\"NAME\":\t\"小熊猫\",\n\t\"USER\":\t\"大笨蛋\"'+"\n}")
    temp.close()
    raise TypeError("配置文件丢失，请重新启动bot")

##导入插件##
from plugins.ai import *
from plugins.ai.data_source import *
#导入说明 from plugins.[插件文件夹名称].插件文件夹中的每一份以.py结尾的文件(不用写后缀) import *
##导入插件##
##导入全局变量##
from module.unitl import *
##导入全局变量##
##变量申明##
error = "发生了未知错误"
num = 1
result = None
if os.path.exists('temp'):
    shutil.rmtree('temp')
os.mkdir('temp')
#生成缓存
if os.path.exists("temp/answer"):
    temp = 1
else:
    temp = open("temp/answer","x")
if os.path.exists("temp/num"):
    temp = 1
else:
    temp = open("temp/num","x")
if os.path.exists("temp/learn"):
    temp = 1
else:
    temp = open("temp/learn","x")
##生成配置
if os.path.exists(".end.dev"):
    try: 
      ask = str(input(f'当前bot名字是：{NICKNAME()}\n当前你的昵称是：{USER()}\n是否更改？[y/N]'))
    except EOFError:
      sys.exit(0)
    if ask == "y":
        NICKNAME = str(input("输入bot名称："))
        USER = str(input("输入你的昵称："))
        temp = open('.end.dev','w')
        temp.write("{"+f'\n\t\"NAME\":\t\"{NICKNAME}\",\n\t\"USER\":\t\"{USER}\"'+"\n}")
        temp.close()
while 1:
    try: 
        ask = str(input("\033[32m输入想对bot说的话：\033[0m"))
    except EOFError: 
        sys.exit(0)
    if num == (1):
        answer = ask
        temp = open('temp/answer','w')
        temp.write(str(answer))
        temp.close
    try:
        if ask in [ #询问昵称
            "你是谁",
            "你是",
            "你叫",
            "你叫什么"
            ]:
            result = f'我是{NICKNAME()}啊，{USER()}的脑袋是不是坏掉了？'
        else:
            result = hello(ask)
        if ask == "":
            result = "输入不得为空！"
    ####在下方添加插件####
    ####在上方添加插件####
        elif result == None:   #词库匹配回答
           result = AI(ask)
       #添加插件说明：
       #elif result == None:
       #result = [插件提供的函数名](ask)
       
        if result == None:
           result = no_result()
        #重复话语判定
        num = num + 1
        if num >= 3 and answer == ask:
            result = repeat()
        elif answer != ask:
            num = 1
        temp = open('temp/num','w')
        temp.write(str(num))
        temp.close()
        #学说话判定
        if ask == learn_speak():
           result = learn()
        print(f'\033[33m{result}\033[0m')
        temp = open('temp/learn','w')
        temp.write(result)
        temp.close
        result = None
    except:
        print(error)
