from zzcore import StdAns
import sqlite3
from random import randint, choice

n = {'madoka': '鹿目圆', 'homura': '晓美焰', 'sayaka': '美树沙耶香',
     'kyoko': '佐仓杏子', 'mami': '巴麻美', 'qb': '丘比'}


def getQuote(name='random'):
    conn = sqlite3.connect('./data/madoka/quote.db')
    cursor = conn.cursor()
    msg = ''
    try:
        if name == 'random':
            id = randint(1, 49)
            cursor.execute('SELECT text FROM quote WHERE id=?', (id,))
            res = cursor.fetchall()
            msg += res[0][0]

        else:
            cursor.execute('SELECT text FROM quote WHERE name=?', (n[name],))
            res = cursor.fetchall()
            msg += choice(res)[0]
    except Exception:
        pass
    finally:
        cursor.close()
        conn.close()
        return msg


class Ans(StdAns):
    def GETMSG(self):
        try:
            if len(self.parms) == 1:
                return getQuote()
            if len(self.parms) == 2:
                if self.parms[1].lower() in ['madoka', 'homura', 'sayaka', 'kyoko', 'mami', 'qb']:
                    return getQuote(self.parms[1].lower())
                else:
                    return '可以使用"/madoka [人物名字]"的方式调用此命令\n可选人物有: Madoka, Homura, Sayaka, Kyoko, Mami, QB'
            else:
                return '不知道怎么使用的话，就看看"/madoka help"吧'
        except Exception:
            return '出现了奇怪的错误呢'
