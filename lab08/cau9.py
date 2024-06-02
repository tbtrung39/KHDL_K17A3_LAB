def sum_of_nums(x,y):
    return x+y
def subtraction_of_nums(x,y):
    return x-y
def division_of_nums(x,y):
    return x/y
def multiplication_of_nums(x,y):
    return x*y

a = int(input("Nhập số thứ 1: "))
b = int(input("Nhập số thứ 2: "))
print("Tổng 2 số là: ", sum_of_nums(a,b))
print("Hiệu 2 số là: ", subtraction_of_nums(a,b))
print("Tích 2 số là: ", multiplication_of_nums(a,b))
print("Thương 2 số là: ", division_of_nums(a,b))