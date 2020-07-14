from zzcore import StdAns


class Ans(StdAns):
    NotAllowGroup = [204097403]

    def CheckPermission(self):
        if self.gid in self.NotAllowGroup:
            return -1
        return 0

    def GETMSG(self):
        if self.parms:
            if self.uid != 1318000868:
                for sakuya in ['口关夜','十六夜咲夜','十六夜','十六','咲夜','Sakuya','sakuya','Izayoi Sakuya','Izayoi','izayoi','izayoi sakuya']:
                    if sakuya in self.parms[0]:
                        return "咲夜是最完美的！！"
            return '咱也不知道' + self.parms[0] + '是啥呢~'
        else:
            return '汝再调戏咱，咱可就生气了！！'
