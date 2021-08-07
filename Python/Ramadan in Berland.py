def sumNatural(n): 
    summ = (n*(n+1))//2
    return summ
def suminRange(l, r): 
    return sumNatural(r) - sumNatural(l-1)


n=int(input())

for i in range(n):
    money=0
    l,r=map(int,input().split())
    money=suminRange(l,r)
    print(money)
