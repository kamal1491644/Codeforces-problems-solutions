n,m=map(int,input().split())
flag=False
for i in range(int((n+1)/2),n+1):
    if i%m==0:
        print(i)
        flag=True
        break

if flag==False:
    print("-1")
