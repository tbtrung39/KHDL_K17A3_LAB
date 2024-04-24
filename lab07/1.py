ds= set()
while True:
    a=input("Nhập kí tự lưu vào set():")
    if a == 'ESC':
        break
    ds.add(a)
print("set sau khi nhập dữ liệu là:")
print(ds)
print("Sau khi xoá số là:")
x={i for i in ds if not i.isdigit()} #isdigit kiểm tra thuộc số ko
print(x)