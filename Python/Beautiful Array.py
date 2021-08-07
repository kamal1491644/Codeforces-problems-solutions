n=int(input())

numbers=list(map(int,input().split()))
flag=False

for i in range(len(numbers)-2):
    temp=numbers[i]*numbers[i+1]
    if temp not in numbers:
        flag=False
        break
    else:
        flag=True
    

if flag:
    print('YES')
else:
    print('NO')
        
