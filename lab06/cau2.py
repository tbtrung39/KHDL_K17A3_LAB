
n=int(input('nhap só phần tử: '))
a=[]
for i in range(n):
    a.append(int(input(f'nhap so tu nhien vị trí số {i+1}: ')))
b=sorted(a,reverse=True)
print(f'phần tử lớn thứ 2 trong danh sách là {b[1]} và vị trí của phần tử lớn thứ 2 trong danh sách là: {a.index(b[1])}')
so_luong_lien_tiep=0
max_so_luong_lien_tiep=0
for i in a:
    if i>0:
        so_luong_lien_tiep+=1
        max_so_luong_lien_tiep=max(so_luong_lien_tiep,max_so_luong_lien_tiep)
    else:
        so_luong_lien_tiep=0
print(f'so luong so duong lien tiếp lớn nhất trong danh sách là: {max_so_luong_lien_tiep}' )

so_luong_lien_tiep=0
max_so_luong_lien_tiep=0
tong_max=0
tong_ht=0
for i in a:
    if i > 0:
        so_luong_lien_tiep+=1
        tong_ht+=i
        if tong_ht>tong_max:
            tong_max=tong_ht
            max_so_luong_lien_tiep=so_luong_lien_tiep
    else:
        so_luong_lien_tiep=0
        tong_ht=0
print(f'số lượng số dương liên tiếp có tổng lớn nhất là: {max_so_luong_lien_tiep}')