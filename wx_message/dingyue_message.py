import requests
import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 8080                # 设置端口
s.bind((host, port))        # 绑定端口
 
s.listen(5)                 # 等待客户端连接
while True:
    c,addr = s.accept()     # 建立客户端连接
    print('连接地址：', addr)
    stu_id,open_id =eval(c.recv(1024))
    c.close()                # 关闭连接

def get_access_token():
    """
    获取小程序全局唯一后台接口调用凭据 access_token
    :return:
    """
    appid = "小程序AppID"
    secret = "Appkey（API密钥）"
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appid, secret)
    res = requests.get(url, timeout=3).json()
    access_token = res.get("access_token", None)
    return access_token


def message_data():
    """
    设置订阅消息内容
    :return:
    """
    #  key 是模板的字段名称，value是字段对应的值
    data = {"key1": {"value": any}, "key2": {"value": any}}

    post_data = {
        "touser": "open_id",  # 微信用户的open_id
        "template_id": "mini_template_id",  # 订阅消息模板id
        "data": data,  # 模板字段及其对应的字段，注意字段类型
        "page": "page",  # 需要跳转的路径（前端提供）
    }
    access_token = get_access_token()
    base_send_mini_sub_msg(access_token, post_data)


def base_send_mini_sub_msg(access_token, post_data):
    """
    发送订阅消息
    :param access_token:
    :param post_data:
    :return:
    """
    api = f"https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token={access_token}"
    try:
        result = requests.post(api, json=post_data, timeout=3).json()  # 发送订阅消息
    except:
        result = {}
    print(post_data)
    print(result)
    errcode = result.get("errcode")
    if errcode == 0:
        return True
    return False

