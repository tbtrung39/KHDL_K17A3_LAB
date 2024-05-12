def tim_ucln(a, b):
    if b == 0:
        return a
    else:
        return tim_ucln(b, a % b)
def tim_ucln_nhieu_so(x):
    if len(x) == 1:
        return x[0]
    else:
        a = x[0]
        b = x[1]
        y = tim_ucln(a, b)
        x[1] = y
        return tim_ucln_nhieu_so(x[1:])
def nhap_nhieu_so():
    n = int(input("Nhập số lượng số: "))
    x = []
    for i in range(n):
        x.append(int(input(f"Nhập số thứ {i+1}: ")))
    return x
x = nhap_nhieu_so()
ucln = tim_ucln_nhieu_so(x)
print(f"Ước chung lớn nhất của các số là: {ucln}")
