# -- coding:UTF-8 --
# Author:章永新
# 父类定义执行的方法
import time
from datetime import datetime
import urllib.parse
from application.ding_helper.user_helper import UserHelper


class CommandStrategy:

    def __init__(self, describe):
        # 功能描述，例如：获取后端周报发布之日者
        self.describe = describe
        self.at_mobiles = []
        self.from_mobile = None

    def handle_message(self, message_json):
        message = self.execute(message_json)
        # 将返回详细放到context里面
        if self.is_markdown():
            message_json['msgtype'] = 'markdown'
            message_json['markdown'] = self.format_markdown(message)
        elif self.is_action_card():
            message_json['msgtype'] = 'actionCard'
            message_json['actionCard'] = self.format_action_card(message)
        else:
            message_json['text']['content'] = str(message)
        message_json['at'] = {'atMobiles': self.at_mobiles, "isAtAll": 'false'}
        # 执行完毕需要清理
        self.at_mobiles = []
        self.after_execution()
        return message_json

    def execute(self, message_json):
        return '暂未实现'

    def after_execution(self):
        pass

    @staticmethod
    def get_current_date_str():
        return datetime.strftime(datetime.now(), '%Y-%m-%d')

    def format_markdown(self, message):
        message = '@{}\n{}'.format(self.from_mobile, message)
        return {
            "title": self.describe,
            "text": message
        }

    def set_from_mobile(self, from_mobile):
        self.from_mobile = from_mobile
        self.at_mobiles.append(from_mobile)

    @staticmethod
    def is_markdown():
        return False

    @staticmethod
    def is_action_card():
        return False

    def format_action_card(self, message):

        return {
            "title": message,
            "text": message,
            "btnOrientation": "0",
            "btns": self.get_btn_list()
        }

    @staticmethod
    def format_btn(title):
        return {
            "title": title,
            "actionURL": 'http://zhangyongxin.vaiwan.com/message?text={}'.format(title)
        }

    def get_btn_list(self):
        pass

    @staticmethod
    def date_diffs(date_start, date_end):
        date_end_time = time.strptime(date_end, '%Y-%m-%d')
        date_start_time = time.strptime(date_start, '%Y-%m-%d')

        # 比较日期
        date1 = datetime(date_start_time[0], date_start_time[1], date_start_time[2])
        date2 = datetime(date_end_time[0], date_end_time[1], date_end_time[2])
        return (date2 - date1).days

    @staticmethod
    def get_job_number(message_json):
        crop_id = message_json['chatbotCorpId']
        sender_staff_id = message_json['senderStaffId']
        user_helper = UserHelper(crop_id)
        return user_helper.get_user_job_number(sender_staff_id)

    @staticmethod
    def get_at_users(message_json):
        atUsers = message_json['atUsers']
        crop_id = message_json['chatbotCorpId']
        at_user_infos = []
        for user in atUsers:
            if user.get('staffId'):
                staff_id = user.get('staffId')
                user_helper = UserHelper(crop_id)
                at_user_infos.append(user_helper.get_brief_user_info(staff_id))
        return at_user_infos

    @staticmethod
    def format_jira_markdown_link(issue_key):
        return '[{}](https://issue.f6yc.com/browse/{})'.format(issue_key, issue_key)

    @staticmethod
    def gen_answerable_message(message):
        return '[{}](dtmd://dingtalkclient/sendMessage?content={})'.format(message, urllib.parse.quote(message))


if __name__ == '__main__':
    print(CommandStrategy('').gen_answerable_message('打tag'))
