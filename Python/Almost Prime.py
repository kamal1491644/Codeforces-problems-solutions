import math
isprime=[]
def seive(n):
    for i in range(n):
        isprime.append(True)
    isprime[0],isprime[1]=False,False

    for i in range(2,int(math.sqrt(n))):
        if isprime[i]:
            for j in range(i*i,n,i):
                isprime[j]=False
    

n=int(input())
seive(n+3)
divisors=[]
counter2=0
for i in range(1,n+1):
    counter=0
    
    for j in range(2,i):
        if i%j==0:
           if isprime[j]:
               counter+=1
    if counter==2:
        counter2+=1
print(counter2)
        
        
            





                    
    
        
    
    
