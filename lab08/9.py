def cong(a, b):
    return a+b
def tru(a, b):
    return a-b
def nhan(a, b):
    return a*b 
def chia(a, b):
    if b==0:
        return "Không thể chia 0"
    return a/b 
a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
print("Kết quả của các phép tính: ")
print("a+b", cong(a, b))
print("a-b", tru(a, b))
print("a*b", nhan(a, b))
print("a/b", chia(a, b))


