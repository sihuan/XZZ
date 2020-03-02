from zzcore import StdAns
from subprocess import run

class Ans(StdAns):
    def GETMSG(self):
        domain = self.raw_msg['message'][4:]
        msg = run(["nslookup",domain],capture_output=True)
        return msg
