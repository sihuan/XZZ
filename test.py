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
        package = __import__(name='worker.'+ worker, fromlist=worker)
        Ans_ = getattr(package,'Ans')
    except Exception as e:
        # de(e)
        Ans_ = emmm.Ans
    # de(Ans_)
    try:
        Ans = Ans_(parms,uid=0,gid=0,role='owner',raw_msg={'message':'/' + inp})
        Message = Ans.GETMSG()
    except Exception as e:
        Message = '   Error:\n'+str(e)
    print(Message)
    inp = input('>')