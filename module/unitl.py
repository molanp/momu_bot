import ast, os

#ćšć±ćé
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
    num = open('temp/num','r',encoding="utf-8")
    num = num.read()
    return num

def learn_speak():
    learn_speak = open('temp/learn','r',encoding="gbk")
    learn_speak = learn_speak.read()
    return learn_speak
    