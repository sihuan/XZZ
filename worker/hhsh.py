from zzcore import StdAns, mysakuya
import requests

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'

        if mysakuya(self, self.raw_msg['raw_message']) == False:
            return "不许你们说咲夜！！"

        msg = f"[CQ:reply,id={self.raw_msg['message_id']}]"
        r = nbnhhsh(self.parms[1])
        msg += f'''{(str(r['trans'])[1:-1]).replace("'","").replace(","," ")}'''
        
        return msg


def nbnhhsh(text):
    url = 'https://lab.magiconch.com/api/nbnhhsh/guess'
    data = {
        'text': text,
    }

    r = requests.post(url=url, data=data).json()
    return r[0]