from zzcore import StdAns, mysakuya
import requests

class Ans(StdAns):
    def GETMSG(self):
        msg=''
        try:
            msg += xs()
        except:
            msg += '可能是机器人笑死了！'
        return msg

def xs():
    url = "http://api-x.aya1.xyz:6/"
    text = requests.get(url=url).text
    return text
