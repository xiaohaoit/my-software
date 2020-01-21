# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:36:45 2020

@author: 日天网络
"""

import requests
import hashlib
import base64
import json
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ef234377-1cb5-4cb4-91fb-9bf60ce589a2"
#url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9ceafd23-3008-4f95-9f5e-c4e88b96994d"
headers = {"Content-Type": "application/json"}
#发送图片
#img_p = "./Export/DailyPaper_20200118.png"
#with open(img_p,"br") as f:
#    ront = f.read()
#    basee64 = base64.b64encode(ront)
#    mdd5 = hashlib.md5(ront)
#data = {
#      "msgtype": "image",
#      "image": {
#        "base64": basee64.decode('utf8'),
#        "md5": mdd5.hexdigest()
#      }
#   }
#data_j = json.dumps(data)
#r = requests.post(url, data=data_j)

#发送图文消息
data = {
         "msgtype": "news",
         "news": {
                 "articles" : [
          {
               "title" : "“鼠你最有福”——潭州福卡大放送将于明日截止！",
               "description" : "“潭州福卡大放送活动正在如火如荼地进行中：红牌赢，还是黑牌赢？",
               "url" : "https://mp.weixin.qq.com/s/BoxhHNHDMje7mpaSE-Ff9Q",
               "picurl" : "http://chuantu.xyz/t6/713/1579349991x1031866013.png"
           }
                   ]
          }
        
        }
r = requests.post(url,headers=headers,json=data)

print(r.text)
