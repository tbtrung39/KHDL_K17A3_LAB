n = int(input("Nhập số phần tử của dãy: "))
ket_qua = 1  
tu_so = 2  
mau_so = 3  
for i in range(2, n + 1):
    tu_so *= (2 * i)  
    mau_so *= (2 * i + 1)  
    ket_qua += tu_so / mau_so  
ket_qua = round(ket_qua, 3)  
print("Kết quả của phép toán là:", ket_qua)