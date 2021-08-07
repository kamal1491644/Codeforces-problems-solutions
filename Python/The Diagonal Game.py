n=int(input())
l=[]
s1=0
s2=0
for i in range(n):
    l.append(list(map(int,input().split())))

s1=sum(l[i][i] for i in range(n))
s2=sum(l[i][n-i-1] for i in range(n))

print(s1,s2)
    
