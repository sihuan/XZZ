# by weilinfox~
# 支持四则运算，括号和浮点数，可以省略部分乘号
# 支持语法检查

from zzcore import StdAns

divError = False

#函数段

def reportErr (errorNo, ch):
    if (errorNo == 1):
        return ch + "是什么东西嘛，哼！"
    elif (errorNo == 2):
        return "括号一个一个对不起来了啦~"
    elif (errorNo == 3):
        return ch + "都不会用了嘿！"
    elif (errorNo == 4):
        return "一个数小数点那么多拿来做什么嘞！"
    elif (errorNo == 5):
        return "多出来的小数点很孤单的啦~"
    elif (errorNo == 6):
        return "啊吓死我了，0怎么做除数了啊……"
    else:
        return "啊呀呀这是啥错误啊？问问狸去：" + ch

def supportCh (ch):
    if (ch.isdigit()):
        return True;
    elif (ch == "+" or ch == "-" or ch == "*" or ch == "/" or ch == '.'):
        return True
    elif (ch == '(' or ch == ')'):
        return True
    else:
        return False

def exprCal (ch):
    #处理不带括号的表达式
    global divError
    mulflag = False
    plusflag = False
    for i in range(0, len(ch), 1):
        if (ch[i] == "+" or ch[i] == '-'):
            plusflag = True;
        elif (ch[i] == '*' or ch[i] == '/'):
            mulflag = True;
        if (mulflag and plusflag):
            break;
    if (not mulflag and not plusflag):
        return ch;
    elif (mulflag and plusflag):
        while (1):
            fmul = lmul = 0
            i = 0
            for c in ch:
                if (c == '*' or c == '/'):
                    if (fmul == 0):
                        fmul = i
                    lmul = i
                elif (fmul != 0 and (c == '+' or c == '-')):
                    break
                i += 1
            if (fmul == 0 and lmul == 0):
                break;
            fmul -= 1
            lmul += 1
            while (fmul >= 0 and (ch[fmul].isdigit() or ch[fmul] == '.')):
                fmul -= 1
            while (lmul < len(ch) and (ch[lmul].isdigit() or ch[lmul] == '.')):
                lmul += 1
            fmul += 1
            ch = ch[:fmul] + exprCal(ch[fmul:lmul]) + ch[lmul:]
    #        print(ch)
        return exprCal(ch)
    elif (mulflag):
        while (1):
            fst = lst = 0
            i = 0
            for c in ch:
                if (c == '*' or c == '/'):
                    if (fst == 0):
                        fst = i
                    else:
                        lst = i
                        break
                i += 1
            if (lst == 0):
                num2 = float(ch[fst+1:])
                if (num2 == 0.0):
                    num2 = 1
                    divError = True
                num1 = float(ch[:fst])
                if (ch[fst] == '*'):
                    return str(num1 * num2)
                elif (ch[fst] == '/'):
                    return str(num1 / num2)
            else:
                ch = exprCal(ch[:lst]) + ch[lst:]
    elif (plusflag):
        while (1):
            fst = lst = 0
            i = 0
            for c in ch:
                if (c == '+' or c == '-'):
                    if (fst == 0):
                        fst = i
                    else:
                        lst = i
                        break
                i += 1
            if (lst == 0):
                num2 = float(ch[fst+1:])
                num1 = float(ch[:fst])
                if (ch[fst] == '+'):
                    return str(num1 + num2)
                elif (ch[fst] == '-'):
                    return str(num1 - num2)
            else:
                ch = exprCal(ch[:lst]) + ch[lst:]

def bracketExprCal (ch):
    #处理带括号的表达式
    fbr = lbr = -1
    i = 0
    for c in ch:
        if (c == '('):
            fbr = i
        elif (c == ')'):
            lbr = i
            break
        i += 1
    if (fbr == -1):
        return exprCal(ch)
    else:
        if (lbr+1 >= len(ch)):
    #        print(ch)
            return bracketExprCal(ch[:fbr] + bracketExprCal(ch[fbr+1:lbr]))
        else:
    #        print(ch)
            return bracketExprCal(ch[:fbr] + bracketExprCal(ch[fbr+1:lbr]) + ch[lbr+1:])

def bcMain(com):
    global divError
    #预处理
    #字符替换
    com = com.replace(" ", "")
    com = com.replace("\'", "")
    com = com.replace("\"", "")
    com = com.replace(",", ".")
    com = com.replace("{", "(")
    com = com.replace("}", ")")
    com = com.replace("[", "(")
    com = com.replace("]", ")")
    com = com.replace("x", "*")
    com = com.replace("X", "*")
    
    #省略乘号的支持
    for i in range(1, len(com)-1, 1):
        if (com[i] == '(' and (com[i-1].isdigit() or com[i-1] == '.' or com[i-1] == ')')):
            com = com[:i] + "*" + com[i:]
        elif (com[i] == ')' and (com[i+1].isdigit() or com[i+1] == '.' or com[i+1] == '(')):
            com = com[:i+1] + "*" + com[i+1:]
    
    #print(com)

    #表达式合法性

    #括号合法性
    ncom = ""
    for ch in com:
        if (not supportCh(ch)):
            return reportErr(1, ch)
        elif (ch == "(" or ch == ")"):
            ncom += ch
    nlen = plen = len(ncom)
    while (nlen > 0):
        ncom = ncom.replace("()", "")
        nlen = len(ncom)
        if (nlen == plen):
            return reportErr(2, ncom[0])
        plen = nlen

    #运算符及小数点位置合法性
    ncom = com.replace("(", "")
    ncom = ncom.replace(")", "")
    if (not ncom[0].isdigit() and ncom[0] != '.'):
        return reportErr(3, ncom[0])
    elif (ncom[0] == '.' and (len(ncom) < 2 or not ncom[1].isdigit())):
        return reportErr(5, "")
    elif (not ncom[len(ncom)-1].isdigit() and ncom[len(ncom)-1] != '.'):
        return reportErr(3, ncom[len(ncom)-1])
    elif (ncom[len(ncom)-1] == '.' and (len(ncom) < 2 or not ncom[len(ncom)-2].isdigit())):
        return reportErr(5, "")
    for i in range(1, len(ncom)-1, 1):
        if (ncom[i] == "+" or ncom[i] == "-" or ncom[i] == "*" or ncom[i] == "/"):
            if ((not ncom[i-1].isdigit() and ncom[i-1] != '.') or (not ncom[i+1].isdigit() and ncom[i+1] != '.')):
                return reportErr(3, ncom[i])
        elif (ncom[i] == '.'):
            if (not ncom[i-1].isdigit() and not ncom[i+1].isdigit()):
                return reportErr(5, "")

    #小数点数量合法性
    inNum = False
    dotNum = 0
    for i in range(0, len(com), 1):
        if (com[i].isdigit()):
            inNum = True
        elif (com[i] == "."):
            inNum = True
            dotNum += 1
        else:
            inNum = False
            if (dotNum > 1):
                return reportErr(4, ".")
            dotNum = 0
    if (dotNum > 1):
        return reportErr(4, ".")

    ans = str(bracketExprCal(com))
    if (divError):
        divError = False
        return reportErr(6, "")
    return ans

#代码段
class Ans (StdAns):
    def GETMSG(self):
        ans = "汝以为咱不会算算数的嘛！"
        for s in self.parms:
            if (s == "help"):
                ans = "你喂给我式子我算呀，还不会问狸吧~"
                break
            elif (s != "bc"):
                ans += "\n" + s + " ==> " + bcMain(s)
        return ans

