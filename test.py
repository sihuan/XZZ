from worker import emmm
debug = True


def de(e):
    if debug:
        print('DEBUG  '+str(e))


print("开始测试咯，在 '>' 后面输入n你的消息，不用加 '/'")
inp = input('>')
while(inp):
    parms = str.split(inp)
    worker = parms[0]

    try:
        package = __import__(name='worker.' + worker, fromlist=worker)
        Ans_ = getattr(package, 'Ans')
    except Exception as e:
        de(e)
        Ans_ = emmm.Ans
    de(Ans_)
    try:
        Ans = Ans_(parms, uid=0, gid=0, role='owner', mid=1001, raw_msg={'message': [
            {
                "data": {
                    "text": f"/{inp}"
                },
                "type": "text"
            }
        ], 'message_id': '1001', 'raw_message': f"/{inp}"})
        Message = Ans.GETMSG()
    except Exception as e:
        Message = '   Error:\n'+str(e)
    print(Message)
    inp = input('>')
