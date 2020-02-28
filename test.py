from worker import emmm

print("开始测试咯，在 '>' 后面输入n你的消息，不用加 '/'")
inp = input('>')
while(inp):
    parms = str.split(inp)
    worker = parms[0]

    try:
        package = __import__(name='worker.'+ worker, fromlist=worker)
        Ans_ = getattr(package,'Ans')
    except:
        Ans_ = emmm.Ans
    
    try:
        Ans = Ans_(parms,uid=0,gid=0,role='owner',raw_msg={'message':'/' + inp})
        Message = Ans.GETMSG()
    except Exception as e:
        Message = '   Error:\n'+e
    print(Message)
    inp = input('>')