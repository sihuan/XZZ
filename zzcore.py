import requests, json, redis
from config import APIURL, ALLWORKERS, AUTHORIZATION
from worker import emmm
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

class StdAns():
    AllowGroup = []
    AllowUser = []
    AllowRole = []
    BlockGroup = []
    BlockUser = []
    GroupNotAllow = '汝所在的群组不被允许这样命令咱呢.'
    UserNotAllow = '汝不被允许呢.'
    RoleNotAllow = '汝的角色不被允许哦.'

    def __init__(self,parms,uid,gid,role,mid,raw_msg):
        self.parms = parms
        self.uid = uid
        self.gid = gid
        self.role = role
        self.mid = mid
        self.raw_msg = raw_msg

    def DATAGET(self):
        return r.hgetall(self.parms[0])

    def DATASET(self,data):
        r.hmset(self.parms[0],data)

    def CheckPermission(self):
            if (self.AllowGroup and self.gid not in self.AllowGroup) or self.gid in self.BlockGroup:
                return self.GroupNotAllow
            if (self.AllowUser and self.uid not in self.AllowUser) or self.uid in self.BlockUser:
                return self.UserNotAllow
            if self.AllowRole and self.role not in self.AllowRole:
                return self.RoleNotAllow
            return 0

    def GETMSG(self):
        return self.__module__ +'的话，咱已经知道了，但是还在学习呢！'

    def sendmsg(self,msg):
        url = APIURL + "send_msg"

        data = {
            'access_token' : AUTHORIZATION,
            'message_type' : 'group',
            'group_id' : self.gid,
            'message': msg
            }
        return requests.get(url = url, params=data).json()['data']['message_id']

    def sendfile(self, filepath, filename=""):
        url = APIURL + "upload_group_file"

        name = filename if filename else filepath.split("/")[-1]
        data = {
            "access_token": AUTHORIZATION,
            "group_id": self.gid,
            "file": filepath,
            "name": name,
            }
        return requests.get(url=url, params=data).json()["status"]

    def get_img(self,cache_name):
        url = APIURL + "get_image"

        data = {
            'access_token' : AUTHORIZATION,
            'file': cache_name
            }
        return requests.get(url = url, params=data).json()['data']['url']

    def delmsg(self,msgid):
        url = APIURL + "delete_msg"

        data = {
            'access_token' : AUTHORIZATION,
            'message_id' : msgid,
            }
        requests.get(url = url, params=data)

    def getgroups(self):
        url = APIURL + "get_group_list"
        Headers = {
            'content-type': 'application/json',
            'Authorization':'Bearer ' + AUTHORIZATION
            }

        return requests.get(url = url,headers = Headers).json()['data']

def mysakuya(self, words):
    if self.uid == 1318000868:
        return True
        
    if ('咲' in words and '夜' in words) or ('关' in words and '夜' in words) or ('十' in words and '六' in words and '夜' in words) or ('1' in words and '6' in words and '夜' in words):
        return False
    for sakuya in ['口关夜','十六夜咲夜','十六夜','十六','咲夜', '夜咲', '六夜','Sakuya','sakuya','Izayoi Sakuya','Izayoi','izayoi','izayoi sakuya']:
            if sakuya in words:
                return False

    return True


def DM(msgid):
    url = APIURL + "delete_msg"
    data = {
        'access_token' : AUTHORIZATION,
        'message_id' : msgid,
        }
    requests.get(url = url, params=data)
