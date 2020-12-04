import requests
import json
import urllib
import time
import random
from PIL import Image
from aip import AipOcr

data = {"studentId":["201801120127","201801120102","201801120103","201801120129"],
        "password" :["Aolong0813","forever1314ZY","Rwanwanwan2333","Wh890912."]}

# 获取验证码随机Token
def getimgvcode():
    url = "https://fangkong.hnu.edu.cn/api/v1/account/getimgvcode"
    headers = {
            'Host': 'fangkong.hnu.edu.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://fangkong.hnu.edu.cn',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://fangkong.hnu.edu.cn/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }
    resp = requests.get(url, headers=headers, verify = False)
    # resp = requests.get(url, headers=headers,cert='fangkong/fangyi.cer')
    return resp.json()['data']['Token']

# 获取验证码图片
def getimg(token):
    url = "https://fangkong.hnu.edu.cn/imagevcode?token={}".format(token)
    headers = {
            'Host': 'fangkong.hnu.edu.cn',
            'Connection': 'keep-alive',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://fangkong.hnu.edu.cn',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': 'https://fangkong.hnu.edu.cn/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }
    response = urllib.request.urlopen(url)
    pic = response.read()
    return pic

# 识别验证码
def decord(pic):
    AppID = '123061489'
    API_Key = '5tsCETiTgH4q4IhMzl29zgj7'
    Secret_Key = 's1T2eqCb6Ki4iI7VfxCNhYtl4HBNnTRP'
    client = AipOcr(AppID, API_Key, Secret_Key)
    res=client.basicGeneral(pic)
    # print(res['words_result'][0]['words'])
    return res['words_result'][0]['words']

# 登录
def login(token, verCode, studentId, password):
    data = {
        'Code': studentId,
        'Password': password,
        'Token': token,
        'VerCode': verCode,
        'WechatUserinfoCode': None
    }
    headers = {
            'Host': 'fangkong.hnu.edu.cn',
            'Connection': 'keep-alive',
            'Content-Length': '133',
            'Accept': 'application/json, text/plain, */*',
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://fangkong.hnu.edu.cn',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://fangkong.hnu.edu.cn/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }

    cookie={ 
        # 'CCKF_visitor_id_144692' : '1299268355',
        # 'UM_distinctid' : '17478f18be55c9-0b266fdff9b052-58321f4d-144000-17478f18be6dad',
        # 'pgv_pvi' : '3370444800',
        # 'Hm_lvt_d7e34467518a35dd690511f2596a570e' : "1606406616,1606406645,1606406659,1606579508",
        # 'Hm_lpvt_d7e34467518a35dd690511f2596a570e' : '1606580853'
    }

    data = json.dumps(data)
    url = 'https://fangkong.hnu.edu.cn/api/v1/account/login'
    resp = requests.post(url,data=data,headers=headers,cookies = cookie, verify = False)
    print("login:"+str(resp.json()['code'])+':'+resp.json()['msg'])
    return resp.json()['code'],requests.utils.dict_from_cookiejar(resp.cookies)

# 打卡
def daka(aspxauth, token):
    url = 'https://fangkong.hnu.edu.cn/api/v1/clockinlog/add/'
    data = {'BackState': 1,
        'Latitude': None,
        'Longitude': None,
        'MorningTemp': random.randrange(365,373)/10.0,
        'NightTemp': random.randrange(365,373)/10.0,
        'RealAddress': "正在获取定位...",
        'RealCity': None,
        'RealCounty': None,
        'RealProvince': None,
        'tripinfolist': []
    }
    #把cookie字符串处理成字典，以便接下来使用
    headers = {
            'Host': 'fangkong.hnu.edu.cn',
            'Connection': 'keep-alive',
            'Content-Length': '198',
            'Accept': 'application/json, text/plain, */*',
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://fangkong.hnu.edu.cn',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://fangkong.hnu.edu.cn/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }
    cookies = {
        # 'CCKF_visitor_id_144692':'1299268355',
        # 'UM_distinctid':'17478f18be55c9-0b266fdff9b052-58321f4d-144000-17478f18be6dad',
        # 'pgv_pvi':'3370444800',
        # 'Hm_lvt_d7e34467518a35dd690511f2596a570e':'1606406616,1606406645,1606406659,1606579508',
        # 'Hm_lpvt_d7e34467518a35dd690511f2596a570e':'1606580853',
        '.ASPXAUTH':aspxauth,
        'TOKEN':token
    }
    #在发送get请求时带上请求头和cookies
    resp = requests.post(url,data=json.dumps(data),headers=headers,cookies = cookies, verify = False)
    print(resp.json())
    return resp.json()['code']

if __name__ == "__main__":
    for i in range(4):
        code = 1
        while code!=0:
            token = getimgvcode()
            pic = getimg(token)
            VerCode = decord(pic)
            code,cookie = login(token, VerCode, data['studentId'][i], data['password'][i])
            time.sleep(1)
        while daka(cookie['.ASPXAUTH'],cookie['TOKEN'])!=0:
            time.sleep(1)
        print("No.{}:successful!".format(i))
        