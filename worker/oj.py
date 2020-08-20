from zzcore import StdAns

class Ans(StdAns):
    def GETMSG(self):
        msg = 'https://openjudge.sakuya.love/'
        try:
            msg += '?'+ str(self.parms[1])
        except:
            msg += '\n可以在命令里加上题号直接搜索哦.'
        return msg
