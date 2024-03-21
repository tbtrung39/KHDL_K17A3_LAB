n=int(input('nhap số hàng: '))

print(" "(n-1)+'')
for i in range(1,n-1):
    print(" "(n-i-1)+'',end='')
    print(" "*(2*i-1),end='')
    print("*")
print('*'*(2*n-1))
print('hình 1')

print(" "(n-1)+'')
for i in range(1,n-1):
    print(" "(n-i-1)+'',end='')
    print(" "*(2*i-1),end='')
    print("*")
print('* '*(n))
print('hình 2')

for i in range(n):
    print(' '*(n-i-1),end='')
    print('* '*(i+1),end='')
    print()
print('hình 3')