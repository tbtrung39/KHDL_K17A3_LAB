so = {
    '0': 'không',
    '1': 'một',
    '2': 'hai',
    '3': 'ba',
    '4': 'bốn',
    '5': 'năm',
    '6': 'sáu',
    '7': 'bảy',
    '8': 'tám',
    '9': 'chín'
}
n = input("Nhập một số: ")
i = 0
while i < len(n):
    a = n[i]
    if a in so:
        print(so[a], end=' ')
    i += 1
