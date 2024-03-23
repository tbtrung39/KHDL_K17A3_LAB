kw = int(input('Nhap vao mot so:'))
if 0< kw <= 100: 
    don_gia = 2000*kw
    print(f'So tien dien la: {don_gia}')
elif kw <= 200:
    don_gia = 2500*kw
    print(f'So tien dien la: {don_gia}')
elif kw <= 300:
    don_gia = 3000*kw
    print(f'So tien dien la: {don_gia}')
elif kw > 300:
    don_gia = 5000*kw
else:
    print('Khong hop le')