import requests
from zzcore import StdAns

class Ans(StdAns):
    AllowGroup = [959613860, 983250332]
    def GETMSG(self):
        seconds = int(requests.get("http://127.0.0.1:8095/").text)
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return f'{h}小时{m}分钟{s}秒前有人来过。'
