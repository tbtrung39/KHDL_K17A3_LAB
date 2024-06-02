with open('lab11\package_1\dayso.dat', 'w') as file:
    so_luong = int(input("Nhập số lượng số hạng của dãy: "))
    print("Nhập các số hạng của dãy:")
    for i in range(so_luong):
        so_hang = int(input())
        file.write(str(so_hang) + '\n')

print("Đã tạo file dayso.dat")

with open('lab11\package_1\dayso.dat', 'r') as file:
    day_so_le = []
    tong_le = 0
    for line in file:
        so_hang = int(line)
        if so_hang % 2 != 0:
            day_so_le.append(so_hang)
            tong_le += so_hang
print("Các số hạng lẻ trong dãy là:",day_so_le)
print("Tổng các số hạng lẻ trong dãy là:", tong_le)