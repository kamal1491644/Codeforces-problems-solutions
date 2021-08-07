def valid(n,row,col):
    if row>=0 and row<=n-1 and col>=0 and col<=n-1:
        return True
    else:
        return False
    
 
 
n=int(input())
 
matrix=[]
shiny=[]
ans=0
 
for i in range(n):
    matrix.append(list(map(int,input().split())))
for i in range(n):
    a=[]
    for j in range(n):
        a.append(False)
    shiny.append(a)
 
 
 
for i in range(n):
    for j in range(n):
        if valid(n,i-1,j) and valid(n,i-1,j-1) and valid(n,i,j-1) and valid(n,i+1,j-1) and valid(n,i+1,j) and valid(n,i+1,j+1) and valid(n,i,j+1) and valid(n,i-1,j+1):
            s=matrix[i-1][j]+matrix[i-1][j-1]+matrix[i][j-1]+matrix[i+1][j-1]+matrix[i+1][j]+matrix[i+1][j+1]+matrix[i][j+1]+matrix[i-1][j+1]
            if matrix[i][j]%2==s%2:
                shiny[i][j]=True
 
for i in range(n):
    for j in range(n):
        if valid(n,i-1,j) and valid(n,i,j-1) and valid(n,i+1,j) and valid(n,i,j+1):
            if shiny[i-1][j] and shiny[i][j-1] and shiny[i+1][j] and shiny[i][j+1]:
                ans+=1
                
            
print(ans)
