from zzcore import StdAns
import requests
import sxtwl
from datetime import datetime
from config import HFWEATHERKEY


class Ans(StdAns):
    def GETMSG(self):
        msg = f'早上好，今天是{calendar()}\n\n'
        msg += getWeather() + '\n\n'
        t = requests.get('https://v1.hitokoto.cn/?c=k&encode=text').text
        # t = ("预祝大家四六级考试顺利。")
        msg += t
        return msg


def getWeather(id='101120206'):
    def wemoji(text):
        if '雪' in text:
            return text + '🌨'
        if '雨' in text:
            return text + '🌧️'
        if '阴' in text:
            return text + '⛅'
        if '云' in text:
            return text + '🌤'
        if '晴' in text:
            return text + '☀️'
        return text

    url = 'https://devapi.heweather.net/v7/weather/3d'
    params = {
        'location': id,
        'key': HFWEATHERKEY,
    }
    r = requests.get(url=url, params=params).json()
    tdw = r['daily'][0]
    ndw = r['daily'][1]
    weather = f"今日日间{wemoji(tdw['textDay'])}，温度{tdw['tempMin']}～{tdw['tempMax']}℃，{tdw['windDirDay']}{tdw['windScaleDay']}级；夜间{wemoji(tdw['textNight'])}，{tdw['windDirNight']}{tdw['windScaleNight']}级。明日日间{wemoji(ndw['textDay'])}，温度{ndw['tempMin']}～{ndw['tempMax']}℃。"
    if float(tdw['precip']) > 0:
        weather += '\n记得收好衣服，出门带伞~'
    
    return weather


def calendar():

    ymc = ["冬", "腊", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五",
           "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]
    zmc = ["一", "二", "三", "四", "五", "六", "天"]
    nowdate = datetime.now()
    y = nowdate.year
    m = nowdate.month
    d = nowdate.day
    zc = int(nowdate.strftime("%W")) - 1

    z = zmc[nowdate.weekday()]

    lunar = sxtwl.Lunar()
    lunarday = lunar.getDayBySolar(y, m, d)

    lunardaychinese = f"{ymc[lunarday.Lmc]}月{rmc[lunarday.Ldi]}"
    if lunarday.Lleap:
        lunardaychinese = "闰" + lunardaychinese

    cal = f"{m}月{d}日，{lunardaychinese}，寒假第{zc}周，星期{z}"
    return cal
