import requests
import time
import csv

def login(str1,str2):
    url="http://59.67.0.220/a70.htm"

    datas={
    'DDDDD':str1,
    'upass':str2,
    'R1':'0',
    'R2':'',
    'R6':'0',
    'pare':'00',
    'OMKKey':'123456',
    'v6ip':'',
    'R7':'0'
    }

    req=requests.post(url,data=datas)
    if "您已经成功登录。" in req.text:
        return True
    else:
        return False


login()
