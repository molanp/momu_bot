from config.config import __plugin_PATH__
from module.loads import *

__momu_plugin_name__ = "help"
__momu_plugin_version__ = 1
__momu_plugin_help__="""
简简单单的帮助系统
""".strip()
def start(ask):
    if ask[:2] == "帮助" and ask[2:] != "":
        try:
            name = ask[2:]
            list,module,ai = momu.load_plugins(__plugin_PATH__)
            result = f"{ask[2:]}的帮助信息是：\n"+list[name]
        except:
            result = "没有此功能的帮助信息..."
        return result