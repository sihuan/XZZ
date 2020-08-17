from zzcore import StdAns, mysakuya
import requests

from config import LOLIKEYS

class Ans(StdAns):
    AllowGroup = [973510746, 805197917,343700338,125733077,1084566280,920863253,798595664,655057127,196268763, 204097403, 247022495, 474907856]
    def GETMSG(self):

        keys = LOLIKEYS
        
        try:
            nowkey = int(self.DATAGET()['nowkey'])
        except:
            nowkey = 0

        if len(self.parms) < 2:
            keyword = ''
        else:
            keyword = self.parms[1]
            if mysakuya(self, keyword) == False:
                return "不许你们看咲夜的涩图！！"
            
        code, quota, picurl = getsetu(keys[nowkey], keyword)
        
        msg = ''
        if code == -1 or code == -2:
            msg += f'>_< 天啦喽，loli 不见了 Code:{code}'
        elif code == 3:
            msg += '咱没查到,也有可能是Pixiv坏掉惹'
        elif code == 0:
            if len(self.parms) < 2 or (len(self.parms > 2) and self.parms[2] == 'p'):
                msg += f'[CQ:image,file={picurl}]'
            else:
                msg += f'[CQ:reply,id={self.mid}]咱帮你🔍{keyword}找到了这个\n{picurl}'
                
        if quota == 0:
            nowkey = (nowkey+1)%(len(keys))
            if code == 429:
                msg += f'>_< 已经没有 loli 啦，帮你换到了key{nowkey}，再试一下吧'
            else:
                msg += f'额度用光了，下次将使用 key{nowkey}'
        self.DATASET({'nowkey':nowkey})
        return msg
        
        
def getsetu(apikey, keyword = ''):
    url = 'https://api.lolicon.app/setu/'
    params = {
        'apikey': apikey,
    }
    if keyword != '':
        params['keyword'] = keyword
        
    try:
        resp = requests.get(url=url,params=params).json()
    except:
        return -1, -1 ,''
    
    #quota = str(resp['quota'])
    #seconds = resp['quota_min_ttl']
    #m, s = divmod(seconds, 60)
    #h, m = divmod(m, 60)
    #quota_min_ttl = f'{h}时{m}分{s}秒'
    if resp['code'] == 0:
        quota = resp['quota']
        try:
            picurl = resp['data'][0]['url']
            code = 0
        except:
            picurl = ''
            code = -3
        return code, quota, picurl
    elif resp['code'] == 429:
        return 429, 0, ''
    else:
        return -2, -1, ''
