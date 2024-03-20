a=int(input('nhập a:'))
b=int(input('nhập b:'))
c=a
d=b
while b!=0:
    a,b=b,a%b
bcnn=c*d/a
print(f'bội chung nhỏ nhất của {c} và {d} là: {int(bcnn)}')