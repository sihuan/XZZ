from zzcore import StdAns, mysakuya
import requests

class Ans(StdAns):
    #AllowGroup = [874769998,596678277]
    def GETMSG(self):
        msg = f"[CQ:reply,id={self.raw_msg['message_id']}]"
        try:
            msg += tiangou()
        except:
            msg += '可能是api坏掉了，可不是咱！'
        return msg

def tiangou():
    r = requests.get(url='https://api.muxiaoguo.cn/api/tiangourj').json()
    # print(r)
    msg = None
    if r['msg'] == 'success':
        msg = r['data']['comment']
    return msg
