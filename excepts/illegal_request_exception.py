# -- coding:UTF-8 --
# Author:章永新


class IllegalRequestException(Exception):

    def __init__(self):
        self.message = "非法的请求，签名不合法"
        super(IllegalRequestException, self).__init__(self.message)

