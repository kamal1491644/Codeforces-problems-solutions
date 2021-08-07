n=int(input())
leftList=[]
rightList=[]
flag=False
FinalString=""
for i in range(n):
    string=input()
    left,right=string.split("|")
    leftList.append(left)
    rightList.append(right)

for i in range(len(leftList)):
    if leftList[i]=="OO":
        leftList[i]="++"
        flag=True
        break

for i in range(len(rightList)):
    if flag:
        break
    if rightList[i]=="OO":
        rightList[i]="++"
        flag=True
        break

for i in range(len(leftList)):
    FinalString+=leftList[i]+"|"+rightList[i]+"\n"

if flag:
    print("YES")
    print(FinalString)

else:
    print("NO")
