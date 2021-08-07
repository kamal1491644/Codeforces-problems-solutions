n,k=map(int,input().split())
numbers=list(map(int,input().split()))

counter=0



for i in numbers:
    if i==0:
        continue
    if i>=numbers[k-1]:
        counter+=1
    
print(counter)
