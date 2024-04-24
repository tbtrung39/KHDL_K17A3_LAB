def nhap_so():
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    c = int(input("Nhập số thứ ba: "))
    return a, b, c

def tim_min_max(a, b, c):
    min_val = min(a, b, c)
    max_val = max(a, b, c)
    return min_val, max_val

a,b,c = nhap_so()
min_val,max_val = tim_min_max(a,b,c)
print("Số nhỏ nhất là: ", min_val)
print("Số lớn nhất là: ", max_val)
