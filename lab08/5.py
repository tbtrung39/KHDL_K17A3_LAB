def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

try:
    num1 = int(input("Nhập số nguyên a: "))
    num2 = int(input("Nhập số nguyên b: "))
    
    ucln = tim_ucln(num1, num2)
    print(f"Ước chung lớn nhất của {num1} và {num2} là {ucln}")
except ValueError:
    print("Vui lòng chỉ nhập số nguyên.")
