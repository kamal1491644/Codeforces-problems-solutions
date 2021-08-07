n,k,a=map(int,input().split())

res=(n*k)/a
check_float=isinstance(res,float)
if res<-2147483648 or res>2147483647:
    print('long long')
elif res>=-2147483648 or res<=2147483647:
    print('int')
elif check_float:
    print('double')

print(res)
