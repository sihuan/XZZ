from zzcore import StdAns, mysakuya
import requests

class Ans(StdAns):
    def GETMSG(self):
        msg = f"[CQ:reply,id={self.raw_msg['message_id']}]"
        try:
            msg += wyy()
        except:
            msg += '可能是网抑云坏掉了，可不是咱！'
        return msg

def wyy():
    r = requests.get(url='http://api.heerdev.top:4995/nemusic/random').json()
    return r['text']