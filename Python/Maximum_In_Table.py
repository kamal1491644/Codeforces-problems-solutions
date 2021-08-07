n=int(input())
matrix=[]
l=[]
for i in range(n):
    new=[]
    for j in range(n):
        new.append(1)
    matrix.append(new)

if len(matrix)==1:
    print(1)
    exit(0)

for i in range(n):
    if i==0:
        continue
    for j in range(n):
        if j==0:
            continue
        matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
        l.append(matrix[i][j])
        
            
print(max(l))


