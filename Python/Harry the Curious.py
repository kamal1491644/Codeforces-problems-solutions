l,r,n=map(int,input().split())
factors=[]
while n%2==0:
    factors.append(2)
    n=n//2

divisor=3

while n>=1 and divisor<=n:
    if n%divisor==0:
        factors.append(divisor)
        n=n//divisor
    else:
        divisor+=2
new=[]
for i in factors:
    if i>=l and i<=r:
        new.append(i)

new=set(new)
for i in new:
    print(i,end=' ')
if len(new)==0:
    print(-1)
