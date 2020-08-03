from zzcore import StdAns

from datetime import timedelta, datetime
import requests
import random


class Ans(StdAns):

    def GETMSG(self):

        if len(self.parms) < 2:
            try:
                illust = rsearch('')
            except Exception as e:
                # print(e)
                illust = {}

        elif self.parms[1] == 'help':
            msg = '/pixiv 获取昨日随机日榜\n/pixiv [关键词] 使用关键词搜索，不可以有空格哦\n/pixiv id [插画id] 获取指定插画，不可以是漫画（\n/pixiv help 展示本 help'
            return msg

        elif self.parms[1] == 'id' :
            try:
                id = int(self.parms[2])
                illust = getbyid(id)
            except Exception as e:
                illust = {}

        else:
            try:
                illust = rsearch(self.parms[1])
            except Exception as e:
                illust = {}

        if illust == {}:
            msg = '[CQ:reply,id={}] 看起来什么东西出错了 >_<\n稍后再试试吧'.format(str(self.raw_msg['message_id']))
        else :
            imgid = str(illust['id'])

            imgtitle = illust['title']
            imgo = illust['imageUrls'][0]['original'].replace('https://i.pximg.net','https://i.pixiv.cat')
            imgl = illust['imageUrls'][0]['large'].replace('https://i.pximg.net','https://i.pixiv.cat')
            if self.parms[len(self.parms)-1] == 'o':
                imgl = imgo

            msg = '[CQ:reply,id={}]咱帮你🔍找到了这个[CQ:image,file={}]\nid {}\ntitle {}\nurl {}'.format(str(self.raw_msg['message_id']), imgl, imgid, imgtitle, imgo) 
            # .replace('https://i.pixiv.cat', 'https://pximg.sihuan.workers.dev')
            # msg =  picurl.replace('https://i.pixiv.cat', 'https://original.img.cheerfun.dev'
            return msg

def rsearch(s):

    r = random.randint(0, 233)

    if s == '':
        url = 'https://api.pixivic.com/ranks'
        yesterday = datetime.today() + timedelta(-1)

        params = {
            'date' : yesterday.strftime('%Y-%m-%d') ,
            'mode' : 'day',
            'pageSize' : 1,
            'page' : r,
        }

    else:
        url = 'https://api.pixivic.com/illustrations'
        params = {
            'keyword': s,
            'illustType': 'illust',
            'searchType': 'autoTranslate',
            'pageSize': 1,
            'page': r
        }

    for _ in range(3):
        print(r)
        resp = requests.get(url=url, params=params).json()
        if 'data' in resp :
            if resp['data'][0]['type'] != 'illust':
                params['page'] += 1
                continue

            return resp['data'][0]
        params['page'] = int(params['page']/2)

    return {}


def getbyid(id):

    url = 'https://api.imjad.cn/pixiv/v2/'
    params = {
        'type': 'illust',
        'id': id,
    }

    resp = requests.get(url=url, params=params).json()

    if 'illust' in resp and resp['illust']['type'] == 'illust':
        resp['illust']['imageUrls'] = [{
            'large': resp['illust']['image_urls']['large'],
            'original': resp['illust']['meta_single_page']['original_image_url']
        }]
        return resp['illust']

    return {}
