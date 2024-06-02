from functools import reduce
n=int(input('nhập n:'))
print(reduce(lambda x,y: x+y,list(filter(lambda x:x%2==0,range(1,n+1)))))