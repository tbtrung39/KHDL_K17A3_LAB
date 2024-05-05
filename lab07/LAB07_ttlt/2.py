chu_so = []
while True:
    n = int(input("Nhap mot so tu nhien(Nhap enter de dung): "))
    if n == '':
        break
    if n.isdigit():
        chu_so.append(int(n))
    else:
        print('Vui long nhap lai so tu nhien')
A = set(chu_so)

print("Danh sach cac chu so", chu_so)
print("Tap hop A", A)
