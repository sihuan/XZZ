from zzcore import StdAns
from subprocess import getoutput

class Ans(StdAns):
    def GETMSG(self):
        if self.parms[1] == 'status':
            return getoutput('spigot status')
        AllowCmd = ['list','tps']
        if self.parms[1] in AllowCmd:
            cmd = 'spigot command '
            cmd = cmd + self.parms[1]
            return getoutput(cmd)
        else:
            return self.parms[1] + ' 是暂时不被允许的命令！'