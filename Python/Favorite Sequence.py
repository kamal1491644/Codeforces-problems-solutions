t=int(input())

for i in range(t):
    new=[]
    n=int(input())
    start=0
    end=n-1
    turn=True
    a=list(map(int,input().split()))
    for i in range(n):
        if turn:
            new.append(a[start])
            start+=1
            turn=not turn
        else:
            new.append(a[end])
            end-=1
            turn=not turn
    for i in new:
        print(i,end=' ')
    print()    
