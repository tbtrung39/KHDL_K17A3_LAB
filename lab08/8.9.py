def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    return a / b

so_a = float(input("Nhập số a: "))
so_b = float(input("Nhập số b: "))

print("Kết quả cộng:", cong(so_a, so_b))
print("Kết quả trừ:", tru(so_a, so_b))
print("Kết quả nhân:", nhan(so_a, so_b))
print("Kết quả chia:", chia(so_a, so_b))