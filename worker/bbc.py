from zzcore import StdAns

class Ans(StdAns):
    def GETMSG(self):
        if len(self.parms) < 2:
            return '不加参数是坏文明！'
        try:
            msg = str(bc(self.raw_msg['message'][5:]))
        except Exception as e:
            msg = str(e)
        return msg

def bc(formula):
    formula = pure(formula)
    try:
        return float(formula)
    except ValueError:
        print(subFormula(formula))
        subLift,subRight,flag = subFormula(formula)
        return cal(bc(subLift),bc(subRight),flag)

def pure(formula):
    while(formula[0] == '(' or (formula[0] == '-' and formula[1] == '-')):
        if formula[0] == '(':
            formula = formula[1:]
        else:
            formula = formula[2:]
    while(formula[len(formula) - 1] == ')'):
        formula = formula[:len(formula) - 1]
    
    return formula

def subFormula(formula):
    start = 0
    if formula[0]=='-':
        start = 1
    for index in range(start,len(formula)):
        if formula[index] in ['*','/']:
            lastxx = index
        elif formula[index] == '+':
            return formula[:index],formula[index+1:],'+'
        elif formula[index] == '-' and formula[index-1] not in ['*','/']:
            return formula[:index],formula[index:],'+'
        elif formula[index] == '(':
            return formula[:index-1],formula[index:],formula[index-1]
    return formula[:lastxx],formula[lastxx+1:],formula[lastxx]

def cal(f1,f2,flag):
    do = {
        '+':lambda x,y: x+y,
        '*':lambda x,y: x*y,
        '/':lambda x,y: x/y
    }
    return do[flag](f1,f2)        
