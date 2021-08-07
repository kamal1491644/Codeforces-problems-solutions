entries=list(map(int,input().split()))

k=entries[0]
n=entries[1]
w=entries[2]
s=0
for i in range(1,w+1):
    new=k*i
    s+=new

if n>=s:
    print('0')
else:
    print(s-n)

    
        
    
