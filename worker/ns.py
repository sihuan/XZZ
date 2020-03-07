from zzcore import StdAns
import subprocess

class Ans(StdAns):
    def GETMSG(self):
        try:
            if (len(self.parms) < 2):
                return "不加参数是坏文明！"
            com = ""
            for s in self.parms:
                com += s + ' '
            com = 'nslookup \"' + com[3:len(com)-1] + '\"'
            s = subprocess.run(com, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, timeout = 5)
            return bytes.decode(s.stdout)
        except subprocess.TimeoutExpired:
            return "请求超时！"
        except:
            return "未知错误！"
