n,m=map(int,input().split())

x,y,l=map(int,input().split())

matrix=[]
temp=[]

for i in range(n):
    matrix.append(list(map(int,input().split())))
    

for i in range(x-1,(x-1)+l):
    for j in range(y-1,(y-1)+l):
        temp.append(matrix[i][j])
print(sum(temp)%m)
