def max_number(x,y,z):
    return max(x,y,z)
def min_number(x,y,z):
    return min(x,y,z)
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
print("Số lớn nhất trong 3 số là: ", max_number(a,b,c))
print("Số nhỏ nhất trong 3 số là: ", min_number(a,b,c))