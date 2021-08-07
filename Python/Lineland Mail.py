n=int(input())
cor=list(map(int,input().split()))

print(abs(cor[0]-cor[1]),abs(cor[0]-cor[-1]))

for i in range(1,n-1):
    print(min(abs(cor[i]-cor[i-1]),abs(cor[i]-cor[i+1])),max(abs(cor[i]-cor[0]),abs(cor[i]-cor[-1])))
print(abs(cor[-1]-cor[-2]),abs(cor[-1]-cor[0]))

