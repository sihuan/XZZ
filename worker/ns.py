from zzcore import StdAns
import os

class Ans(StdAns):
    def GETMSG(self):
        domain = 'www.qq.com'
        p = os.popen("nslookup " + domain)
        msg = p.read()
        return msg