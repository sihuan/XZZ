import requests
import time
from zzcore import StdAns


class Ans(StdAns):
    # AllowGroup = [874769998,596678277,7343311]

    def GETMSG(self):
        if len(self.parms) < 2:
            msg = '请输入包名 如：/pkg linux testing 查询 Testing 的 linux 软件'
            return msg
        elif self.parms[1] == 'help':
            msg = '使用 /pkg 包名 查询Core, Extra, Testing, Multilib, Multilib-Testing, ' \
                  'Community, Community-Testing仓库以及AUR的软件 '
            return msg
        else:
            repo = str()
            try:
                if len(self.parms) > 1:
                    repo = '&repo=' + self.parms[2].capitalize()
            except:
                print('repo empty')

            def timeTrans(value):
                temp = time.localtime(int(value))
                timeValue = time.strftime("%Y-%m-%d %H:%M:%S", temp)
                return timeValue[:16]

            req = requests.get(
                url='https://archlinux.org/packages/search/json/?name=' + self.parms[1] + repo).json()
            if not req['results']:
                req = requests.get(
                    url='https://aur.tuna.tsinghua.edu.cn/rpc/?v=5&type=info&arg=' + self.parms[1]).json()
                if req['resultcount'] == 0:
                    req = requests.get(
                        url='https://aur.tuna.tsinghua.edu.cn/rpc/?v=5&type=search&arg=' + self.parms[1]).json()
                # print(req)
                if req['resultcount'] > 0:
                    name = '包名：' + req['results'][0]['Name']
                    # pkgname = req['results'][0]['pkgname']
                    version = '版本：' + req['results'][0]['Version']
                    description = '描述：' + req['results'][0]['Description']
                    maintainer = '维护：' + str(req['results'][0]['Maintainer'])
                    numvotes = '投票：' + str(req['results'][0]['NumVotes'])
                    updatetime = '更新日期：' + timeTrans(req['results'][0]['LastModified'])
                    outofdate = req['results'][0]['OutOfDate']
                    if outofdate is not None:
                        outofdate=timeTrans(outofdate)
                        updatetime = updatetime + '\n过期日期：' + outofdate
                    url = req['results'][0]['URL']
                    if url is None:
                        url = '链接：None'
                    else:
                        url = '链接：' + url
                    msg = '仓库：AUR\n' + name + '\n' + version + '\n' + description + '\n' + maintainer \
                          + '\n' + numvotes + '\n' + updatetime + '\n' + url
                    return msg
            else:
                repo = req['results'][0]['repo']
                pkgname = req['results'][0]['pkgname']
                pkgver = req['results'][0]['pkgver'] + '\n'
                pkgdesc = req['results'][0]['pkgdesc']
                url = req['results'][0]['url']
                updatetime = req['results'][0]['last_update']
                updatetime = updatetime.replace('T', ' ')
                updatetime = updatetime[0:16] + '\n'
                # return repo,pkgname,pkgver,pkgdesc,url
                # print('仓库：' + repo + '\n包名：' + pkgname + '\n版本：' + pkgver + '\n描述：' + pkgdesc + '\n上游：' + url + '\n')
                msg = '仓库：' + repo + '\n包名：' + pkgname + '\n版本：' + pkgver + '描述：' + pkgdesc + '\n更新日期：' \
                      + updatetime + '上游：' + url
                return msg
