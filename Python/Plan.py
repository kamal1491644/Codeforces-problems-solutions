n,q=map(int,input().split())
numbers=list(map(int,input().split()))
d={}
for i,j in enumerate(numbers):
    d[j]=i+1
numbers=sorted(numbers)
for i in range(q):
    start=0
    end=n-1
    found=False    
    x=int(input())
    while start<=end:
        mid=(start+end)//2
        if numbers[mid]==x:
            print('Yes',d[x])
            found=True
            break
        elif numbers[mid]>x:
            end=mid-1
        else:
            start=mid+1
    
    if found==False:
        print('No')
    


        
