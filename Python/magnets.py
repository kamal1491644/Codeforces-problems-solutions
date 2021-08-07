l=[]
first=[]
second=[]
third=[]
for i in range(3):
    x,y=map(int,input().split())
    l.append(x)
    l.append(y)
first=l[:2]
second=l[2:4]
third=l[4:]

if first[-1]!=second[0] and second[-1]!=third[0]:
    print('YES')
elif first[-1]!=third[0] and third[-1]!=second[0]:
    print('YES')
elif second[-1]!=first[0] and first[-1]!=third[0]:
    print('YES')
elif second[-1]!=third[0] and third[-1]!=first[0]:
    print('YES')
elif third[-1]!=first[0] and first[-1]!=second[0]:
    print('YES')
elif third[-1]!=second[0] and second[-1]!=first[0]:
    print('YES')
else:
    print('NO')
    
