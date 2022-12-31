from module.unitl import *

import random, os
#打招呼
def hello(ask):
    '''
    一些打招呼的内容
    '''
    if ask in [ #打招呼
            "你好",
            "在",
            "您好",
            "你好啊",
            "在不在",
            "在吗",
            "您好啊"
            ]:
                return (
                    random.choice(
                        [
                          "哦豁！？",
                          "叫我干甚？",
                          "我在！",
                          f"库库库，呼叫{NICKNAME()}干什么呢",
                          "呼呼，叫俺干啥"
                        ]
                    )
                )
            
def no_result() -> str: #没有回复时回答
    return (
        random.choice(
            [
                "你在说啥子？",
                f"纯洁的{NICKNAME()}没听懂",
                "下次再告诉你(下次一定)",
                "你觉得我听懂了吗？嗯？",
                "我！不！知！道！",
            ]
        )
    )

#重复话语
def repeat() -> str:
    '''
    有人连续发一样的话的回答
    '''
    #读取重复内容
    if os.path.exists("temp/answer"):
        answer = open('temp/answer','r')
        answer = answer.read()
    return (
        random.choice(
            [
                "为什么要发一样的话？",
                "爪巴！",
                "请不要再重复对我说一句话了，不然我就要生气了！",
                "别再发这句话了，我已经知道了...",
                "你是只会说这一句话吗？",
                f"{answer}，你发我也发！",
                f"{USER()}，{answer}",
                f"救命！有笨蛋一直给{NICKNAME()}发一样的话！",
                f"这句话你已经给我发了{num()}次了，再发就生气！",
                f"这句话你已经给我发{num()}次了！我生气啦！"
            ]
        )
    )
#学bot说话
def learn() -> str:
    '''
    学bot说话的回答(不会有人这么闲吧...)
    '''
    return (
        random.choice(
            [
                f"请不要学{NICKNAME()}说话",
                f"为什么要一直学{NICKNAME()}说话？",
                "你再学！你再学我就生气了！",
                f"呜呜，你是想欺负{NICKNAME()}嘛..",
                f"{USER()}不要再学我说话了！",
                "再学我说话，我就把你拉进黑名单（生气",
                f"你再学！{USER()}是个笨蛋！",
                f"你已经学我说话{num()}次了！别再学了！",
            ]
        )
    )
