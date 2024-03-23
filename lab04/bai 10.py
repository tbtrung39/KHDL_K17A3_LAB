
chu_so=['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
so_thap_phan=input("Nhap mot so thap phan: ")
for chu in so_thap_phan:
    if chu in '0123456789':
        print(chu_so[int(chu)], end=' ')
