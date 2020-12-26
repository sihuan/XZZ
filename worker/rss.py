from zzcore import StdAns

import feedparser, json, time

allowCMD = ['sub','unsub','list','disable', 'enable']

# allSub = {
#     'https://farseerfc.me/feeds/atom.xml' : {
#         'url' : 'https://farseerfc.me/feeds/atom.xml',
#         'title' : 'Farseerfc的小窩',
#         'lastUpdated' : 'Sat, 12 Dec 2020 22:55:52 +0800',
#     }
# }

class Ans(StdAns):

    def push(self,title,posttitle,posturl):
        msg = f'{title}\n{posttitle} {posturl}'
        self.sendmsg(msg)
    
    def GETMSG(self):

        if len(self.parms) < 2:
            return '不加参数是坏文明！'
        
        gid = str(self.gid)
        cmd = self.parms[1]
        if cmd not in allowCMD:
            return f'咱不知道 {cmd} 是什么东西 ●﹏●'

        try:
            nowdata = json.loads(self.DATAGET()[gid])
        except:
            nowdata ={
                'allSub' : {},
                'status' : False,
            }
        
        if cmd == 'sub':
            if len(self.parms) < 3:
                return '汝想订阅什么呢？'
            
            suburl = self.parms[2]
            try:
                d = feedparser.parse(suburl)
                title = d.feed.title
                lastUpdated = d.entries[0].published
            
            except:
                return "咱好像没能成功订阅 (╥_╥)"
            
            newsub = {
                'url': suburl,
                'title': title,
                'lastUpdated' : lastUpdated,
            }

            nowdata['allSub'][suburl] = newsub

            msg = f'《{title}》订阅成功'

        elif cmd == 'unsub':
            if len(self.parms) < 3:
                return '汝想退订什么呢？'

            suburl = self.parms[2]
            if suburl not in nowdata['allSub'].keys():
                return '汝没有订阅过这个！'
            
            unsub = nowdata['allSub'].pop(suburl)
            
            msg = f"《{unsub['title']}》已退订"

        elif cmd == 'list':
            msg = '订阅列表'

            for sub in nowdata['allSub'].values():
                msg += f"\n{sub['title']}  {sub['url']}"

        elif cmd == 'enable':
            nowdata['status'] = True
            self.DATASET({gid:json.dumps(nowdata)})
            self.sendmsg("订阅已启用，咱会每隔五分钟抓取订阅，有新内容就会推送哦")
            while(nowdata['status']):
                nowdata = json.loads(self.DATAGET()[gid])
                for sub in nowdata['allSub'].values():
                    try:
                        d = feedparser.parse(sub['url'])
                    except:
                        self.sendmsg(f"咱抓取不到 《{sub['title']}》!")
                        continue
                    if d.entries[0].published == sub['lastUpdated']:
                        continue
                    
                    newfeedtitle = d.entries[0].title
                    newfeedlink = d.entries[0].link
                    self.push(sub['title'], newfeedtitle, newfeedlink)
                    nowdata['allSub'][sub['url']]['lastUpdated'] = d.entries[0].published
                self.DATASET({gid:json.dumps(nowdata)})
                time.sleep(5000)

            return '订阅已经真的停了！'

        elif cmd == 'disable':
            nowdata['status'] = False
            msg = '咱不会再推送了！'

        self.DATASET({gid:json.dumps(nowdata)})
        return msg
            