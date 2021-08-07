w,n=map(int,input().split())
string=input().upper()
new=''
index=list(map(int,input().split()))
for i in range(n):
    new+=string[index[i]-1]

for i in new:
    if i=='E':
        w+=2
        print(w,end=' ')
    elif i=='T':
        w-=1
        print(w,end=' ')

