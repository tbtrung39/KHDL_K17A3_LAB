so = input("Nhập một số thập phân: ")
chu_so = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
so_chu = ''
for chu in so:
    if chu.isdigit():
        so_chu += chu_so[int(chu)] + ' '
print("Số", so, "được viết bằng chữ là:", so_chu.strip())