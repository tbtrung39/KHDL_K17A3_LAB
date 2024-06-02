def cong(a,b):
    return a + b

def tru(a,b):
    return a - b

def nhan(a,b):
    return a * b

def chia(a,b):
    return a / b

a = float(input("Nhap so a :"))
b = float(input("Nhap so b :"))
print("tong :",cong(a,b))
print("hieu :",tru(a,b))
print("tich :",nhan(a,b))
print("thuong :",chia(a,b))