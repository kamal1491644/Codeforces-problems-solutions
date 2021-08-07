colors=input().upper()
red=0
blue=0
green=0
for i in colors:
    if i=='R':
        red+=1
    elif i =='G':
        green+=1
    elif i=='B':
        blue+=1

print('Red stones =',red)
print('Blue stones =',blue)
print('Green stones =',green)
