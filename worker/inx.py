from zzcore import StdAns
import requests, time

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'
        cmd = self.parms[1]
        AllowCmd = ['start','stop']

        if  cmd in AllowCmd:
            if cmd == 'stop':
                self.DATASET({'status':'0'})
                return '我已知晓你希望 inx 停止.'
            if cmd == 'start':
                self.DATASET({'status':'1'})
                self.sendmsg('inx 启动！')
                pinx = 0
                pixic = 0
                pdji = 0
                while(self.DATAGET()['status'] == '1'):
                    inx, ixic, dji = getMG()
                    msg = '标普500 现在的涨跌幅度: ' + inx + ' ' + emoji(pinx,inx) + '纳斯达克现在的涨跌幅度: ' + ixic + ' ' +  emoji(pixic,ixic) + '道琼斯指数现在的涨跌幅: ' + dji + ' ' +  emoji(pdji,dji)
                    self.sendmsg(msg)
                    pinx = inx
                    pixic = ixic
                    pdji = dji
                    time.sleep(16)

                return "现在 inx 真的停了！"

        else:
            return '汝是不是在inx后面添加了奇怪的参数，咱可只知道 start 和 stop。'


def getMG():
    req = requests.get("https://hq.sinajs.cn/etag.php?_=1584712625172&list=gb_$inx,gb_$ixic,gb_$dji").text.split(',')
    return req[2], req[29], req[56]

def emoji(p,n):
    n = float(n)
    p = float(p)
    if n < p:
        emoji = '🟩🟩🟩🎉\n'
    elif n > p:
        emoji = '🟥🟥🟥😢\n'
    else :
        emoji = '⬜⬜⬜🌚\n'
    return emoji
