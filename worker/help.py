from zzcore import StdAns
from config import ALLWORKERS

class Ans(StdAns):
    def GETMSG(self):
        if ALLWORKERS:
            msg = '咱支持下面的'+str(len(ALLWORKERS)) + '个命令呢.'
            for work in ALLWORKERS:
                msg = msg + '\n' + work
        else:
            msg = '某人忘了往congif里写配置了吧,笨蛋!'                
        
        return msg