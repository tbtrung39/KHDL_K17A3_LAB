
# Tam giác cân rỗng
chieu_cao = int(input("Nhập chiều cao của tam giác: "))
for i in range(chieu_cao):
    if i == 0 or i == chieu_cao - 1:
        print(' ' * (chieu_cao - i - 1) + '*' * (2 * i + 1))
    else:
        print(' ' * (chieu_cao - i - 1) + '*' + ' ' * (2 * i - 1) + '*')

# Tam giác đều rỗng
chieu_cao = int(input("Nhập chiều cao của tam giác: "))
for i in range(chieu_cao):
    if i == 0 or i == chieu_cao - 1:
        print(' ' * (chieu_cao - i - 1) + '*' * (2 * i + 1))
    else:
        print(' ' * (chieu_cao - i - 1) + '*' + ' ' * (2 * i - 1) + '*')

# Tam giác đều không rỗng
chieu_cao = int(input("Nhập chiều cao của tam giác: "))
for i in range(chieu_cao):
    print(' ' * (chieu_cao - i - 1) + '* ' * (i + 1))
