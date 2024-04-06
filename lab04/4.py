a = int(input("Nhập tử số của phân số: "))
b = int(input("Nhập mẫu số của phân số: "))
while b == 0:
    print("Mẫu số phải khác 0. Vui lòng nhập lại.")
    b = int(input("Nhập lại mẫu số của phân số: "))
print("Phân số đã nhập là:", a, "/", b)

