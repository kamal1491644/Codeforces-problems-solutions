n,q=map(int,input().split())
numbers=list(map(int,input().split()))

for i in range(q):
    k=int(input())
    start=0
    end=n-1
    temp=-1
    while start<=end:
        mid=(start+end)//2
        if numbers[mid]>k:
            temp=numbers[mid]
            end=mid-1
        else:
            start=mid+1
    print(temp)
