
n=int(input())
students=list(map(int,input().split()))

programming=[]
maths=[]
pe=[]

for i in range(len(students)):
    if students[i]==1:
        programming.append(i+1)
    elif students[i]==2:
        maths.append(i+1)
    elif students[i]==3:
        pe.append(i+1)
   
ans=min(len(programming),len(maths),len(pe))
print(ans)
for i in range(ans):
    print(programming[i],maths[i],pe[i])
    

    





