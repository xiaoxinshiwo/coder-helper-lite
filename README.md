# coder-helper-lite
# 项目介绍
一个python实现的钉钉交互机器人

# 配置钉钉机器人
1. 登录钉钉开发者后台，获取cropId：
<img width="441" alt="image" src="https://user-images.githubusercontent.com/24218496/161930583-9294fb5c-ba90-46c0-b0d6-3fa506e7e479.png">
2. 创建钉钉机器人应用
<img width="590" alt="image" src="https://user-images.githubusercontent.com/24218496/161930778-88f5c362-54d8-4962-bf02-e2783bbb02cb.png">
<img width="553" alt="image" src="https://user-images.githubusercontent.com/24218496/161930889-b5042fcc-04d4-42dc-9b2e-84a84bf21377.png">
<img width="1299" alt="image" src="https://user-images.githubusercontent.com/24218496/161931036-f8fd7f65-1c96-4a1b-8385-a43749cdda9f.png">

# 环境
python >=3.8

# 启动项目

1. colne project到本地
2. 修改项目application/ding_helper/app_info_config.py配置，将上面采集到的`cropId、appKey、appSecret`三个参数复制修改
3. 运行命令`pip install -r requirements.txt` 安装依赖
4. 运行命令 `gunicorn -w 4 app:app &`运行项目， ginicorn安装参考：https://gunicorn.org/
5. 或者不用其他服务器发布，直接运行` python app.py`一样可以启动（可选）
6. 配置域名或者通过内网穿透工具来提供域名

# 发布钉钉机器人
**填写服务出口ip和消息接收地址**
<img width="1031" alt="image" src="https://user-images.githubusercontent.com/24218496/161931855-5692cf8a-b3e3-4e3c-9ee4-18e33e9b3c2c.png">
**消息接收地址**为域名加接口名的形式，如果没有自己的域名可以使用内网穿透工具来实现，参考：https://open.dingtalk.com/document/resourcedownload/http-intranet-penetration
# 在钉钉中启用机器人
![image](https://user-images.githubusercontent.com/24218496/161932589-62099ef4-9dda-444d-b8f6-7dd9fa9c28cb.png)

# 使用机器人
群里面添加好机器人就可以使用了，或者对机器人单聊也可以哦
![image](https://user-images.githubusercontent.com/24218496/161933159-3b892cb8-c491-42c1-9f18-c75ec3eeec01.png)

