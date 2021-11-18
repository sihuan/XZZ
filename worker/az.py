# -*- encoding: utf-8 -*-
"""
@File    :   az.py
@Time    :   2021/11/12 13:40:15
@Author  :   Ayatale 
@Version :   1.1
@Contact :   ayatale@qq.com
@Github  :   https://github.com/brx86/
@Desc    :   啊这加密,在“啊”与“这”之间隐写文本内容（其实图片也可以,但只能在QQ解密）
"""

from binascii import a2b_hex
from zzcore import StdAns

all_map = {
    "char_map": ["\u200B", "\u200C", "\u200D", "\u202A"],
    "meow_map": ["喵", "呜", "啊", "~"], # 喵呜啊~
}


def strToMeow(str_text, map_type="char_map"):
    text_map = all_map[map_type]
    encode_text, hex_text = "", str_text.encode().hex()
    for hex_num in hex_text:
        a = int(hex_num, 16) // 4
        b = int(hex_num, 16) % 4
        encode_text += text_map[a]
        encode_text += text_map[b]
    return f"啊{encode_text}这"


def meowToStr(encode_text, map_type="char_map"):
    text_map = all_map[map_type]
    hex_text = ""
    print(encode_text)
    for n in range(len(encode_text) // 2 - 1):
        a = text_map.index(encode_text[2 * n + 1])
        b = text_map.index(encode_text[2 * n + 2])
        hex_text += hex(4 * a + b)[-1]
    return a2b_hex(hex_text).decode()


# 消息处理类
class Ans(StdAns):
    def GETMSG(self):
        # 显示帮助
        # msg= "用法:\n  #az -e <待加密文字>\n  #az -d <待解密文字>\n[CQ:image,file=https://gitee.com/brx86/picpool/raw/master/2021/11/18/d29ef17ebd8a17c2be660427d0d72171.png]"
        msg= "用法:\n  #az -e <待加密文字>\n  #az -d <待解密文字>\n[CQ:image,file=https://gitee.com/brx86/picpool/raw/master/2021/11/18/d29ef17ebd8a17c2be660427d0d72171.png]"
        if len(self.parms) < 3:
            return msg
        # 加密解密
        try:
            if self.parms[1] == "-e":
                msg = strToMeow(self.parms[2])
            elif self.parms[1] == "-d":
                msg = f"解密结果:\n{meowToStr(self.parms[2])}"
            else:
                self.sendmsg("请输入正确参数！")
                return msg
        except Exception as e:
            print(e)
            msg = "加密好像出了问题……但一定不是小白的问题!"
        return msg
