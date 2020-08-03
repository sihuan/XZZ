from worker import emmm
from zzcore import DM


def ZZRouter(data):

    if '[CQ:image,file=a854b2390d427b02fc26cae49d508a75.image]' in data['raw_message'] and data['user_id'] != 1318000868:
        DM(data['message_id'])


    if data['post_type'] != 'message' or data['message_type'] != 'group' or data['message'][0] != '/':
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
