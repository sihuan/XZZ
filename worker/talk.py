from zzcore import StdAns

from pydub import AudioSegment
from base64 import b64encode
import requests, io

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            text = "想让我说点什么呢？"
        else:
            text = self.raw_msg['raw_message'][5:]

        try:
           b = tts(text)
           msg = f'[CQ:record,file=base64://{str(b)}]'
        except:
            msg = '什么东西坏掉了,...咱不能说话了!'
        return msg

def tts(text):
    url = "https://tts.baidu.com/text2audio"
    params = {
        'cuid': 'baike',
        'lan': 'zh',
        'ctp': 1,
        'pdt': 301,
        'vol': 5,
        'rate': 32,
        'per': 5118,
        'tex': text,
    }

    r = requests.get(url=url, params=params)
    s = io.BytesIO(r.content)
    r.close()
    # s.seek(0,0)
    song = AudioSegment.from_mp3(s)
    amr = song.export(format="amr", parameters=["-ar", "8000"])
    b = b64encode(amr.read()).decode("utf-8")
    return b