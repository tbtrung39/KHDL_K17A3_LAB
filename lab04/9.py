a = float(input("nhập tử số :"))
b = float(input("nhập mẫu số :"))
while b == 0:
    b = int(input("Giá trị không hợp lệ. Nhập lại b (b > 0 or b < 0): "))
print(f"phân số là :\n{a}\n---\n{b}")