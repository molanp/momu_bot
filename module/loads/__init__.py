import pkgutil,os
class momu:
    def load_plugins(__plugin_path__):
        with open("config/config.py","w") as conf:
            conf.write(f"__plugin_PATH__ = {__plugin_path__}")
        _plugins_before_listen = []  #插件列表
        #__plugin_list__ = set() 
        __plugin_list__ = {}
        ##导入插件##
        ai = None
        for finder,name,ispck in pkgutil.walk_packages(__plugin_path__):   #插件目录这个文件目录参数是一个列表 
            loader = finder.find_module(name)  #返回一个loader对象或者None。
            plugin = loader.load_module(name) #返回一个module对象或者raise an exception
            try:
                __plugin_list__[plugin.__momu_plugin_name__] = plugin.__momu_plugin_help__
                if plugin.__momu_plugin_name__ != 'AI':
                    _plugins_before_listen.append(plugin) #把模块加入列表中，方便使用
                else:
                    ai = plugin
            except:
                pass
        return __plugin_list__, _plugins_before_listen, ai