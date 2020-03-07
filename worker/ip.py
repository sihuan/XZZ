from zzcore import StdAns
import requests

class Ans(StdAns):
    def GETMSG(self):
        try:
            ip = self.parms[1]
        except:
            ip = ''
        url = 'https://api.ip.sb/geoip/'
        if ip == '' or ip == 'help':
            ret = '您可以使用 "/ip ip地址" 进行查找'
        else:
            res = requests.get(url + ip)
            rsc = res.status_code
            rem = res.json()
            if rsc == 400:
                ret = '不是正确的ip地址，您可以使用 "/ip ip地址" 进行查找'
            else:
                rlt = []
                try:
                    rlt.append('IP： ' + ip)
                    rlt.append('国家/地区： ' + rem['country'])
                    rlt.append('ISP： ' + rem['isp'])
                    rlt.append('ASN： ' + str(rem['asn']))
                    rlt.append('ASN组织： ' + rem['asn_organization'])
                    rlt[1] += ', ' + rem['region']
                    rlt[1] += ', ' + rem['city']
                except:
                    pass
                ret = '\n'.join(rlt)
        return ret
