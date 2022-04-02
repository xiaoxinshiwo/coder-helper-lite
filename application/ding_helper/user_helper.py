# -- coding:UTF-8 --
# Author:章永新
# 用户信息查询工具类

import requests

from application.basic.local_cache import cacheable
from application.ding_helper.accesstoken_helper import AccessTokenHelper
from excepts.ding_talk_exception import DingTalkException


class UserHelper:

    def __init__(self, crop_id):
        self.crop_id = crop_id

    @cacheable(region='UserHelper', ttl=36000)
    def get_user_info(self, user_id):
        access_token = AccessTokenHelper(self.crop_id).get_access_token()
        url = 'https://oapi.dingtalk.com/topapi/v2/user/get?access_token={}'.format(access_token)
        param_json = {'userid': user_id}
        response_json = requests.post(url=url, json=param_json).json()
        if not response_json or response_json.get('errcode') != 0:
            raise DingTalkException(response_json)
        return response_json.get('result')

    def get_brief_user_info(self, user_id):
        result_data = self.get_user_info(user_id)
        mobile = result_data.get('mobile')
        job_number = result_data.get('job_number')
        name = result_data.get('name')
        brief_user_info = {
            'job_number': job_number,
            'mobile': mobile,
            'name': name
        }
        return brief_user_info

    def get_user_mobile(self, user_id):
        return self.get_brief_user_info(user_id).get('mobile')

    def get_user_job_number(self, user_id):
        return self.get_brief_user_info(user_id).get('job_number')


if __name__ == '__main__':
    token_helper = AccessTokenHelper('dinge668cfccc47884c135c2f4657eb6378f')
    access_token = token_helper.get_access_token()
    user_helper = UserHelper(access_token)
    print(user_helper.get_user_info('manager1933'))
    print(user_helper.get_user_mobile('manager1933'))
