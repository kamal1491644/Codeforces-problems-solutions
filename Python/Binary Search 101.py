a,b,k=map(int,input().split())
arr=range(a,b+1)
start=a
end=b
counter=0
while start<=end:
    counter+=1
    mid=int((start+end)/2)
    if mid==k:
        print(counter)
        break
    elif mid<k:
        start=mid+1
    else:
        end=mid-1
    

