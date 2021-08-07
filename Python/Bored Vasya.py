n,m=map(int,input().split())
if n==0 or m==0:
    print("0")


else:
    numbers=list(map(int,input().split()))
    ind=[]
    for i in range(m):
        if numbers[i]%n==0:
            ind.append(i+1)
    ind=sorted(ind,reverse=True)
    print(len(ind))
    for i in ind:
        print(i,end=' ')

    
