from zzcore import StdAns, mysakuya
import requests

from config import LOLIKEY


class Ans(StdAns):
    AllowGroup = [959613860, 973510746, 805197917, 343700338, 125733077, 1084566280,
                  920863253, 798595664, 655057127, 196268763, 247022495, 474907856, 940333876,
                  204097403]

    def GETMSG(self):
        if len(self.parms) == 1:
            code, picurl = getsetu()
        else:
            keyword = self.parms[1]
            if mysakuya(self, keyword) == False:
                return "不许你们看咲夜的涩图！！"
            code, picurl = getsetu(keyword)
        if code == 0:
            return f'[CQ:reply,id={self.mid}][CQ:image,file={picurl},type=flash]'
        else:
            return f'[CQ:reply,id={self.mid}] 什么东西出错了，code:{code}'


def getsetu(keyword=''):
    url = 'https://api.lolicon.app/setu/'
    params = {
        'apikey': LOLIKEY,
        'keyword': keyword,
    }

    try:
        resp = requests.get(url=url, params=params, timeout=5).json()
    except:
        return 500, ''

    picurl = ''
    if resp['code'] == 0:
        picurl = "https://r.zjuyk.site/" + resp['data'][0]['url']

    return resp['code'], picurl
