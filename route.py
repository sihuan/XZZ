from worker import emmm


def ZZRouter(data):
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
