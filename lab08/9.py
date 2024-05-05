def cong(a, b):
    return a + b
def tru(a, b):
    return a - b
def nhan(a, b):
    return a * b
def chia(a, b):
    if b == 0:
        return "Không thể chia cho 0."
    else:
        return a / b
try:
    so1 = float(input("Nhập số thứ nhất: "))
    so2 = float(input("Nhập số thứ hai: "))
    print(f"{so1} + {so2} = {cong(so1, so2)}")
    print(f"{so1} - {so2} = {tru(so1, so2)}")
    print(f"{so1} * {so2} = {nhan(so1, so2)}")
    print(f"{so1} / {so2} = {chia(so1, so2)}")
except ValueError:
    print("Vui lòng chỉ nhập số.")
