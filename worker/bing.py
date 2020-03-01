from zzcore import StdAns
from config import BINGKEY

import requests

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'

        url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
        params = {
            'q':self.raw_msg['message'][5:],
            'count': 1,
        }
        headers = {
            'Ocp-Apim-Subscription-Key': BINGKEY,
        }
        try:
            resp = requests.get(url=url,params=params,headers=headers).json()
            result = resp['webPages']['value'][0]
            msg =  '[CQ:at,qq=' + str(self.uid) + ']' + '咱帮你🔍到了这个\n' + result['name']
            self.sendmsg(msg)
            msg = result['url']
        except:
            msg = '什么东西坏掉了,大概是bing吧...不可能是咱!'
        return msg
