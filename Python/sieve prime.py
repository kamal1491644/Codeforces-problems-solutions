def IsPrime(n):
    prime=[True for i in range(n+1)]
    prime[0]=False
    prime[1]=False
    for i in range(2,n+1):
        if prime[i]:
            for j in range(i+i,n+1,i):
                prime[j]=False
    return prime


l,r=map(int,input().split())
total=0
count=0
p=IsPrime(1000001)
for i in range(l,r+1):
    if p[i]:
        count+=1
        total+=i
print(total,count)
        


