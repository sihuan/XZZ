from zzcore import StdAns

class Ans(StdAns):
    def GETMSG(self):
        if self.parms:
            return '咱也不知道' + self.parms[0] + '是啥呢~'
        else:
            return '汝再调戏咱，咱可就生气了！！' 