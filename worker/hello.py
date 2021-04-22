from zzcore import StdAns
import requests

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '你好啊！我是小智障机器人，你现在可以使用/hello 你想说的话 跟我聊天！'
        question=self.raw_msg['raw_message'][6:]
        # print(question)
        quest=self.raw_msg['sender']['nickname']
        # print(quest)
        key='9c0f6f69aa395bad36a0e797ed44189f'
        url=f'http://api.tianapi.com/txapi/robot/index?key={key}&question={question}&uniqueid={quest}&mode=1'
        reply=requests.get(url).json()
        msg=''
        if(reply['code']==200):
            msg+=reply['newslist'][0]['reply']
        else:
            msg+='不想和你说话！'
        return msg
