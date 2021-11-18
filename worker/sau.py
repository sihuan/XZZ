# -*- encoding: utf-8 -*-
"""
@File    :   sau.py
@Time    :   2021/11/18 20:54:06
@Author  :   Ayatale 
@Version :   1.1
@Contact :   ayatale@qq.com
@Github  :   https://github.com/brx86/
@Desc    :   SauceNAO以图搜图

SauceNAO注册：https://saucenao.com/user.php
api key：https://saucenao.com/user.php?page=search-api
"""

import re, requests
from zzcore import StdAns

SAUCONFIG = {
    "api_key": "paste your api key here",  # 这里是你的api key（必填）
    "numres": 3,  # 返回结果数量,默认为3（必填）
    # "proxies": {"https": "http://127.0.0.1:20171"},  # 设置代理（可选）
}


class SauceNAO:
    APIURL = "https://saucenao.com/search.php"

    def __init__(self, api_key, numres=3, proxies=None):
        self.params = {  # 初始化参数
            "db": 999,
            "api_key": api_key,
            "numres": numres,
            "output_type": 2,
        }
        self.proxies = proxies  # 设置代理

    def search(self, url):
        files, params = None, self.params
        if url[:4] == "http":  # 网络url
            params["url"] = url
        else:  # 本地文件
            files = {"file": open(url, "rb")}
        resp = requests.post(
            self.APIURL,
            files=files,
            params=params,
            proxies=self.proxies,
        )
        return SauceNAOResponse(resp.json())

    def find(self, pic_path):
        text, res = "", self.search(pic_path)
        if res.raw[0].similarity < 60:  # 如果相似度小于60，则不进行搜索
            return "没有找到相似的图片"
        for i in range(self.params["numres"]):
            text += f"""{i+1}.相似度：{res.raw[i].similarity}%
[CQ:image,file={res.raw[i].thumbnail}]
标题：{res.raw[i].title}
作者：{res.raw[i].author}
图片地址：{res.raw[i].url}
"""
        return text.strip()


class SauceNAONorm:
    def __init__(self, data):
        result_header = data["header"]
        result_data = data["data"]
        self.raw: dict = data
        self.similarity: float = float(result_header["similarity"])
        self.thumbnail: str = result_header["thumbnail"]
        self.index_id: int = result_header["index_id"]
        self.index_name: str = result_header["index_name"]
        self.title: str = self._get_title(result_data)
        self.url: str = self._get_url(result_data)
        self.author: str = self._get_author(result_data)
        self.pixiv_id: str = self._get_pixiv_id(result_data)
        self.member_id: str = self._get_member_id(result_data)

    def download_thumbnail(self, filename="thumbnail.png"):  # 缩略图生成
        with requests.get(self.thumbnail, stream=True) as resp:
            with open(filename, "wb") as fd:
                for chunk in resp.iter_content():
                    fd.write(chunk)

    @staticmethod
    def _get_title(data):
        if "title" in data:
            return data["title"]
        elif "eng_name" in data:
            return data["eng_name"]
        elif "material" in data:
            return data["material"]
        elif "source" in data:
            return data["source"]
        elif "created_at" in data:
            return data["created_at"]

    @staticmethod
    def _get_url(data):
        if "ext_urls" in data:
            return data["ext_urls"][0]
        elif "getchu_id" in data:
            return f'http://www.getchu.com/soft.phtml?id={data["getchu_id"]}'
        return ""

    @staticmethod
    def _get_author(data):
        if "author" in data:
            return data["author"]
        elif "author_name" in data:
            return data["author_name"]
        elif "member_name" in data:
            return data["member_name"]
        elif "pawoo_user_username" in data:
            return data["pawoo_user_username"]
        elif "company" in data:
            return data["company"]
        elif "creator" in data:
            if isinstance(data["creator"], list):
                return data["creator"][0]
            return data["creator"]

    @staticmethod
    def _get_pixiv_id(data):
        if "pixiv_id" in data:
            return data["pixiv_id"]
        else:
            return ""

    @staticmethod
    def _get_member_id(data):
        if "member_id" in data:
            return data["member_id"]
        else:
            return ""

    def __repr__(self):
        return f"<NormSauceNAO(title={repr(self.title)}, similarity={self.similarity:.2f})>"


class SauceNAOResponse:
    def __init__(self, resp):
        self.raw: list = []
        resp_header = resp["header"]
        resp_results = resp["results"]
        for i in resp_results:
            self.raw.append(SauceNAONorm(i))
        self.origin: dict = resp
        self.short_remaining: int = resp_header["short_remaining"]  # 每30秒访问额度
        self.long_remaining: int = resp_header["long_remaining"]  # 每天访问额度
        self.user_id: int = resp_header["user_id"]
        self.account_type: int = resp_header["account_type"]
        self.short_limit: str = resp_header["short_limit"]
        self.long_limit: str = resp_header["long_limit"]
        self.status: int = resp_header["status"]
        self.results_requested: int = resp_header["results_requested"]
        self.search_depth: str = resp_header["search_depth"]
        self.minimum_similarity: float = resp_header["minimum_similarity"]
        self.results_returned: int = resp_header["results_returned"]

    def __repr__(self):
        return (
            f"<SauceNAOResponse(count={repr(len(self.raw))}, long_remaining={repr(self.long_remaining)}, "
            f"short_remaining={repr(self.short_remaining)})>"
        )


saucenao = SauceNAO(*SAUCONFIG.values())


# 消息处理类
class Ans(StdAns):
    def GETMSG(self):
        try:
            if len(self.parms) < 2:  # 显示帮助
                # msg = "用法: (注意空格)\n  #sau <图片>\n  #sau <图片链接>\n[CQ:image,file=file:///home/aya/git/SiHuanBot/XZZ/img/help_sau.jpg]"
                msg = "用法: (注意空格)\n  #sau <图片>\n  #sau <图片链接>\n[CQ:image,file=https://gitee.com/brx86/picpool/raw/master/2021/11/18/f791458516c231c4ed7471fa3150d554.png]"
                return msg
            elif self.parms[1][:4] == "http":  # 处理参数并搜索图片
                pic_url = self.parms[1]
                msg = saucenao.find(pic_url)
            elif "[CQ:image,file=" in self.parms[1]:
                args = re.split("[=,\]]", self.parms[1])
                pic_url = self.get_img(args[2])
                msg = saucenao.find(pic_url)
            else:
                msg = "请输入正确参数！"
        except Exception as e:
            print(e)
            msg = "什么东西坏掉了,大概是SauceNAO吧...不可能是咱!"
        return msg
