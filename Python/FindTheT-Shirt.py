def binary_search(arr, x,I):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if x>=arr[mid]:
            low=mid+1
            ans=mid
        else:
            high=mid-1
            
        
    return ans-I
 
n=int(input())
numbers=list(map(int,input().split()))
q=int(input())
 
for i in range(q):
    I,P=map(int,input().split())
    maxi=numbers[I-1]+P
    if maxi>=numbers[-1]:
        print(n-I)
    else:
        ans=binary_search(numbers,maxi,I-1)
        print(ans) 
