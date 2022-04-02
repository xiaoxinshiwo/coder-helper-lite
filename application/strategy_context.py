# -- coding:UTF-8 --
# Author:章永新
# 策略上下文，用于注册
from application import *

# 命令名和命令的dict

command_and_name_dict = {}
# 命令描述的列表
commands_desc_list = []
# 命令描述和命令名的dict
command_desc_name_mapping = {}


# 注册入口
def register(commandStrategy):
    command_and_name_dict[commandStrategy.name] = commandStrategy
    commands_desc_list.append(commandStrategy.describe)
    command_desc_name_mapping[commandStrategy.describe] = commandStrategy.name
    logger.info('已注册命令:{}'.format(commandStrategy.describe))


def get_mobile(crop_id, staff_id):
    user_helper = UserHelper(crop_id)
    return user_helper.get_user_mobile(staff_id)


# 执行入口
def execute(message_json):
    # 返回消息@问题发起者
    crop_id = message_json['chatbotCorpId']
    sender_staff_id = message_json['senderStaffId']
    staff_mobile = get_mobile(crop_id, sender_staff_id)
    # 开始执行
    command_in = message_json.get('text').get("content").strip()
    command_strategy = find_suitable_command(command_in)
    command_strategy.set_from_mobile(staff_mobile)
    return command_strategy.handle_message(message_json)


# 根据指令找到合适的命令实现策略去执行
def find_suitable_command(command_in):
    commands = commands_desc_list
    default_command = CommandSayAnything()
    if not command_in or len(command_in) == 0:
        return default_command
    command_in = command_in.upper()
    command_found_list = []
    for command in commands:
        multi_command_list = command.split('-')
        for sub_command in multi_command_list:
            if command_in.upper() in sub_command.upper() or sub_command.upper() in command_in:
                command_found_list.append(command)
                break
    if not command_found_list:
        return default_command
    elif len(command_found_list) > 1:
        return CommandFoundTooMany(command_found_list)
    else:
        command_desc = command_found_list[0]
        command_name = command_desc_name_mapping.get(command_desc)
        return command_and_name_dict.get(command_name)


# 新添加命令需要在此手动注册
def register_all_commands():
    register(CommandEncourageSomeone())
    register(CommandPoisonSoap())


# 初始化加载
def init_load_all_commands():
    register_all_commands()


init_load_all_commands()
