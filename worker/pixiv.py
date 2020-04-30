from zzcore import StdAns
import requests

from config import LOLIKEY

class Ans(StdAns):
    AllowGroup = [805197917,959613860,343700338,125733077]
    def GETMSG(self):
        url = 'https://api.lolicon.app/setu/'
        params = {
            'apikey': LOLIKEY,
        }

        if len(self.parms) < 2:        
            try:
                resp = requests.get(url=url,params=params).json()
                picurl = resp['data'][0]['url']
                msg =  picurl
            except Exception as e:
                print(e)
                msg = '什么东西坏掉了,大概是Pixiv吧...不可能是咱!'
            return msg

        else:
            keyword = self.raw_msg['message'][7:]
            params['keyword'] = keyword
            try:
                resp = requests.get(url=url,params=params).json()
                picurl = resp['data'][0]['url']
                msg =  picurl
            except Exception as e:
                print(e)
                msg = '咱没查到，也有可能是Pixiv坏掉了'
            return msg