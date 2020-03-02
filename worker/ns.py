from zzcore import StdAns
from subprocess import Popen

class Ans(StdAns):
    def GETMSG(self):
        domain = self.raw_msg['message'][4:]
        p = Popen(["nslookup",domain])
        msg = p.read()
        return msg
