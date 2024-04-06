n = int(input("nhap vao n:"))
if n >= 100:
    hangtram = (n // 100) % 10
    print(f"chu so hang tram cua n la {hangtram}")
else:
    print("ko co chu so hang tram, xuat ra 0")