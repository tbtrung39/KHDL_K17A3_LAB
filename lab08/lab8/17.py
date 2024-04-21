n=int(input('nhập n:'))
ds=[i for i in range(1,n+1)]
f= list(filter(lambda x: x%2==0,ds))
from functools import reduce as namhandsome
tong = namhandsome(lambda x,y: x+y,f)
print(f'tổng các sổ chẵn trong danh sách đã nhập {tong}')