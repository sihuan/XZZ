from zzcore import StdAns, mysakuya
import requests

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'

        if mysakuya(self, self.raw_msg['message']) == False:
            return "不许你们说咲夜！！"

        msg = f"[CQ:reply,id={self.raw_msg['message_id']}]"
        r = nbnhhsh(self.raw_msg['message'][6:])
        for i in r:
            msg += f"{i['name']} {str(i['trans'])[1:-1]}\n"
        
        return msg


def nbnhhsh(text):
    url = 'https://lab.magiconch.com/api/nbnhhsh/guess'
    data = {
        'text': text,
    }

    r = requests.post(url=url, data=data).json()
    return r