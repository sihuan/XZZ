from zzcore import StdAns
import requests

class Ans(StdAns):
    def GETMSG(self):
        url = 'https://v1.hitokoto.cn/?encode=text&'
        cmdlst = {'动画': 'a', '漫画': 'b', '游戏': 'c', '文学': 'd', '原创': 'e', '来自网络': 'f',
                  '其他': 'g', '影视': 'h', '诗词': 'i', '网易云': 'j', '哲学': 'k', '抖机灵': 'l'}
        try:
            cmd = self.parms[1]
        except :
            cmd = ''
        if cmd == '帮助':
            msg = '您可以使用以下参数：\n   动画，漫画，游戏，文学，原创，来自网络，其他，影视，诗词，网易云，哲学，抖机灵'
        elif cmd == '':
            msg = requests.get(url).text
        elif cmd in cmdlst:
            msg = requests.get(url+cmdlst[cmd]).text
        else:
            msg = '我不知道 ' + cmd + ' 这个参数，你可以使用"/yiyan 帮助"来获取帮助'
        return msg