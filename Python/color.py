
            
r,c=map(int,input().split())
string=[]
flag=0
for i in range(c):
    string.append(input())

for i in range(c):
    temp=string[0][-1]
    if string[i][-1]==temp:
        flag+=1
    if 



if flag>=r or flag>=c:
    print('YES')
else:
    print('NO')
        
