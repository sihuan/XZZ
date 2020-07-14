import requests, json, redis
from config import APIURL, ALLWORKERS, AUTHORIZATION
from worker import emmm
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

class StdAns():
    AllowGroup = []
    AllowUser = []
    AllowRole = []
    GroupNotAllow = '汝所在的群组不被允许这样命令咱呢.'
    UserNotAllow = '汝不被允许呢.'
    RoleNotAllow = '汝的角色不被允许哦.'

    def __init__(self,parms,uid,gid,role,raw_msg):
        self.parms = parms
        self.uid = uid
        self.gid = gid
        self.role = role
        self.raw_msg = raw_msg

    def DATAGET(self):
        return r.hgetall(self.parms[0])

    def DATASET(self,data):
        r.hmset(self.parms[0],data)

    def CheckPermission(self):
            if self.AllowGroup and self.gid not in self.AllowGroup:
                return self.GroupNotAllow
            if self.AllowUser and self.uid not in self.AllowUser:
                return self.UserNotAllow
            if self.AllowRole and self.role not in self.AllowRole:
                return self.RoleNotAllow
            return 0

    def GETMSG(self):
        return self.__module__ +'的话，咱已经知道了，但是还在学习呢！'

    def sendmsg(self,msg):
        url = APIURL + "send_msg"
        Headers = {
            'content-type': 'application/json',
            'Authorization':'Bearer ' + AUTHORIZATION
            }
        
        data = {
            'message_type' : 'group',
            'group_id' : self.gid,
            'message': msg
            }
        return requests.post(url = url, data = json.dumps(data),headers = Headers).json()['data']['message_id']


    def delmsg(self,msgid):
        url = APIURL + "delete_msg"
        Headers = {
            'content-type': 'application/json',
            'Authorization':'Bearer ' + AUTHORIZATION
            }
        data = {
            'message_id' : msgid,
            }
        requests.post(url = url, data = json.dumps(data),headers = Headers)


def mysakuya(self, words):
    if self.uid == 1318000868:
        return True
        
    if ('咲' in words and '夜' in words) or ('关' in words and '夜' in words) or ('十' in words and '六' in words and '夜' in words) or ('1' in words and '6' in words and '夜' in words):
        return False
    for sakuya in ['口关夜','十六夜咲夜','十六夜','十六','咲夜','Sakuya','sakuya','Izayoi Sakuya','Izayoi','izayoi','izayoi sakuya']:
            if sakuya in words:
                return False