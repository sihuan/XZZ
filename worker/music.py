from zzcore import StdAns
import requests

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'
        
        # url = 'https://api.imjad.cn/cloudmusic/'
        url = 'https://music.jeeas.cn/v1/search'
        # url = 'http://mc.sakuya.love:3000/search'
        params = {
            'limit': 1,
            's':self.raw_msg['message'][6:],
        }
        try:
            resp = requests.get(url=url,params=params).json()
            # print(resp)
            musicid = resp['result']['songs'][0]['id']
            musicname = resp['result']['songs'][0]['name']
            msg =  '[CQ:share,url=https://music.163.com/song/' + str(musicid) + '/,title=' + str(musicname) + ']'
        except Exception as e:
            print(e)
            msg = '什么东西坏掉了,大概是网易云吧...不可能是咱!'
        return msg
