# -- coding:UTF-8 --
# Author:章永新


# 如果新增公司，需要将添加的群机器人的信息维护到这里
# dict 的key是cropId
def get_config():
    return {
        "ding6a097b349ef5b661acaaa37764f94726": {
            "desc": "小新的公司-猿小蜜",
            "appKey": "dingdugn9oiynlbywzo2",
            "appSecret": "G9SRWnzPOc6MVrG6rjdKI6BWAcHJqhNAGoPXodAlIv6Mb5q-LtDZ6KeE0D5QGux2"
        }
    }


def get_app_info(crop_id):
    return get_config().get(crop_id)
