# 通用工具函数
#   功能：

#   读取 config.json，便于支持多个网站
#   解析 HTML，获取关键元素
#   处理异常、日志等
import json

def load_config(site):
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    return config.get(site, {})
