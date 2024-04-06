n = int(input("Nhập vào một số nguyên có ba chữ số: "))
hangtram = n // 100
hangchuc = (n % 100) // 10
hangdv = n % 10
ds_chuso = {
    0: 'không',
    1: 'một',
    2: 'hai',
    3: 'ba',
    4: 'bốn',
    5: 'năm',
    6: 'sáu',
    7: 'bảy',
    8: 'tám',
    9: 'chín'
}
print(f"Cách đọc của số {n} là:", end=' ')
print(ds_chuso[hangtram], "trăm", end=' ')

if hangchuc == 1:
    if hangdv == 0:
        print("mười")
    elif hangdv == 5:
        print("mười lăm")
    else:
        print("mười", ds_chuso[hangdv])
elif hangchuc > 1:
    print(ds_chuso[hangchuc], "mươi", end=' ')
    if hangdv > 0:
        print(ds_chuso[hangdv])
else:
    if hangdv != 0:
        print(ds_chuso[hangdv])
    else:
        print(" ")
