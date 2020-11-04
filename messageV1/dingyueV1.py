import json
import datetime
import time
import logging
import os.path

logger = ''
access_token = ''

# 获取温度湿度
def getTmpHu(n):
    response = requests.get(
        url='http://ntscdtu.xindun.hn.cn:5566/value/IntelSw/rlvalue?token=27CAE903&ide=503316%d' % n).json()
    response = response[0]
    return {'tm': eval('%.2f' % response['outertm'][0]), 'hu': eval('%.2f' % response['outerhu'][0])}

# 从传感器获取数据
def flush_data():
    json_data = {}
    with open('c:/message/data.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)

    for i in range(49, 54):
        json_data['data'][i - 49] = getTmpHu(i)

    with open('c:/message/data.json', "w") as jsonFile:
        json.dump(json_data, jsonFile, ensure_ascii=False)


def judge_tm(i):
    json_data = {}
    with open('c:/message/data.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    data = json_data['data']
    if data[i]['tm'] > 35:
        return False
    else:
        return True


def judge_hu(i):
    json_data = {}
    with open('c:/message/data.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    data = json_data['data']
    if i == 2 and data[i]['hu'] > 90:
        return False
    if i == 3 and data[i]['hu'] < 60:
        return False
    return True


# 判断是否应该发消息，存储事件
def judge_all():
    flush_data()
    json_data = {}
    with open('c:/message/data.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    record_data = {}
    with open('c:/message/record.json', 'r', encoding='utf8')as fp:
        record_data = json.load(fp)

    json_data['isNormal_now'][0] = judge_tm(0)
    json_data['isNormal_now'][1] = judge_tm(1)
    json_data['isNormal_now'][2] = judge_tm(2) and judge_hu(2)
    json_data['isNormal_now'][3] = judge_hu(3)
    json_data['isNormal_now'][4] = judge_tm(4)

    data = json_data['data']
    isNormal_now = json_data['isNormal_now']
    isNormal_past = json_data['isNormal_past']
    isFirst = getfirst()
    state = getgroup()
    noerror = geterror()

    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # 日志
    logger.warning(data)
    # 第一次同时报警
    if isFirst:
        if True not in isNormal_now:
            post_data = {
                "time1": {"value": str(time.strftime('%Y年%m月%d日 %H:%M', time.localtime(time.time())))},
                "thing2": {"value": '全部报警'},
            }
            for i in range(5):
                record_data[i] = {'time': str(t), 'state': 1}
            send_message_all('YSL6LXFSwBGFWctF-es4qNB8moOrbmYSvYYhVx5xT4U',
                             post_data, state, -1)
            changefisrt(False)
    else:
        for i in range(5):
            if isNormal_now[i] != isNormal_past[i]:
                if isNormal_now[i]:
                    record_data[i] = {'time': str(t), 'state': 2}
                else:
                    record_data[i] = {'time': str(t), 'state': 1}
        if noerror:
            if False not in isNormal_now:
                post_data = {
                    "time1": {"value": str(time.strftime('%Y年%m月%d日 %H:%M', time.localtime(time.time())))},
                    "thing2": {
                        "value": '全部报警解除'
                    },
                }
                send_message_all('RlzIWw04GwP9p2pEsTg3p959A3waEVm4RAvn2CJP0cA', post_data, state, -1)
                seterror(False)
        else:
            for i in range(5):
                # 报警解除
                if (not isNormal_past[i]) and isNormal_now[i]:
                    post_data = {
                        "time1": {"value": str(time.strftime('%Y年%m月%d日 %H:%M', time.localtime(time.time())))},
                        "thing2": {
                            "value": '设备：{:d} 温度：{:.1f} 湿度：{:.1f}'.format(i + 1, data[i]['tm'], data[i]['hu'])
                        },
                    }
                    send_message_all('RlzIWw04GwP9p2pEsTg3p959A3waEVm4RAvn2CJP0cA', post_data, state, i)
                # 开始报警
                if isNormal_past[i] and (not isNormal_now[i]):
                    post_data = {
                        "time1": {"value": str(time.strftime('%Y年%m月%d日 %H:%M', time.localtime(time.time())))},
                        "thing2": {
                            "value": '设备：{:d} 温度：{:.1f} 湿度：{:.1f}'.format(i + 1, data[i]['tm'], data[i]['hu'])
                        },
                    }
                    send_message_all('YSL6LXFSwBGFWctF-es4qNB8moOrbmYSvYYhVx5xT4U',
                                     post_data, state, i)

    json_data['isNormal_past'] = isNormal_now
    with open('c:/message/data.json', "w") as jsonFile:
        json.dump(json_data, jsonFile, ensure_ascii=False)
    with open('c:/message/record.json', "w") as jsonFile:
        json.dump(record_data, jsonFile, ensure_ascii=False)
    return


def getgroup():
    with open('c:/message/group.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    state = json_data['state']
    return state


def changestate(state):
    with open('c:/message/group.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    json_data['state'] = state
    with open('c:/message/group.json', "w") as jsonFile:
        json.dump(json_data, jsonFile, ensure_ascii=False)
    return


def getfirst():
    with open('c:/message/first.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    isfirst = json_data['isFirst']
    return isfirst


def changefisrt(isfirst):
    json_data = {"isFirst": isfirst}
    with open('c:/message/first.json', "w") as jsonFile:
        json.dump(json_data, jsonFile, ensure_ascii=False)
    return


def geterror():
    with open('c:/message/noerror.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    noerror = json_data['noerror']
    return noerror


def seterror(noerror):
    json_data = {"noerror": noerror}
    with open('c:/message/noerror.json', "w") as jsonFile:
        json.dump(json_data, jsonFile, ensure_ascii=False)
    return


def get_access_token():
    """
    获取小程序全局唯一后台接口调用凭据 access_token
    :return:
    """
    global access_token
    # print('getToken')
    appid = "wxab5ec0b2d5f3463d"
    # Appkey（API密钥）
    secret = "d1f05a2e84888462c28dbb2344a18ecc"
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=" \
          "client_credential&appid=%s&secret=%s" % (appid, secret)
    res = requests.get(url, timeout=3).json()
    access_token = res.get("access_token", None)
    print('access_token', access_token)


def base_send_mini_sub_msg(post_data):
    """
    发送订阅消息
    :param post_data:
    :return:
    """
    api = f"https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token={access_token}"
    try:
        result = requests.post(api, json=post_data, timeout=3).json()  # 发送订阅消息
    except:
        result = {}
    errcode = result.get("errcode")
    logger.warning(post_data['touser'])
    logger.warning(result)
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


def send_message_all(template_id, post_data, group, event):
     with open('main_dingyue_message_user.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)

    user_list = []
    for data in json_data:
        if data['group'] == 6:
            user_list.append(data)

    for user in user_list:
        message_data(user['oid'], template_id, post_data)

def init():
    global logger
    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)  # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_path = 'c:/message/Logs/'
    log_name = log_path + rq + '.log'
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='a')
    fh.setLevel(logging.WARNING)  # 输出到file的log等级的开关
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)

if __name__ == "__main__":
    init()
    get_access_token()
    while True:
        flush_data()
        time.sleep(2)