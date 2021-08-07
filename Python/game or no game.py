numbers=list(map(int,input().split()))
n=numbers[0]
a=numbers[1]
b=numbers[2]
c=numbers[3]

if (a+b+c)%n==0:
    print('YES')
else:
    print('NO')
