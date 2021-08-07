n=int(input())
ages=list(map(int,input().split()))
x_age=int(input())
ind=[]
for i in range(len(ages)):
    if ages[i]==x_age:
        ind.append(i+1)
        
    else:
        continue

mini=min(ages)
maxi=max(ages)

text=''

for i in ind:
    text+=str(i)+' '
    
text=text.rstrip()
text=text.replace(' ',', ')
if len(ind)==0:
    print('No students are',x_age,'years old.') 
    print('Range:',mini,'to',maxi)
elif len(ind)==1:
    print('Student',text,'is',x_age,'years old.')
    print('Range:',mini,'to',maxi)

    
else:
    print('Students',text,'are',x_age,'years old.')
    print('Range:',mini,'to',maxi)
