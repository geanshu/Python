import requests
import json
import urllib
from PIL import Image
from aip import AipOcr

# 获取验证码
def getimgvcode():
    url = "https://fangkong.hnu.edu.cn/api/v1/account/getimgvcode"
    resp = requests.get(url)
    return resp.json()['data']['Token']

def getimg(token):
    url = "https://fangkong.hnu.edu.cn/imagevcode?token={}".format(token)
    file = 'pic.jpg'
    # resp = requests.get(url)
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def decord(pic):
    AppID = '123061489'
    API_Key = '5tsCETiTgH4q4IhMzl29zgj7'
    Secret_Key = 's1T2eqCb6Ki4iI7VfxCNhYtl4HBNnTRP'
    client = AipOcr(AppID, API_Key, Secret_Key)
    res=client.basicGeneral(pic)
    print(res['words_result'][0]['words'])
    return res['words_result'][0]['words']

def login(Token, VerCode):
    data = {
        'Code': "201801120127",
        'Password': "Aolong0813",
        'Token': Token,
        'VerCode': VerCode,
        'WechatUserinfoCode': ''
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

    Cookie={ 
        'CCKF_visitor_id_144692' : '1299268355',
        'UM_distinctid' : '17478f18be55c9-0b266fdff9b052-58321f4d-144000-17478f18be6dad',
        'pgv_pvi' : '3370444800',
        'Hm_lvt_d7e34467518a35dd690511f2596a570e' : "1606406616,1606406645,1606406659,1606579508",
        'Hm_lpvt_d7e34467518a35dd690511f2596a570e' : '1606580853'
    }

    data = json.dumps(data)
    url = 'https://fangkong.hnu.edu.cn/api/v1/account/login'
    resp = requests.post(url,data=data,headers=headers,cookies = Cookie)
    print(resp.json()['msg'])
    return requests.utils.dict_from_cookiejar(resp.cookies)

def daka(cookie):
    url = 'https://fangkong.hnu.edu.cn/api/v1/clockinlog/add/'
    data = {'BackState': 1,
        'Latitude': '',
        'Longitude': '',
        'MorningTemp': "36.6",
        'NightTemp': "36.6",
        'RealAddress': "正在获取定位...",
        'RealCity': '',
        'RealCounty': '',
        'RealProvince': '',
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
        'CCKF_visitor_id_144692':'1299268355',
        'UM_distinctid':'17478f18be55c9-0b266fdff9b052-58321f4d-144000-17478f18be6dad',
        'pgv_pvi':'3370444800',
        'Hm_lvt_d7e34467518a35dd690511f2596a570e':'1606406616,1606406645,1606406659,1606579508',
        'Hm_lpvt_d7e34467518a35dd690511f2596a570e':'1606580853',
        '.ASPXAUTH':cookie['.ASPXAUTH'],
        'TOKEN':cookie['TOKEN']
    }
    #在发送get请求时带上请求头和cookies
    resp = requests.post(url,data=json.dumps(data),headers=headers,cookies = cookies)
    print(resp.json)

if __name__ == "__main__":
    token = getimgvcode()
    pic = getimg(token)
    VerCode = decord(pic)
    cookie = login(token, VerCode)
    daka(cookie)