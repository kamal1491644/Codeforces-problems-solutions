isprime=[]
import math
for i in range(1001):
    isprime.append(True)
isprime[0],isprime[1]=False,False

for i in range(2,int(math.sqrt(1000))):
    if isprime[i]:
        for j in range(i*i,1000,i):
            isprime[j]=False
print(isprime[5],isprime[6])



