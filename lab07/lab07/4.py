cc = [161,182,175,173,153,190,182,188,192,140,176,177,150,184,189,180,170,165]
#a
so_luong = len(cc)
print(f'Nhóm có {so_luong} sinh viên.')
#b
tong = sum(cc)
cc_tb=tong/so_luong
print(f'Chiều cao trung bình của các sinh viên trong nhóm là: {cc_tb}')
#c
unique_cc = set(cc)
s = sum(cc)
sx = sorted(unique_cc)
sl = len(cc)
cctb = s/sl 
print('Các chiều cao khác nhau: ')
for cc in sx:
    print(cc)
print(f'Chiều cao trung bình là: {cctb}')