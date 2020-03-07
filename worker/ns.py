from zzcore import StdAns
from subprocess import check_output

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'

        domain = self.raw_msg['message'][4:]
        try:
            answer = check_output(['nslookup',domain],shell=False,timeout=4)
            msg = bytes.decode(answer)
        except:
            msg = '汝干了什么！ ns 超时了！'
        return msg
