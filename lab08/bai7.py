def so_lon_nhat(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
def so_nho_nhat(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    elif c<a and c<b:
        return c
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
max_value = so_lon_nhat(a,b,c)
min_value = so_nho_nhat(a,b,c)
print("Số lớn nhất là:",max_value)
print("Số nhỏ nhất là:",min_value)