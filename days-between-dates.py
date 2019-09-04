def isleapyear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def daysinmonth(m,y):
    if(m<8):
        if(m==2 and isleapyear(y)):
            return 29
        if(m==2 and not isleapyear(y)):
            return 28
        if(m%2!=0):
            return 31
        else:
            return 30
    else:
        if(m%2==0):
            return 31
        else:
            return 30
d1,m1,y1 = map(int,input("Enter the first date, month, year").split())
d2,m2,y2 = map(int,input("Enter the second date, month, year").split())
d = d1
m = m1
y = y1
days=0
while(True):
    days+=1
    if(y==y2 and m==m2 and d==d2):
        break
    if(m==13):
        m=1
        y+=1
    if(d==daysinmonth(m,y)):
        days+=1
        d=1
        m+=1
    d+=1
print(days)
