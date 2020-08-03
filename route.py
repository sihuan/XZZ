from worker import emmm
from zzcore import DM
from config import DAAPI

import requests


def ZZRouter(data):

    if data['post_type'] != 'message' or data['message_type'] != 'group' or data['message'][0] != '/':
        if data['user_id'] == 1318000868 :
            return
        if len(data['raw_message']) == 54 and data['raw_message'][:15] == '[CQ:image,file=':   # use re
            url = data['message'][58:][:-1]
            r = requests.post(
                "https://api.deepai.org/api/image-similarity",
                data={
                    'image1': 'https://img.vim-cn.com/fa/4a7f3996e3601e98bd3c1b245fcb88e05f32ec.jpg',
                    'image2': url,
                },
                headers={'api-key': DAAPI}
            )
            if r.json()['output']['distance'] < 10:
                DM(data['message_id'])
        return

    uid = data['user_id']
    gid = data['group_id']
    role = data['sender']['role']
    parms = str.split(data['message'][1:])
    print(uid, gid, role, parms)
    if parms == []:
        parms[0] = 'help'
    worker = parms[0]

    try:
        package = __import__(name='worker.' + worker, fromlist=worker)
        Ans_ = getattr(package, 'Ans')
    except:
        Ans_ = emmm.Ans

    Ans = Ans_(parms, uid, gid, role, data)
    Message = Ans.CheckPermission()
    if Message == 0:
        Message = Ans.GETMSG()
    elif Message == -1:
        return
    Ans.sendmsg(Message)
