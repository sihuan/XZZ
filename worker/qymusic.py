from zzcore import StdAns
import requests
import json

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '歌名都不指定就能搜到歌了？'
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
        params = {
            'ct': 24,
            'qqmusic_ver': 1298,
            'new_json': 1,
            'remoteplace': 'txt.yqq.song',
            'searchid': '',
            't': 0,
            'aggr': 1,
            'cr': 1,
            'catZhida': 1,
            'loseless': 0,
            'flag_qc': 0,
            'p': 1,
            'n': 20,
            'w':self.raw_msg['message'][8:],
        }
        try:
            resp = requests.get(url=url,params=params).text
            resp = json.loads(list(resp.split('callback('))[1][:-1])
            # print(resp)
            if resp['data']['song']['totalnum'] == 0:
                return '辣鸡曲库没这首，或者你的关键词有问题'
            mid = resp['data']['song']['list'][0]['mid']
            mname = resp['data']['song']['list'][0]['name']
            msg =  '[CQ:share,url=https://y.qq.com/n/yqq/song/' + str(mid) + '.html,title=' + str(mname) + ']'
        except Exception as e:
            print(e)
            msg = '辣鸡q音，太弟弟了（'
        return msg
