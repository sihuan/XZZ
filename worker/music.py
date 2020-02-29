from zzcore import StdAns
import requests

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'
        
        url = 'http://47.100.45.234/search'
        params = {
            'keywords':self.raw_msg['message'][6:],
            'limit': 1,
        }
        try:
            resp = requests.get(url=url,params=params).json()
            musicid = resp['result']['songs'][0]['id']
            msg =  '[CQ:music,type=163,id='+ str(musicid)+']'
        except Exception as e:
            print(e)
            msg = '什么东西坏掉了,大概是网易云吧...不可能是咱!'
        return msg
