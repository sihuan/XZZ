import requests

from zzcore import StdAns


class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            msg = '请输入包名 如：/mner yjun'
            return msg
        else:
            msg = ''
            req = requests.get(
                url='https://aur.archlinux.org/rpc/?v=5&type=search&by=maintainer&arg=' + self.parms[1]).json()
            count = req['resultcount']
            if count != 0:
                msg += '工具人 ' + self.parms[1] + ' 打包了' + str(count) + '个软件\n'
                soft=''
                if count < 5:
                    # soft = list()
                    for i in range(count):
                        soft= req['results'][i]['Name']
                else:
                    for i in range(5):
                        soft+=req['results'][i]['Name']+'\n'
                    soft+='....'
                return msg+soft
