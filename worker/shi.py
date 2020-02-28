from zzcore import StdAns
import requests


class Ans(StdAns):
    def GETMSG(self):
        apilist = {
            '抒情': {
                '全部': 'https://v1.jinrishici.com/shuqing',
                '爱情': 'https://v1.jinrishici.com/shuqing/aiqing',
                '友情': 'https://v1.jinrishici.com/shuqing/youqing',
                '离别': 'https://v1.jinrishici.com/shuqing/libie',
                '思念': 'https://v1.jinrishici.com/shuqing/sinian',
                '思乡': 'https://v1.jinrishici.com/shuqing/sixiang',
                '伤感': 'https://v1.jinrishici.com/shuqing/shanggan',
                '孤独': 'https://v1.jinrishici.com/shuqing/gudu',
                '闺怨': 'https://v1.jinrishici.com/shuqing/guiyuan',
                '悼亡': 'https://v1.jinrishici.com/shuqing/daowang',
                '怀古': 'https://v1.jinrishici.com/shuqing/huaigu',
                '爱国': 'https://v1.jinrishici.com/shuqing/aiguo',
                '感恩': 'https://v1.jinrishici.com/shuqing/ganen',
            },
            '四季': {
                '全部': 'https://v1.jinrishici.com/siji',
                '春天': 'https://v1.jinrishici.com/siji/chuntian',
                '夏天': 'https://v1.jinrishici.com/siji/xiatian',
                '秋天': 'https://v1.jinrishici.com/siji/qiutian',
                '冬天': 'https://v1.jinrishici.com/siji/dongtian',
            },
            '山水': {
                '全部': 'https://v1.jinrishici.com/shanshui',
                '庐山': 'https://v1.jinrishici.com/shanshui/lushan',
                '泰山': 'https://v1.jinrishici.com/shanshui/taishan',
                '江河': 'https://v1.jinrishici.com/shanshui/jianghe',
                '长江': 'https://v1.jinrishici.com/shanshui/changjiang',
                '黄河': 'https://v1.jinrishici.com/shanshui/huanghe',
                '西湖': 'https://v1.jinrishici.com/shanshui/xihu',
                '瀑布': 'https://v1.jinrishici.com/shanshui/pubu', },
            '天气': {
                '全部': 'https://v1.jinrishici.com/tianqi',
                '写风': 'https://v1.jinrishici.com/tianqi/xiefeng',
                '写云': 'https://v1.jinrishici.com/tianqi/xieyun',
                '写雨': 'https://v1.jinrishici.com/tianqi/xieyu',
                '写雪': 'https://v1.jinrishici.com/tianqi/xiexue',
                '彩虹': 'https://v1.jinrishici.com/tianqi/caihong',
                '太阳': 'https://v1.jinrishici.com/tianqi/taiyang',
                '月亮': 'https://v1.jinrishici.com/tianqi/yueliang',
                '星星': 'https://v1.jinrishici.com/tianqi/xingxing', },
            '人物': {
                '全部': 'https://v1.jinrishici.com/renwu',
                '女子': 'https://v1.jinrishici.com/renwu/nvzi',
                '父亲': 'https://v1.jinrishici.com/renwu/fuqin',
                '母亲': 'https://v1.jinrishici.com/renwu/muqin',
                '老师': 'https://v1.jinrishici.com/renwu/laoshi',
                '儿童': 'https://v1.jinrishici.com/renwu/ertong', },
            '人生': {
                '全部': 'https://v1.jinrishici.com/rensheng',
                '励志': 'https://v1.jinrishici.com/rensheng/lizhi',
                '哲理': 'https://v1.jinrishici.com/rensheng/zheli',
                '青春': 'https://v1.jinrishici.com/rensheng/qingchun',
                '时光': 'https://v1.jinrishici.com/rensheng/shiguang',
                '梦想': 'https://v1.jinrishici.com/rensheng/mengxiang',
                '读书': 'https://v1.jinrishici.com/rensheng/dushu',
                '战争': 'https://v1.jinrishici.com/rensheng/zhanzheng',
            },
            '生活': {
                '全部': 'https://v1.jinrishici.com/shenghuo',
                '乡村': 'https://v1.jinrishici.com/shenghuo/xiangcun',
                '田园': 'https://v1.jinrishici.com/shenghuo/tianyuan',
                '边塞': 'https://v1.jinrishici.com/shenghuo/biansai',
                '写桥': 'https://v1.jinrishici.com/shenghuo/xieqiao',
            },
            '节日': {
                '全部': 'https://v1.jinrishici.com/jieri',
                '春节': 'https://v1.jinrishici.com/jieri/chunjie',
                '元宵节': 'https://v1.jinrishici.com/jieri/yuanxiaojie',
                '寒食节': 'https://v1.jinrishici.com/jieri/hanshijie',
                '清明节': 'https://v1.jinrishici.com/jieri/qingmingjie',
                '端午节': 'https://v1.jinrishici.com/jieri/duanwujie',
                '七夕节': 'https://v1.jinrishici.com/jieri/qixijie',
                '中秋节': 'https://v1.jinrishici.com/jieri/zhongqiujie',
                '重阳节': 'https://v1.jinrishici.com/jieri/chongyangjie',
            },
            '动物': {
                '全部': 'https://v1.jinrishici.com/dongwu',
                '写鸟': 'https://v1.jinrishici.com/dongwu/xieniao',
                '写马': 'https://v1.jinrishici.com/dongwu/xiema',
                '写猫': 'https://v1.jinrishici.com/dongwu/xiemao',
            },
            '植物': {
                '全部': 'https://v1.jinrishici.com/zhiwu',
                '梅花': 'https://v1.jinrishici.com/zhiwu/meihua',
                '梨花': 'https://v1.jinrishici.com/zhiwu/lihua',
                '桃花': 'https://v1.jinrishici.com/zhiwu/taohua',
                '荷花': 'https://v1.jinrishici.com/zhiwu/hehua',
                '菊花': 'https://v1.jinrishici.com/zhiwu/juhua',
                '柳树': 'https://v1.jinrishici.com/zhiwu/liushu',
                '叶子': 'https://v1.jinrishici.com/zhiwu/yezi',
                '竹子': 'https://v1.jinrishici.com/zhiwu/zhuzi',
            },
            '食物': {
                '全部': 'https://v1.jinrishici.com/shiwu',
                '写酒': 'https://v1.jinrishici.com/shiwu/xiejiu',
                '写茶': 'https://v1.jinrishici.com/shiwu/xiecha',
                '荔枝': 'https://v1.jinrishici.com/shiwu/lizhi'
            }
        }
        if len(self.parms) == 1:
            resp = requests.get('https://v1.jinrishici.com/all').json()
            msg = resp['author']+'在《'+resp['origin']+'》中的:\n    ' + resp['content']
        elif len(self.parms) == 2:
            if  self.parms[1] == 'help':
                onelist = apilist.keys()
                msg = '咱知道一级分类有：\n  '
                for it in onelist:
                    msg = msg + ' ' + it
                msg = msg + '\n汝可以用 shi help 一级分类名让咱列出二级分类'
            else:
                try:
                    url = apilist[self.parms[1]]['全部']
                    msg = ''
                except :
                    url = 'https://v1.jinrishici.com/all'
                    msg = '没有'+self.parms[1]+'这个分类，咱就随便找了一句~\n'
                resp = requests.get(url).json()
                msg = msg + resp['author']+'在《'+resp['origin']+'》中的:\n    ' + resp['content']
        
        elif len(self.parms) == 3:
            if  self.parms[1] == 'help':
                try:
                    twolist = list(apilist[self.parms[2]].keys())[1:]
                    msg = self.parms[2] + '的二级分类有：\n  '
                    for it in twolist:
                        msg = msg + ' ' + it
                except:
                    msg = '根本没有' + self.parms[2] +'这个分类好伐？'
            else:
                msg = ''
                try:
                    url = apilist[self.parms[1]][self.parms[2]]
                except:
                    url = 'https://v1.jinrishici.com/all'
                    msg = '汝给咱的分类咱不懂，敷衍一下吧：\n'
                resp = requests.get(url).json()
                msg = msg + resp['author']+'在《'+resp['origin']+'》中的:\n    ' + resp['content']
        else:
            msg = '咱收到了shi命令，但是格式咱理解不了呢。\n请使用 "shi [一级分类] [二级分类]" 这种格式。\n具体分类使用 "shi help" 查看。'
        return msg
