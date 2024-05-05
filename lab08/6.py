def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def tim_bcnn(a, b):
    return (a * b) // tim_ucln(a, b)

try:
    num1 = int(input("Nhập số nguyên a: "))
    num2 = int(input("Nhập số nguyên b: "))
    
    bcnn = tim_bcnn(num1, num2)
    print(f"Bội chung nhỏ nhất của {num1} và {num2} là {bcnn}")
except ValueError:
    print("Vui lòng chỉ nhập số nguyên.")
