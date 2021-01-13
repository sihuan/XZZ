import requests
import json

url = 'http://127.0.0.1:5580/'
headers = {'Content-Type': 'application/json'}

gids = [743539576, 959613860, 1107535671]

data = {
    "anonymous": "None",
    "font": 1501544,
    "group_id": 959613860,
    "message": "/zhaoan",
    "message_id": 2071,
    "message_type": "group",
    "post_type": "message",
    "raw_message": "/zhaoan",
    "self_id": 161795000,
    "sender": {
        "age": 18,
        "area": "济宁",
        "card": "",
        "level": "活跃",
        "nickname": "SiHuan",
        "role": "owner",
        "sex": "unknown",
        "title": "",
        "user_id": 1318000000
    },
    "sub_type": "normal",
    "time": 1582805370,
    "user_id": 1318000000
}
for gid in gids:
    data['group_id'] = gid
    requests.post(url=url, headers=headers, data=json.dumps(data))