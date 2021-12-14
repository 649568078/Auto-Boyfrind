import random
import requests
import send_qq
import send_wechat
import datetime
import time

res = requests.get('https://img1.doubanio.com/view/photo/l/public/p2709322587.webp')
pic = res.content
t = datetime.datetime.now()
t1 = t.strftime('%Y%m%d%H%M%S')
with open(t1+".webp",'wb') as f:
    f.write(pic)
# send_qq.sendImage('花生',t1+".webp")
send_wechat.sendImage('花生',t1+".webp")