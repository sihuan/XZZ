from zzcore import StdAns
from config import WOLFRAMALPHAAPPID
import wolframalpha

def wolframsearch(query):
    client = wolframalpha.Client(WOLFRAMALPHAAPPID)
    res = client.query(query)
    return res

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'

        try:
            res = wolframsearch(self.raw_msg['message'][9:])
            msg = next(res.results).text
        except Exception as e:
            print(e)
            msg = '什么东西坏掉了,大概是Wolfram | Alpha吧...不可能是咱!'
        return 