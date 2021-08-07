t=int(input())

for i in range(t):
    even=0
    odd=0
    n=int(input())
    numbers=list(map(int,input().split()))
    for i in numbers:
        if i%2==0:
            even+=1
        else:
            odd+=1
    if even>0 and odd==0:
        print('Even')
    elif odd>0 and even==0:
        print('Odd')
    else:
        print('Mix')


    
