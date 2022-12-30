from plugins.ai.data_source import no_result
from collections import Counter
from module.unitl import *
import ast, random
def AI(ask) -> str:
   with open('data/anime.json', encoding='utf-8') as anime:
       anime = anime.read()
       anime = ast.literal_eval(anime)
   anime_keys = list(anime.keys())
   ask = list(ask)
   for i in range(len(ask)):
       for j in range(len(anime_keys)):
           if anime_keys[j].find(ask[i]) == -1:
               continue
           temp = open("temp/index.json",'w')
           temp.write(f'{anime_keys[j]},')
           temp.close()
        
   data = open("temp/index.json",'r')
   data = data.read()
   data = f'{data[:-1]}'
   data1 = data
   data = data.split(",")
   number = Counter(data)
   result = number.most_common()
   most_key = '{}'.format(result[0][0])
   most_num = '{}'.format(result[0][1])
   data = str(anime[most_key])
   data = eval(data)
   AI = str(random.sample(data, 1))
   AI = AI[2:-2]
   AI = AI.replace("我",f"{NICKNAME()}")
   AI = AI.replace("你",f"{USER()}")
   dict1 = {}
   if most_num == 2:
      return no_result()
   else:
      return AI