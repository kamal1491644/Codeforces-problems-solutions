strength_dragons=list(map(int,input().split()))
strength=strength_dragons[0]
dragons=strength_dragons[1]
flag=True
temp=[]
for i in range(dragons):
    x,y=map(int,input().split())
    temp.append([x,y])

temp=sorted(temp)

for i in range(dragons):
    if strength>temp[i][0]:
        strength+=temp[i][1]
    else:
        flag=False
        break

if flag:
    print("YES")
else:
    print("NO")
