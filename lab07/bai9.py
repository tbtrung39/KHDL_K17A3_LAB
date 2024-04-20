n = int(input("Nhap mot so tu nhien n la :"))
A = set()
B = set()

for i in range(1, n):
    if n % i == 0:
        A.add(i)
    else:
        B.add(i)
print("Tập hợp của A là : ", A)
print("Tập hợp của B là : ", B)