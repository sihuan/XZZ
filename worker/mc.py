from zzcore import StdAns
import re
from subprocess import getoutput,call

class Ans(StdAns):
    AllowGroup = [959613860, 125733077]
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'
        cmd = self.parms[1]
        AllowCmd = ['list','status','say']

        if cmd in AllowCmd:
            if cmd == 'status':
                output = getoutput('spigot status')
                p = re.compile(r'processes = ([0-9]*) \(')
                prsnum = re.findall(p,output)[0]
                p = re.compile(r' \((.*?)\)',re.S)
                prsnames = re.findall(p,output)[0].split(', ')
                p = re.compile(r'Total memory usage = (.*)$')
                memory = re.findall(p,output)[0]
                msg = '咱的MC服务器现在有 '
                for prsname in prsnames:
                    msg = msg + prsname + ' '
                msg = msg + '这' + prsnum +'个进程,\n一共占用了' + memory +'内存呢。'
            elif cmd == 'list':
                output = getoutput('spigot command list')
                p = re.compile(r'There are (.*?)[ of a max]', re.S)
                online = re.findall(p,output)[0]
                if online == '0':
                    msg =  '咱看着没有人在线哎\n_(-ω-`_)⌒)_'
                else:
                    msg = '有' + online + '个小伙伴在线!'
                    p = re.compile(r'online: (.*?)[\n>]', re.S)
                    players = re.findall(p,output)[0].split(', ')
                    for player in players:
                        msg = msg + '\n' + player
            elif cmd == 'say':
                saywhat = self.raw_msg['message'][8:]
                if not saywhat:
                    return '汝让咱say what？o(≧口≦)o'
                shellcmd = ['spigot','command','say',saywhat]
                if call(shellcmd) == 0:
                    msg = '咱已经把消息传过去了。'
                else:
                    msg = '٩(ŏ﹏ŏ、)۶竟然失败了,汝是不是让我发送奇怪的话过去!'
        else:
            msg = '汝是不是在mc后面添加了奇怪的参数，咱可只知道 status list 和 say。'
        
        return msg
