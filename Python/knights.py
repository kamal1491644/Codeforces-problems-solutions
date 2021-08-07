x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
 
 
temp1=abs(x1-x2)
temp2=abs(y1-y2)
 
if temp1==1 and temp2==2:
    print('Yes')
elif temp2==1 and temp1==2:
    print('Yes')
else:
    print('No')
