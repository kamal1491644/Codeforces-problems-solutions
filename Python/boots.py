n=int(input())
counter=0
left=list(map(int,input().split()))
right=list(map(int,input().split()))

for i in range(len(left)):
    for j in range(len(right)):
        if left[i]==right[j]:
            right[j] = -1
            break
            

for i in right:
    if i!=-1:
        counter+=1
        
            
        
print(counter)
