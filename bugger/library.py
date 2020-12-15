# -*- coding:utf-8 -*-
# coding:utf-8
import datetime
import json
import time
import requests
import urllib
import re
import sys

area_name_dic = {
    'hnu_lib1': '总馆',
    'hnu_lib2': '特藏分馆',
    'hnu_lib3': '财院分馆',
    'hnu_lib4': '德智园分馆'
}

address_name_dic = {
    'hnu_lib1_1F1': '总馆一楼外文文献借阅室',
    'hnu_lib1_2F1': '总馆二楼读者服务中心',
    'hnu_lib1_3F1': '总馆三楼中文社科文献借阅室',
    'hnu_lib1_3F2': '总馆三楼自习室',
    'hnu_lib1_4F1': '总馆四楼中文自科文献借阅室(一)',
    'hnu_lib1_5F1': '总馆五楼中文自科文献借阅室(二)',
    'hnu_lib1_6F1': '总馆六楼中文自科文献借阅室(三)',
    'hnu_lib1_7F1': '总馆七楼中文自科文献借阅室(四)',
    'hnu_lib1_8F1': '总馆八楼自习室',
    'hnu_lib4_3F1': '德智园分馆三楼自修室',
    'hnu_lib4_4F1': '德智园分馆四楼借阅室'
}

study_time_dic = [(12, 18), (16, 22.5), (12, 22.5),
                  (12, 22.5), (18, 22.5), (14, 22.5), (14, 22.5)]

cookie_unit_name ='%e6%b9%96%e5%8d%97%e5%a4%a7%e5%ad%a6%e5%9b%be%e4%b9%a6%e9%a6%86'
dt_cookie_user_name_remember = '3FE3638936E97946C744EF0BCA3F5B835ADB779878D74FFD'

def init():
    time_next = datetime.datetime.now()                 # 获取当天
    # time_next = time_next + datetime.timedelta(days=1)  # 获取后一天
    date = (time_next).strftime("%Y-%m-%d")

    if time_next.hour < 8:
        json_data = {"code": 0,"time":''}
        with open('E:/personal/study/Python/bugger/code.json', "w") as jsonFile:
            json.dump(json_data, jsonFile, ensure_ascii=False)
    with open('E:/personal/study/Python/bugger/code.json', 'r', encoding='utf8')as fp:
        if json.load(fp)['code'] == 1:
            sys.exit(0)
    
    (start, end) = study_time_dic[time_next.weekday()]
    study_time = '{:d},{:d}'.format(int(start*60), int(end*60))
    
    SessionId = ''
    SessionId=login()
    return (date, study_time, SessionId)

# 生成Refer
def getRefer(address, date):
    address_name = address_name_dic[address]
    address_name = urllib.parse.quote(address_name)
    area_name = area_name_dic[address[:8]]
    area_name = urllib.parse.quote(area_name)
    refer = 'http://chaxin.hnu.edu.cn/mobile/html/seat/seat_tujian.html?v=20201207&seataddress={}&seatdate={}&address_name={}&area_code{}&area_name={}'.format(
        address, date, address_name, address[:8], area_name)

# 登录
def login():
    data = {
        'rdid': 'w5rHp8b2NIU36N4CaSdMwg==',
        'libcode': 'U4KxUxjQesfSqG0uHSCIiQ==',
        'name': '舒俊锋',
        'openid': "omIDgjoFhNWG6ZBycX3-1t0LiUmw"
    }
    headers = {
        'Host': 'chaxin.hnu.edu.cn',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MIX 2S Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2693 MMWEBSDK/201001 Mobile Safari/537.36 MMWEBID/1531 MicroMessenger/7.0.20.1781(0x2700143F) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/tpg,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'X-Requested-With': 'com.tencent.mm',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    data = json.dumps(data)
    url = 'http://chaxin.hnu.edu.cn/api/hnu/CheckReader.aspx'
    resp = requests.get(url, data=data, headers=headers)
    return requests.utils.dict_from_cookiejar(resp.cookies)['ASP.NET_SessionId']

# 座位列表
def getseat(SessionId, address, date, refer):
    data = {
        'data_type': 'GetTuiJianSeat',
        'areacode': address[:8],
        'addresscode': address,
        'seatdate': date
    }

    headers = {
        'Host': 'chaxin.hnu.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '87',
        'Accept': 'application/json',
        'Origin': 'http://chaxin.hnu.edu.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MIX 2S Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2693 MMWEBSDK/201001 Mobile Safari/537.36 MMWEBID/1531 MicroMessenger/7.0.20.1781(0x2700143F) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': refer,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4'
    }
    cookie = {
        'cookie_unit_name': cookie_unit_name,
        'ASP.NET_SessionId': SessionId,
        'dt_cookie_user_name_remember': dt_cookie_user_name_remember
    }

    data = urllib.parse.urlencode(data)
    url = 'http://chaxin.hnu.edu.cn/mobile/ajax/seat/SeatInfoHandler.ashx'
    resp = requests.post(url, data=data, headers=headers, cookies=cookie)
    return resp.text

# 格式化座位列表
def decoder(txt):
    txt = txt.replace(':"[', ':[')
    txt = txt.replace(']"', ']')
    txt = re.sub(r'\\', '', txt)
    return json.loads(txt)

# 抢座
def setseat(SessionId, seat, date, time, refer):
    data = {
        'data_type': 'seatDate',
        'seatno': seat,
        'seatdate': date,
        'datetime': time
    }

    headers = {
        'Host': 'chaxin.hnu.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '75',
        'Accept': 'application/json',
        'Origin': 'http://chaxin.hnu.edu.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MIX 2S Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2693 MMWEBSDK/201001 Mobile Safari/537.36 MMWEBID/1531 MicroMessenger/7.0.20.1781(0x2700143F) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': refer,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4'
    }
    cookie = {
        'cookie_unit_name': cookie_unit_name,
        'ASP.NET_SessionId': SessionId,
        'dt_cookie_user_name_remember': dt_cookie_user_name_remember
    }

    data = urllib.parse.urlencode(data)
    url = 'http://chaxin.hnu.edu.cn/mobile/ajax/seat/SeatDateHandler.ashx'
    resp = requests.post(url, data=data, headers=headers, cookies=cookie)
    print(resp.json())
    return resp.json()


if __name__ == "__main__":
    (date, study_time, SessionId) = init()
    times = 1
    while times <= 12 * 1 :
        print("第{:d}次尝试".format(times))
        for address in ['hnu_lib4_3F1', 'hnu_lib4_4F1']:
            refer = getRefer(address, date)
            SessionId = 'rr5isn22hlfiuyrib5xmwzjv'
            code = 1
            error = 0
            data = []
            # 获取座位
            while code != 0:
                if error == 3:
                    print("{}No Seat!".format(address))
                    break
                data = getseat(SessionId, address, date, refer)
                data = decoder(data)
                print(data['msg'])
                code = data['code']
                error += 1
                time.sleep(1)
            # 抢座
            error = 0
            for seat in data['data']:
                if error == 3:
                    break
                if seat['ShowDataTime'] == "暂无":
                    print(seat)
                    resp = setseat(SessionId, seat['Code'], date, study_time, refer)
                    if resp['code'] == 0:
                        json_data = {"code": 1,"time":datetime.datetime.now().__str__()}
                        with open('E:/personal/study/Python/bugger/code.json', "w") as jsonFile:
                            json.dump(json_data, jsonFile, ensure_ascii=False)
                        input("Press <enter>")
                        sys.exit(0)
                    error += 1
                    time.sleep(0.5)
        time.sleep(5)
        times+=1
    input("Press <enter>")
