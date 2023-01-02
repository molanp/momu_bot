
# 插件标准
- 插件应包含
  - `__momu_plugin_name__`：插件名
  - `__momu_plugin_help__`：插件帮助
- 可选
  - `__momu_plugin_version__`：插件版本
  - `__momu_plugin_author__`：插件作者

> **\_\_momu_plugin_name__**

- **类型**：`str`
- **说明**：
插件名称，为插件列表中的展示内容，基本所有模块都必须有

> **\_\_momu_plugin_help__**

- **类型**：`str`
- **说明**：
插件帮助说明 示例：
```py
__momu_plugin_help__="""
草
一种植物
""".strip()
```

> **\_\_momu_plugin_version__**

- **类型**：`int`
- **说明**：
只是插件的版本号而已

> **\_\_momu_plugin_author__**

- **类型**：`str`
- **说明**：
插件的作者

> **示例插件**

```py
__momu_plugin_name__='示例插件'
__momu_plugin_version__=114514
__momu_plugin_help__="""
草
一种植物
""".strip()
def start(ask):
    if "草" in ask:
        return "一种植物"
```
**结果：**
```py
你:青青草原
- 一种植物
你:帮助草
- 草
  一种植物
```

# 全局变量调用

> **Bot名称**

```py
from module.unitl import *
__momu_plugin_name__='你是谁'
__momu_plugin_version__=114514
__momu_plugin_help__=f'你好我是{NICKNAME()}'
def start(ask):
    if "你是谁" in ask:
        return f'你好我是{NICKNAME()}，请多多指教~'
```

> **用户名称**

```py
from module.unitl import *
__momu_plugin_name__='我是谁'
__momu_plugin_version__=114514
__momu_plugin_help__=f'你是{USER()}'
def start(ask):
    if "我是谁" in ask:
        return f'你是{USER()}啊？'
```

> **插件文件夹**

```py
from config.config import __plugin_PATH__
__momu_plugin_name__='插件文件夹'
__momu_plugin_version__=114514
__momu_plugin_help__='为什么要有帮助'
def start(ask):
    if "插件文件夹" in ask:
        return f'目前加载的插件文件夹有：{__plugin_PATH__}'
```