import json
from zzcore import StdAns

AllowCMD = ['登记','申请出刀','报刀','挂树','查树','进度','查刀','新的一天','血量','初始化']

status = {
    'all_player':{
        '1318000868': {
            'id':'十六夜咲夜',
            '余刀': 3,
            '加时刀': 0,
            # 'SL':1
        },
    },
    'boss_num': 0,
    'boss_hp': 0,
    'dao':{
        'qq':1318000868,
        '类型':'普通刀',
    },
    'tree':[]
}

class Ans(StdAns):
    AllowGroup = [125733077]
    
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'
        
        cmd = self.parms[1]
        if cmd not in AllowCMD:
            return '没有 ' + cmd + ' 这个命令，请检查。'

        
        try:
            nowdata = json.loads(self.DATAGET()['data'])
        except:
            if cmd == '初始化':
                nowdata = {}
            else:
                return '请管理员先初始化,初始化会将进度设置为第一周目第一个Boss,成员数据不会丢失。'

        
        if cmd == '初始化':
            if self.role not in ['owner','admin'] and self.uid != 1318000868:
                return '你没有权限执行初始化。'
            else:
                try:
                    all_player = nowdata['all_player']
                except:
                    all_player = {}

                nowdata = {}
                nowdata['all_player'] = all_player
                nowdata['boss_num'] = 1
                nowdata['boss_hp'] = -1
                nowdata['dao'] = {
                    'qq':0,
                    '类型':'普通刀',
                }
                nowdata['tree'] = []
                self.DATASET({'data':json.dumps(nowdata)})
                return '初始化完成！请使用\n /pcr 血量 xxxx \n 来设置第一周目第一个Boss的总血量。'
        
        if cmd == '登记':
            nickname = self.raw_msg['message'][8:]
            if nickname:
                player = {
                    'id':nickname,
                    '余刀': 3,
                    '加时刀': 0,
                    # 'SL':1
                }

                nowdata['all_player'][str(self.uid)] = player
                self.DATASET({'data':json.dumps(nowdata)})

                return '[CQ:at,qq=' + str(self.uid) + ']' + '游戏id设置为 ' +  nickname

            else:
                return '登记失败，请使用合法的游戏id。'

        if cmd == '血量':
            if self.role not in ['owner','admin'] and self.uid != 1318000868:
                return '你没有权限设置血量。'
            else:
                try:
                    hp = int(self.parms[2])
                except:
                    return '血量应该是整数！'

                nowdata['boss_hp'] = hp
                self.DATASET({'data':json.dumps(nowdata)})
                return '现在' + bossname(int(nowdata['boss_num'])) +'的血量被设置为' + str(hp)

        if cmd == '新的一天':
            if self.role not in ['owner','admin'] and self.uid != 1318000868:
                return '你没有权限新的一天。'
            else:
                for value in nowdata['all_player'].values():
                    value['余刀'] = 3
                    value['加时刀']  = 0
                    # value['SL'] == 1
                nowdata['tree'] = []
                self.DATASET({'data':json.dumps(nowdata)})
            return '新的一天已经开始，大家各有3刀剩余了。'

        
        if cmd == '进度':
            return bossname(int(nowdata['boss_num'])) + '\n剩余血量：' + str(nowdata['boss_hp'])

        if cmd == '申请出刀':
            try:
                nowplayer = nowdata['all_player'][str(self.uid)]
            except:
                return '您未登记。'
            daoqq = nowdata['dao']['qq']
            if daoqq != 0 and daoqq not in nowdata['tree']:
                return nowdata['all_player'][str(daoqq)]['id'] + '正在出刀，请等待他结算或挂树.'
            elif nowplayer['余刀'] + nowplayer['加时刀'] < 1:
                return '您已无刀可出。'
            else:
                nowdata['dao']['qq'] = self.uid
                if nowplayer['加时刀'] > 0:
                    nowdata['dao']['类型'] = '加时刀'
                else:
                    nowdata['dao']['类型'] = '普通刀'

                self.DATASET({'data':json.dumps(nowdata)})
                return nowplayer['id'] + '出' + nowdata['dao']['类型'] + '讨伐' + bossname(int(nowdata['boss_num'])) + '\n剩余血量：' + str(nowdata['boss_hp'])

        
        if cmd == '报刀':
            try:
                nowplayer = nowdata['all_player'][str(self.uid)]
            except:
                return '您未登记。'
            
            try:
                jianhp = int(self.parms[2])
            except:
                return '打掉的血量应该是整数！'

            newhp = nowdata['boss_hp'] - jianhp
            # BOSS 没死
            if newhp > 0:
                nowdata['boss_hp'] = newhp
                nowdata['dao']['qq'] = 0
                if nowdata['dao']['类型'] == '加时刀':
                    nowplayer['加时刀'] = 0
                else:
                    nowplayer['余刀'] = nowplayer['余刀'] - 1

                nowdata['all_player'][str(self.uid)] = nowplayer
                self.DATASET({'data':json.dumps(nowdata)})
                
                return nowplayer['id'] + '打了' + bossname(int(nowdata['boss_num'])) + str(jianhp) + '\n剩余血量：' + str(nowdata['boss_hp'])
            #BOSS 死了
            else:
                nowdata['boss_hp'] = 0
                nowdata['boss_num'] = nowdata['boss_num'] + 1
                nowdata['dao']['qq'] = 0
                nowdata['tree'] = []
                if nowdata['dao']['类型'] == '加时刀':
                    nowplayer['加时刀'] = 0
                else:
                    nowplayer['余刀'] = nowplayer['余刀'] - 1
                    nowplayer['加时刀'] = 1
                
                nowdata['all_player'][str(self.uid)] = nowplayer
                self.DATASET({'data':json.dumps(nowdata)})

                return nowplayer['id'] + '击杀了' + bossname(int(nowdata['boss_num'])-1) + '\n现在进入' + bossname(int(nowdata['boss_num'])) + '\n挂树的同学已经全部下树\n请使用\n /pcr 血量 xxxx \n 来设置新Boss的总血量'

            
        if cmd == '挂树':
            try:
                nowplayer = nowdata['all_player'][str(self.uid)]
            except:
                return '您未登记。'

            if nowdata['dao']['qq'] != self.uid:
                return '您未出刀，挂个毛树'

            # elif nowplayer['SL'] == 1:
            elif self.uid in nowdata['tree']:
                return '您已经在树上了。'
            
            else:
                nowdata['dao']['qq'] = 0
                # print(nowdata['tree'])
                # print(type(nowdata['tree']))
                nowdata['tree'].append(self.uid)
                # print(nowdata['tree'])
                # print(type(nowdata['tree']))
                self.DATASET({'data':json.dumps(nowdata)})
                return '已挂树'

        if cmd == '查树':
            on_tree_players = ''
            for p in nowdata['tree']:
                on_tree_players = on_tree_players + nowdata['all_player'][str(p)]['id'] + '\n'
            return '树上的有\n' + on_tree_players

        if cmd == '查刀':
            alldao = ''
            for value in nowdata['all_player'].values():
                alldao = alldao + value['id'] + ' ' + '🔪'*value['余刀'] + '🍴'*value['加时刀'] + '\n'
            return alldao




def bossname(num):
    zm = int(num/5)+1
    z = num%5

    if z == 0:
        z = 5
        zm = zm - 1

    return '第'+ str(zm) + '周目第' + str(z) + 'Boss'

