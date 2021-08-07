n,d=map(int,input().split())
l=[d]
s=0
temp=d
flag=False
for i in range(10000000):
    d=d*10+temp
    d%=n
    l.append(d)
 
for i in range(len(l)):
    if l[i]%n==0:
        print(i+1)
        flag=True
        break
 
if flag==False:
    print('-1')
