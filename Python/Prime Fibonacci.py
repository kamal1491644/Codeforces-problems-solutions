import math
fib=[]
fib.append(1)
fib.append(1)

for i in range(2,51):
    fib.append(fib[i-1]+fib[i-2])


prime=[]
for i in fib:
    if i==1:
        prime.append(0)
    elif i==2:
        prime.append(1)
    else:
        flag=False
        for j in range(2,int(math.sqrt(i))):
            if i%j==0:
                prime.append(0)
                flag=True
                break
            
        if not flag:
            prime.append(1)

q=int(input())
for i in range(q):
    number=int(input())
    if prime[number]:
        print('prime')
    else:
        print('not prime')
            
        
        
        
        
    
    
