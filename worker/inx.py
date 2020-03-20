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
                while(self.DATAGET()['status'] == '1'):
                    req = requests.get("https://hq.sinajs.cn/etag.php?_=1584712625172&list=gb_$inx")
                    num = req.text[28:].split(",")[1]
                    msgid = self.sendmsg('标普500现在情况:  ' + num)
                    time.sleep(10)
                    self.delmsg(msgid)
                    
                return "现在 inx 真的停了！"

        else:
            return '汝是不是在inx后面添加了奇怪的参数，咱可只知道 start 和 stop。'