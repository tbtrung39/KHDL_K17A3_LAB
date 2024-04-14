a = int(input("Nhap gia tri a:"))
b = int(input("Nhap gia tri b:"))
mang = [[i * j for j in range (b)] for i in range(a)]
print("ket qua la:", mang)
