# -- coding:UTF-8 --
# Author:章永新
# 如果通过命令字符串找到多个，则使用这个策略提醒提问者,这个策略不需要注册到策略上下文中
from application.command_strategy import CommandStrategy


class CommandFoundTooMany(CommandStrategy):

    def __init__(self, command_list):
        self.command_list = command_list
        describe = '通过命令字符串找到多个，则使用这个策略提醒提问者'
        self.name = self.__class__.__name__
        super(CommandFoundTooMany, self).__init__(describe)

    def execute(self, message_json=None):
        message = '@{} 你是不是想问下面的问题啊？\n'.format(self.from_mobile)
        for command_str in self.command_list:
            message = message + ('> ' + self.gen_answerable_message(command_str) + '\n \n')
        return message

    def format_markdown(self, message):
        return {
            "title": '你是不是想问下面的问题啊？',
            "text": message
        }

    @staticmethod
    def is_markdown():
        return True
