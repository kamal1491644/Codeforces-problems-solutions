t=int(input())

for i in range(t):
    counter=0
    n,m=map(int,input().split())
    for i in range(n):
        start,end=input().split()
        startH,startM=start.split(':')
        endH,endM=end.split(':')
        counter+=(((int(endH)*60)+int(endM))  -  ((int(startH)*60)+int(startM)))
    if counter>=(m*60):
        print('YES')
    else:
        print('NO')
    
        
   
