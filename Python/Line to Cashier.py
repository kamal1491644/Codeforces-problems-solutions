n=int(input())
people=list(map(int,input().split()))
seconds=[]
for i in range(n):
    num=list(map(int,input().split()))
    mul=[(x*5) for x in num]
    s=sum(mul)
    s+=len(num)*15 
    seconds.append(s)

print(min(seconds))


