from zzcore import StdAns, mysakuya


class Ans(StdAns):
    NotAllowGroup = [204097403]

    def CheckPermission(self):
        if self.gid in self.NotAllowGroup:
            return -1
        return 0

    def GETMSG(self):
        if self.parms:

            if mysakuya(self, self.raw_msg['message']) == False:
                return "咲夜是最完美的！！"
                
            return '咱也不知道' + self.parms[0] + '是啥呢~'
        else:
            return '汝再调戏咱，咱可就生气了！！'
