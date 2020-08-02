from zzcore import StdAns

class Ans(StdAns):
    AllowUser = [1318000868]

    def GETMSG(self):
        groups = self.getgroups()
        
        msg = groups
        # for g in groups:
        #     msg += g["groupname"]

        return msg
