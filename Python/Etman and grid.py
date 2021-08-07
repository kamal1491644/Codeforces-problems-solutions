n,m=map(int,input().split())
counterTrue=0
for i in range(n):
    row=list(map(int,input().split()))
    ones=row.count(1)
    zeros=row.count(0)
    if ones==zeros:
        counterTrue+=1
    elif ones>zeros:
        for i in range(len(row)):
            if row[i]==1:
                row[i]=0
                break
        ones=row.count(1)
        zeros=row.count(0)
        if ones==zeros:
            counterTrue+=1
    elif zeros>ones:
        for i in range(len(row)):
            if row[i]==0:
                row[i]=1
                break
        ones=row.count(1)
        zeros=row.count(0)
        if ones==zeros:
            counterTrue+=1
if counterTrue==n:
    print('YES')
else:
    print('NO')
