n=int(input())
names=[]
grades=[]
s=0
for i in range(n):
    name,grade=input().split()
    names.append(name)
    grades.append(int(grade))
letter=input().upper()
for i in range(len(names)):
    if names[i][0]==letter:
        s+=grades[i]

print(s)
    



