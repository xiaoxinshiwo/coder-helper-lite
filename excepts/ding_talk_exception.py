# -- coding:UTF-8 --
# Author:章永新


class DingTalkException(Exception):

    def __init__(self, message):
        self.message = message
        super(DingTalkException, self).__init__(self.message)
