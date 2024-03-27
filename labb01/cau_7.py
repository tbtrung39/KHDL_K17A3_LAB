# CÂU 7: VIẾT CHƯƠNG TRÌNH NHẬP VÀO 1 TỌA ĐỘ TRONG KHÔNG GIAN OXYZ. 
# TÍNH TỌA ĐỘ CỦA ĐIỂM ĐỐI XỨNG VỚI NÓ QUA MẶT PHẲNG OXY,OXZ,OYZ
x=int(input('Nhap toa do x: '))
y=int(input('Nhap toa do y: '))
z=int(input('Nhap toa do z: '))
print(f'Toa do diem doi xung qua Oxy la {x,y,-z}')
print(f'Toa do diem doi xung qua Oxz la {x,-y,z}')
print(f'Toa do diem doi xung qua Oyz la {-x,y,z}')