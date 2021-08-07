string=input().upper()
flag=True
string=sorted(string)


f=0
m=0

for i in string:
    if i=='F':
        f+=1
    elif i=='M':
        m+=1

if f==1 or f==2 or f==5 or f==8 or f==9:
    flag=False

if f==3 or f==4 or f==6 or f==7 or f==10 or f==0:
    flag=True
if flag:
    print('YES')
else:
    print('NO')
