import requests
import socket               # 导入 socket 模块
import datetime
import time

data = [{'tm': 0, 'hu': 0}, {'tm': 0, 'hu': 0}, {'tm': 0, 'hu': 0},
        {'tm': 0, 'hu': 0}, {'tm': 0, 'hu': 0}]
access_token = '37_1AOa4u-s6grgW2RQ4zdTXdyo-OYzVD8gVyRxD1jHw9rdrvRNK54ekeCMBmNMYjy0P9gfWikeFbACgkFSq0poHQLF8JEdfGQiMN4JSM95Gl6IzZFHWjJvGe7TGw44vSIDYLOpwlc64vlJmt_vARTdAGADUW'
def get_access_token():
    """
    获取小程序全局唯一后台接口调用凭据 access_token
    :return:
    """
    global access_token
    appid = "wxab5ec0b2d5f3463d"
    # Appkey（API密钥）
    secret = "d1f05a2e84888462c28dbb2344a18ecc"
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appid, secret)
    res = requests.get(url, timeout=3).json()
    access_token = res.get("access_token", None)
    print(access_token)


def base_send_mini_sub_msg(post_data):
    """
    发送订阅消息
    :param access_token:
    :param post_data:
    :return:
    """
    api = f"https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token={access_token}"
    # try:
    result = requests.post(api, json=post_data, timeout=3).json()  # 发送订阅消息
    # except:
    #     result = {}
    print(post_data)
    print(result)
    errcode = result.get("errcode")
    if errcode == 0:
        return True
    return False


def message_data(openid, template_id, post_data):
    """
    设置订阅消息内容
    """
    #  key 是模板的字段名称，value是字段对应的值
    # post_data = {"key1": {"value": any}, "key2": {"value": any}}

    data = {
        "touser": openid,  # 微信用户的open_id
        "template_id": template_id,  # 订阅消息模板id
        "data": post_data,  # 模板字段及其对应的字段，注意字段类型
        "page": "pages/home/home",  # 需要跳转的路径（前端提供）
    }
    base_send_mini_sub_msg(data)

if __name__ == "__main__":
    post_data = {
        "time1": {"value": str(time.strftime('%Y年%m月%d日 %H:%M', time.localtime(time.time())))},
        "thing2": {
            "value": '设备：{:d} 温度：{:.1f} 湿度：{:.1f}'.format(1, data[1]['tm'], data[1]['hu'])
        },
    }
    get_access_token()
    f = message_data('oizNr5EpkBFDj6soHrARvPxFjlx8','YSL6LXFSwBGFWctF-es4qNB8moOrbmYSvYYhVx5xT4U',post_data)
    print(str(f))

# print(str(datetime.datetime.now()))
