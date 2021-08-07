n=int(input())
s=0
for i in range(n):
    x,p,d=map(int,input().split())
    offer=p-d
    price=x*offer
    s+=price
print(s)
    
