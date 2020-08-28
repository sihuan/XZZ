import random
import requests
import datetime

class Ans(object):
    """docstring for Ans"""
    def __init__(self):
        super(Ans).__init__()

    def GETMSG(self):
        try:
            return self.get_weather()
        except Exception as e:
            return "啊哦，出错了"

    def get_weather(self):
        ran = random.randint(0, 9999999999)
        url = "https://api.caiyunapp.com/v2/Y2FpeXVuIGFuZHJpb2QgYXBp/120.127164,36.000129/weather?lang=zh_CN&device_id={}".format(ran)
        res = requests.get(url).json()
        msg = "XZZ为您播报近期天气\n-------------------------------------\n"
        msg += "日期  |  温度  |  湿度  |  天气  |\n-------------------------------------"
        result = res["result"]["daily"]
        now = datetime.datetime.now()
        weather_summary = {
            "CLEAR_DAY": "晴",
            "CLEAR_NIGHT": "晴",
            "CLOUD_DAY_WIDGET": "多云转晴",
            "CLOUDY": "阴",
            "HAZE": "霾",
            "HAZE_WIDGET": "霾",
            "PARTLY_CLOUD_NIGHT": "多云转晴",
            "PARTLY_CLOUD_NIGHT_WIDGET": "多云转晴",
            "PARTLY_CLOUD_WIDGET": "阴",
            "PARTLY_CLOUDY_DAY": "多云转晴",
            "PARTLY_CLOUDY_NIGHT": "多云转晴",
            "RAIN": "雨",
            "RAIN_HEAVY": "大雨",
            "RAIN_LIGHT": "小雨",
            "RAIN_MIDDLE": "中雨",
            "RAIN_NORMAL_WIDGET": "大雨",
            "SNOW": "雪",
            "SNOW_WIDGET": "雪",
            "SUNSHINE_NIGHT_WIDGET": "晴",
            "SUNSHINE_WIDGET": "晴",
            "WIND": "晴",
        }
        for i in range(5):
            msg += "\n"
            msg += "{} | ".format((now + datetime.timedelta(days=i)).strftime("%Y-%m-%d"))
            msg += "{} | ".format(format(result["temperature"][i]["avg"], ".2f"))
            msg += "{} | ".format(format(result["humidity"][i]["avg"], ".2f"))
            msg += "{} | ".format(weather_summary[result["skycon"][i]["value"]])
        return msg

if __name__ == "__main__":
    Ans().GETMSG()
        