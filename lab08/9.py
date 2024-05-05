a = float(input("Nhập số a:"))
b = float(input("Nhập số b:"))
def tinh():
    tong = a + b
    print("Tổng của a và b =",tong)
    hieu = a - b
    print("Hiệu của a và b =", hieu)
    tich = a * b
    print("Tích của a và b =", tich)
    thuong = a / b
    print("Thương của a và b =", thuong)
    return tinh

tinh()
