from zzcore import StdAns

from subprocess import getoutput

class Ans(StdAns):
    AllowUser = [1318000868]
    UserNotAllow = '汝不是咱的Master!'

    def GETMSG(self):
        output = getoutput('git pull')
        return output
