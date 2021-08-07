n=int(input())
 
numbers=list(map(int,input().split()))
salma=0
for i in numbers:
    if i%3==0:
        salma+=i
print(salma)
