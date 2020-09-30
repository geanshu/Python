import requests
url='http://ntscdtu.xindun.hn.cn:5566/value/IntelSw/rlvalue?token=27CAE903&ide=503316%d'%(50)
response = requests.get(url).json()
response=response[0]
print({'tm':response['outertm'],'hu':response['outerhu']})