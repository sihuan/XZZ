from zzcore import StdAns
import re
from subprocess import getoutput

class Ans(StdAns):
    def GETMSG(self):
        cmd = self.parms[1]
        if cmd == 'status':
            return getoutput('spigot status')
        AllowCmd = ['list']
        if cmd in AllowCmd:
            if cmd == 'list':
                output = getoutput('spigot status')
                p = re.compile(r'There are (.*?)[ of a max]', re.S)
                online = int(re.findall(p,output)[0])
                if online == 0:
                    msg =  '咱看着没有人在线哎\n_(-ω-`_)⌒)_'
                else:
                    msg = '有' + str(online) + '个小伙伴在线!'
                    p = re.compile(r'online: (.*?)[\n>]', re.S)
                    players = re.findall(p,output)[0].split(', ')
                    for player in players:
                        msg = msg + '\n' + player
                    return msg
        else:
            return self.parms[1] + ' 是暂时不被允许的命令！'