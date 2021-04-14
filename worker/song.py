from zzcore import StdAns
import requests
import urllib3
urllib3.disable_warnings()

class Ans(StdAns):
    def GETMSG(self):
    	# self.parms[]
        if len(self.parms) < 2:
            return '不加参数是坏文明！'
        url = 'https://music.xmengnet.cn/api'

        try:
        	# print(self.parms[1])
            getid = requests.get(url + '/search?keywords=' + self.raw_msg['raw_message'][5:], verify=False).json()
            id = getid['result']['songs'][0]['id']
            # print(id)
            downurl = requests.get(url + '/song/url?id=' + str(id), verify=False).json()
            # print(downurl)
            down = downurl['data'][0]['url']
            song = getid['result']['songs'][0]['name'] + '-' \
                   + getid['result']['songs'][0]['artists'][0]['name']
            msg = f"[CQ:reply,id={self.raw_msg['message_id']}]"
            return msg+song+'的下载地址为：'+down
            # msg = f'[CQ:music,type=163,id={id}]'
        except Exception as e:
            print(e)
            msg = '什么东西坏掉了,大概是网易云吧...不可能是咱!'
        return msg
