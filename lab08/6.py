# xây dựng chương trình tìm bội chung nhỏ nhất của 2 số a,b
# tìm bcnn=(a*b)/ucln(a,b)
def ucln(a,b):
    while b!=0:
        a,b=b,a%b
        return b
def bcnn(a,b):
    return (a*b)//(ucln(a,b))
a=int(input('nhập vào a:'))
b=int(input('nhập vào b:'))
print(bcnn(a,b))    