from zzcore import StdAns
import requests


class Ans(StdAns):
    def GETMSG(self):
        try:
            picurl, status = Kemomimi()
        except:
            print()
        msg = ''
        if status == 200:
            # 显示图标
            # msg += f'[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' \
            #        f'<msg serviceID="1">' \
            #        f'<item><title>来喽！！</title></item>' \
            #        f'<source name="K!" icon="{picurl}" action="web" appid="-1" />' \
            #        f'</msg>' \
            #        f']'
            msg = f'[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' \
                  f'<msg serviceID="1"\n' \
                  f'action="web" url="\n' \
                  f'https://brx86.gitee.io/kemomimi/202.jpg">\n' \
                  f'<item><title>ケモミミちゃん：</title><summary>Kemomimi酱来了～</summary><picture cover="https://brx86.gitee.io/kemomimi/202.jpg"/></item>\n' \
                  f'</msg> ' \
                  f']'
            # 显示卡片图片
            # msg += f'[CQ:cardimage,file={picurl},maxheight=200]'
        else:
            msg += '图库丢了哦,不是咱的问题呀！'
        return msg


def Kemomimi():
    url = "http://api.aya1.xyz:6/random0.php"
    # 获取重定向后的地址
    imgurl = requests.get(url).url
    status = requests.get(url).status_code
    # print(imgurl)\
    return imgurl, status
