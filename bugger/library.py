# -*- coding:utf-8 -*-
# coding:utf-8
import datetime
import json
import requests
import urllib
import re

area_name_dic = {
    'hnu_lib1':'总馆',
    'hnu_lib2':'特藏分馆',
    'hnu_lib3':'财院分馆',
    'hnu_lib4':'德智园分馆'
}

address_name_dic = {
    'hnu_lib1_1F1':'总馆一楼外文文献借阅室',
    'hnu_lib1_2F1':'总馆二楼读者服务中心',
    'hnu_lib1_3F1':'总馆三楼中文社科文献借阅室',
    'hnu_lib1_3F2':'总馆三楼自习室',
    'hnu_lib1_4F1':'总馆四楼中文自科文献借阅室(一)',
    'hnu_lib1_5F1':'总馆五楼中文自科文献借阅室(二)',
    'hnu_lib1_6F1':'总馆六楼中文自科文献借阅室(三)',
    'hnu_lib1_7F1':'总馆七楼中文自科文献借阅室(四)',
    'hnu_lib1_8F1':'总馆八楼自习室',
    'hnu_lib4_3F1':'德智园分馆四楼借阅室',
    'hnu_lib4_4F1':'德智园分馆四楼借阅室'
}

study_time_dic = [(12,18),(18,22.5),(12,22.5),(12,22.5),(18,22.5),(14,22.5),(14,22.5)]
dt_cookie_user_name_remember = '3FE3638936E97946C744EF0BCA3F5B835ADB779878D74FFD'

# 生成Refer
def getRefer(address, date):
    address_name = address_name_dic[address]
    address_name=urllib.parse.quote(address_name)
    area_name = area_name_dic[address[:8]]
    area_name=urllib.parse.quote(area_name)
    refer = 'http://chaxin.hnu.edu.cn/mobile/html/seat/seat_tujian.html?v=20200517&seataddress={}&seatdate={}&address_name={}&area_name={}'.format(address, date, address_name, area_name)

# 登录
def login():
    data = {
        'rdid':'77357248703862324E495533364E34436153644D77673D3D',
        'libcode':'55344B7855786A5165736653714730754853434969513D3D',
        'name':'舒俊锋',
        'openid':"omIDgjoFhNWG6ZBycX3-1t0LiUmw"
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
    cookie={ 
        # 'CCKF_visitor_id_144692' : '1299268355',
        # 'UM_distinctid' : '17478f18be55c9-0b266fdff9b052-58321f4d-144000-17478f18be6dad',
        # 'pgv_pvi' : '3370444800',
        # 'Hm_lvt_d7e34467518a35dd690511f2596a570e' : "1606406616,1606406645,1606406659,1606579508",
        # 'Hm_lpvt_d7e34467518a35dd690511f2596a570e' : '1606580853'
    }

    data = json.dumps(data)
    url = 'http://chaxin.hnu.edu.cn/api/hnu/CheckReader.aspx'
    resp = requests.get(url,data=data,headers=headers,cookies = cookie)
    print(requests.utils.dict_from_cookiejar(resp.cookies))
    return requests.utils.dict_from_cookiejar(resp.cookies)['ASP.NET_SessionId']

# 座位列表
def getseat(SessionId, address, date, refer):
    data = {
        'data_type':'GetTuiJianSeat',
        'addresscode':address,
        'seatdate':date
    }

    headers = {
        'Host': 'chaxin.hnu.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '69',
        'Accept': 'application/json',
        'Origin': 'http://chaxin.hnu.edu.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MIX 2S Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2693 MMWEBSDK/201001 Mobile Safari/537.36 MMWEBID/1531 MicroMessenger/7.0.20.1781(0x2700143F) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': refer,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    cookie={ 
        # 'DSSTASH_LOG':'C_4-UN_4965-US_-1-T_1606273080103',
        # 'mduxiu':'musername,=blmobile,!muserid,=1000086,!mcompcode,=1147,!menc,=A68AC0E8A1B0AA007DBB8ABEC1A4B522',
        # 'xc':'5',
        # 'pgv_pvi':'7489844224',
        # 'pgv_si':'s4753588224', 
        # 'mgid':'269',
        # 'maid':'59',
        # 'msign_dsr':'1606273080114',
        'ASP.NET_SessionId':SessionId,
        'dt_cookie_user_name_remember':dt_cookie_user_name_remember
    }

    data = urllib.parse.urlencode(data)
    url = 'http://chaxin.hnu.edu.cn/mobile/ajax/seat/SeatInfoHandler.ashx'
    resp = requests.post(url,data=data,headers=headers,cookies = cookie)
    # print(resp.text)
    return resp.text

# 格式化座位列表
def decoder(txt):
    txt = txt.replace(':"[',':[')
    txt = txt.replace(']"',']')
    txt = re.sub(r'\\','',txt)
    # print(txt)
    return json.loads(txt)

# 抢座
def setseat(SessionId, seat, date, time, refer):
    data = {
        'data_type':'seatDate',
        'seatno': seat,
        'seatdate': date,
        'datetime':time
    }

    headers = {
        'Host': 'chaxin.hnu.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '76',
        'Accept': 'application/json',
        'Origin': 'http://chaxin.hnu.edu.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MIX 2S Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2693 MMWEBSDK/201001 Mobile Safari/537.36 MMWEBID/1531 MicroMessenger/7.0.20.1781(0x2700143F) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': refer,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    cookie={ 
        # 'DSSTASH_LOG':'C_4-UN_4965-US_-1-T_1606273080103',
        # 'mduxiu':'musername,=blmobile,!muserid,=1000086,!mcompcode,=1147,!menc,=A68AC0E8A1B0AA007DBB8ABEC1A4B522',
        # 'xc':'5',
        # 'pgv_pvi':'7489844224',
        # 'pgv_si':'s4753588224', 
        # 'mgid':'269',
        # 'maid':'59',
        # 'msign_dsr':'1606273080114',
        'ASP.NET_SessionId':SessionId,
        'dt_cookie_user_name_remember':dt_cookie_user_name_remember
    }

    data = urllib.parse.urlencode(data)
    url = 'http://chaxin.hnu.edu.cn/mobile/ajax/seat/SeatDateHandler.ashx'
    resp = requests.post(url,data=data,headers=headers,cookies = cookie)
    print(resp.json())
    return resp.json()

if __name__ == "__main__":
    time_next = datetime.date.today() + datetime.timedelta(days=1) #获取后一天
    date = (time_next).strftime("%Y-%m-%d")
    (start, end) = study_time_dic[time_next.weekday()]
    study_time = '{:d},{:d}'.format(int(start*60),int(end*60))
    print(date) 
    print(study_time)
    for address in ['hnu_lib4_3F1','hnu_lib4_4F1','hnu_lib1_2F1']:
        refer = getRefer(address, date)
        # SessionId=login()
        data = getseat('zlahqxwie0iw5qf2vi1bhaxq', address, date, refer)
        data = decoder(data)
        for seat in data['data']:
            if seat['ShowDataTime'] == "暂无":
                print(seat)
                # resp = setseat(SessionId, seat['Code'], date, study_time, refer)
                if resp['code'] == 0:
                    return
