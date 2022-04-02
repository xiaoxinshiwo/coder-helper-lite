# -- coding:UTF-8 --
# Author:章永新

from functools import wraps

from excepts.illegal_request_exception import IllegalRequestException
from application.ding_helper import app_info_config
import hmac
import hashlib
import base64


# 校验消息的签名，判断消息是否来自钉钉
def check_sign(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        header_dict = args[1]
        body_dict = args[2]
        timstamp = header_dict.get('timestamp')
        sign = header_dict.get('sign')
        crop_id = body_dict.get('chatbotCorpId')
        check_sign_equals(timstamp, crop_id, sign)
        return func(*args, **kwargs)

    return decorated


def check_sign_equals(timestamp, crop_id, sign_to_compare):
    if not timestamp or not crop_id or not sign_to_compare:
        throw_exception()
    app_secret = app_info_config.get_app_info(crop_id).get('appSecret')
    app_secret_enc = app_secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, app_secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode('utf-8')
    if sign_to_compare != sign:
        throw_exception()


def throw_exception():
    raise IllegalRequestException()


if __name__ == '__main__':
    check_sign_equals('1577262236757', 'dinge668cfccc47884c135c2f4657eb6378f', '123')
