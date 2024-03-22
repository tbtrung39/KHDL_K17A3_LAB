chu_so = {
    '0': 'không',
    '1': 'một',
    '2': 'hai',
    '3': 'ba',
    '4': 'bốn'
}
so = input("Nhập số: ")
so_chu = ''
i = 0
while i < len(so):
    so_chu += chu_so[so[i]] + ' '
    i += 1
print("Số", so, "bằng chữ là:", so_chu.strip())