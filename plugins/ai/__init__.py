#from plugins.ai.data_source import *
from .data_source import *
from collections import Counter
from module.unitl import *
import ast, random, difflib, requests, json, re,os
__momu_plugin_name__='AI'
__momu_plugin_help__=f'与{NICKNAME()}来一次简简单单的对话吧'
def start(ask):
 try:
   if ask == "":
            result = "输入不得为空！"
   elif ask in [ #打招呼
            "你好",
            "在",
            "您好",
            "你好啊",
            "在不在",
            "在吗",
            "您好啊"
            ]:
            result = hello(ask)
   elif ask in [ #询问昵称
            "你是谁",
            "你是",
            "你叫",
            "你叫什么"
            ]:
            result = f'我是{NICKNAME()}啊，{USER()}的脑袋是不是坏掉了？'
   else:
      with open('data/anime.json', encoding='utf-8') as anime:
          anime = anime.read()
          anime = ast.literal_eval(anime)
          
      data = open("data/anime_index.json",'r',encoding='utf-8')
      data = data.read()
      data = data.split(",")
      key = difflib.get_close_matches(ask, data)
      #print(key)
      if len(key) >= 1:
         data = str(anime[key[0]])
         data = eval(data)
         AI = str(random.sample(data, 1))
         AI = AI[2:-2]
         AI = AI.replace("我",f"{NICKNAME()}")
         AI = AI.replace("你",f"{USER()}")
         result = AI
      else:
       """
        获取青云客回复
        :param text: 问题
        :return: 青云可回复
       """
       res = requests.get(f"http://api.qingyunke.com/api.php?key=free&appid=0&msg={ask}")
       content = ""
       try:
        data = json.loads(res.text)
        if data["result"] == 0:
            content = data["content"]
            if "菲菲" in content:
                content = content.replace("菲菲", USER())
            if "艳儿" in content:
                content = content.replace("艳儿", USER())
            if "公众号" in content:
                content = None
            if "{br}" in content:
                content = content.replace("{br}", "\n")
            if "提示" in content:
                content = content[: content.find("提示")]
            if "淘宝" in content or "taobao.com" in content:
                content = None
            if "face:" in content:
                content = re.sub("{face:[0-999]}","",content)
                #print("RE is OK")
       except Exception as e:
          content = None
       finally:
          result = content
       if result == None:
          result = no_result()

      
 except:
   result = 'AI发生了一些错误'
 finally:
   return result