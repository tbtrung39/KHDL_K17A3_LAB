# viết chương trình tìm ucln của a,b
def ucln(a,b):
    while b!=0:
        a,b=b,a%b
        return b
x=int(input('nhập vào giá trị x:'))
y=int(input('nhập vào giá trị y:'))
ucln=ucln(x,y)
print(ucln)
