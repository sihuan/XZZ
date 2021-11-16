import re,  requests
from zzcore import StdAns
from PicImageSearch import SauceNAO

_REQUESTS_KWARGS = {
    "proxies": {
        "https": "http://127.0.0.1:20171",
    }
}
saucenao = SauceNAO(
    api_key="3fc2c3455b16c966777738c07409253289d7043a", **_REQUESTS_KWARGS
)


def find(pic_path):
    res = saucenao.search(pic_path)
    text = ""
    for i in range(3):
        text += f"""{i+1}.相似度：{res.raw[i].similarity}%
[CQ:image,file={res.raw[i].thumbnail}]
标题：{res.raw[i].title}
作者：{res.raw[i].author}
图片地址：{res.raw[i].url}
"""
    return text


def get_img(cache_name):
    url = "http://127.0.0.1:5700/" + "get_image"
    params = {"access_token": "ayatale", "file": cache_name}
    return requests.get(url=url, params=params).json()


# 消息处理类
class Ans(StdAns):
    def GETMSG(self):
        # 显示帮助
        if len(self.parms) < 2:
            return "用法:\n  #sau <图片>\n  #sau <图片链接>\n[CQ:image,file=http://127.0.0.1:2000/git/SiHuanBot/XZZ/img/help_sau.jpg]"
        # 处理参数
        if self.parms[1][:4] == "http":
            pic_path = self.parms[1]
        else:
            args = re.split("[=,\]]", self.parms[1])
            pic_path = self.get_img(args[2])
        msg = find(pic_path).strip()
        pic_path = ""
        return msg
