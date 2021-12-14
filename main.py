import send_qq
import requests
import datetime
import time
import random

def get_weather():
    rep = requests.get('https://restapi.amap.com/v3/weather/weatherInfo?city=110101&key=2ceedebfb5cbf22a2c8e6a4021069d20')
    rep.encoding = 'utf-8'
    jsdata = eval(rep.text)
    city = jsdata['lives'][0]['city']
    weather = jsdata['lives'][0]['weather']
    temperature = jsdata['lives'][0]['temperature']
    winddirection = jsdata['lives'][0]['winddirection']
    windpower = jsdata['lives'][0]['windpower']
    humidity = jsdata['lives'][0]['humidity']
    reporttime = jsdata['lives'][0]['reporttime'].split(' ')[0]
    text = '早上好，今天是{}\n{}的天气情况是({})\n温度:{}摄氏度\n风向:{}\n风力:{}\n空气湿度:{}'.format(reporttime,city,weather,temperature,winddirection,windpower,humidity,)
    print(text)
    return text

def get_news():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['note']
    news = ''
    news += contents
    news += translation
    print(news)
    return news

if __name__ == '__main__':
    name = '捏饼饼'
    hours = 8
    minutes = 30
    New_day = True
    sended_day = None
    while True:
        t = datetime.datetime.now()
        t1 = t.strftime('%Y-%m-%d %H:%M:%S')
        day = t.day
        hour = t.hour
        minute = t.minute
        second = t.second
        print('%d:%d:%d' % (hour, minute, second))
        # 对比日期，如果如果日期相同则New_day为False
        if day == sended_day:
            New_day = False
        # 到了新的一天
        else:
            New_day = True
        # 发送前的判断
        if hour == hours and minute == minutes and New_day == True:
            print("到时间了，准备发送")
            #设置一个随机等待时间，制造惊喜
            #time.sleep(random.randint(600,1200))
            # 请求接口，循环调用直到请求成功
            weather = ""
            news = ""
            while True:
                try:
                    weather = get_weather()
                    news = get_news()
                    break
                except Exception as e:
                    print(e)
                    time.sleep(10)
                    continue
            # 发送消息
            text = weather + "\n" + news
            print(text)
            send_qq.send(name, text)
            New_day = False
            sended_day = day
            time.sleep(82800)
        else:
            time.sleep(30)  # 延迟60秒
            continue
