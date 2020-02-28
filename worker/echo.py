import random
from zzcore import StdAns

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'
        r = random.randint(1,3)
        if r == 1:
            msg = self.raw_msg['message'][5:]
        elif r == 2:
            msg = "汝以为咱会复读的嘛！\n(╯' - ')╯︵ ┻━┻\n" + self.raw_msg['message'][5:]
        elif r == 3:
            msg = '咱才不做复读机。→_→'
        return msg