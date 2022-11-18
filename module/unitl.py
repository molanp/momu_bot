import ast, os

#全局变量
data = open('.end.dev',"r")
data = data.read()
data = ast.literal_eval(data)
def NICKNAME():
    NAME = data["NAME"]
    return NAME

def USER():
    USER = data["USER"]
    return USER

def num():
    num = open('temp/num.temp','r')
    num = num.read()
    return num

def learn_speak():
    learn_speak = open ('temp/learn.temp','r')
    learn_speak = learn_speak.read()
    return learn_speak
