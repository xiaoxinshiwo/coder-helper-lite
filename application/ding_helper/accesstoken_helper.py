# -- coding:UTF-8 --
# Author:章永新
# access_token获取的工具类
import requests

from application.basic.local_cache import cacheable
from application.ding_helper import app_info_config


class AccessTokenHelper:

    # crop_id：会话中的chatbotCorpId或者senderCorpId
    def __init__(self, crop_id):
        app_info = app_info_config.get_app_info(crop_id)
        self.app_key = app_info.get('appKey')
        self.app_secret = app_info.get('appSecret')

    @cacheable(region='AccessTokenHelper', ttl=5400)
    def get_access_token(self):
        url = "https://api.dingtalk.com/v1.0/oauth2/accessToken"
        param = {
            "appKey": self.app_key,
            "appSecret": self.app_secret
        }

        response = requests.post(url=url, json=param).json()
        return response.get('accessToken')


if __name__ == '__main__':
    token_helper = AccessTokenHelper("dinge668cfccc47884c135c2f4657eb6378f")
    token = token_helper.get_access_token()
    print(token)
