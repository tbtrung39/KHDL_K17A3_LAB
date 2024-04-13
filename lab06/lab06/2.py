n=int(input('Nhập số phần tử: '))
a=[]
for i in range(n):
    a.append(int(input(f'Nhập số tự nhiên vị trí số {i+1}: ')))
b=sorted(a,reverse=True)
print(f'Phần tử lớn thứ 2 trong danh sách là: {b[1]}')
print(f'Vị trí của phần tử lớn thứ 2 trong danh sách là: {a.index(b[1])}')
sl_lien_tiep=0
max_sl_lien_tiep=0
for i in a:
    if i>0:
        sl_lien_tiep+=1
        max_sl_lien_tiep=max(sl_lien_tiep,max_sl_lien_tiep)
    else:
        sl_lien_tiep=0
print(f'so luong so duong lien tiếp lớn nhất trong danh sách là: {max_sl_lien_tiep}' )

sl_lien_tiep=0
max_sl_lien_tiep=0
s=0
tong_ht=0
for i in a:
    if i > 0:
        sl_lien_tiep+=1
        tong_ht+=i
        if tong_ht>s:
            s=tong_ht
            max_sl_lien_tiep=sl_lien_tiep
    else:
        sl_lien_tiep=0
        tong_ht=0
print(f'Số lượng số dương liên tiếp có tổng lớn nhất là: {max_sl_lien_tiep}')