from zzcore import StdAns
import requests
import json

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'
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
                return '啊嘞嘞好像没有诶qaq'
            mid = resp['data']['song']['list'][0]['mid']
            # id = resp['data']['song']['list'][0]['id']
            msg = f'[CQ:music,type=qq,id={mid}]'
            # mname = resp['data']['song']['list'][0]['name']
            # msg =  '[CQ:share,url=https://y.qq.com/n/yqq/song/' + str(mid) + '.html,title=' + str(mname) + ']'
        except Exception as e:
            print(e)
            msg = '什么东西坏掉了,大概是疼讯吧...不可能是咱!'
        return msg
