n=int(input())
counter=0
s=0
for i in range(n):
    entries=list(map(int,input().split()))
    s+=entries[counter]
    counter+=1
print(s)
    
    
