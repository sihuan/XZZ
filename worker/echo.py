import random
from zzcore import StdAns

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'
        
        if self.uid != 1318000868:
            for sakuya in ['十六夜咲夜','十六夜','十六','咲夜','Sakuya','sakuya','Izayoi Sakuya','Izayoi','izayoi','izayoi sakuya']:
                if sakuya in self.raw_msg['message']:
                    return "不许你们说咲夜！！"

        r = random.randint(1,3)
        if r == 1:
            msg = self.raw_msg['message'][6:]
        elif r == 2:
            msg = "汝以为咱会复读的嘛！\n(╯' - ')╯︵ ┻━┻\n" + self.raw_msg['message'][5:]
        elif r == 3:
            msg = '咱才不做复读机。→_→'
        return msg