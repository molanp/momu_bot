__momu_plugin_name__='示例插件'
__momu_plugin_version__=1
__momu_plugin_help__="""
草
一种植物
""".strip()
def start(ask):
    if "草" in ask:
        return "一种植物"