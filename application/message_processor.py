# -- coding:UTF-8 --
# Author:章永新
# 猿小蜜的消息处理服务
from application import strategy_context
from application.ding_helper.message_checker import check_sign


class MessageProcessor:

    # 新增加的命令需要在这里进行注册，json_headers 用于签名校验
    @check_sign
    def __init__(self, json_headers, json_data):
        self.json_data = json_data
        self.json_headers = json_headers

    def process(self):
        return strategy_context.execute(self.json_data)
