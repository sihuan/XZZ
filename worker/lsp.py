from zzcore import StdAns, mysakuya
import requests

from config import LOLIKEYS


class Ans(StdAns):
    AllowGroup = [874769998, 596678277, 794290657, 204097403]

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
        'apikey': LOLIKEYS,
        'keyword': keyword,
        'r18': 0
    }

    try:
        resp = requests.get(url=url, params=params, timeout=5).json()
    except:
        return 500, ''

    picurl = ''
    if resp['code'] == 0:
        picurl = "https://r.zjuyk.site/" + resp['data'][0]['url']

    return resp['code'], picurl
