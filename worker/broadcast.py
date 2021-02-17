from zzcore import StdAns

class Ans(StdAns):
    AllowUser = [1318000868]

    def GETMSG(self):
        groups = self.getgroups()
        text = self.raw_msg['raw_message'][11:]
        gid = self.gid
        
        for g in groups:
            self.gid = g['group_id']
            self.sendmsg(text)
        
        self.gid = gid

        return "Broadcast done."
