#a
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
tong= sum(a)
print("Tong cac phan tu cua danh sach a la", tong)
#b
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
so_hang_duong = len([x for x in a if x>0])
tong_cac_so_hang_duong = sum([x for x in a if x>0])
print("so luong cac so hang duong:", so_hang_duong)
print("tong cac so hang duong :", tong_cac_so_hang_duong)
#c
def tim_vi_tri_am(a):
    vi_tri_am = [i for i, num in enumerate(a) if num <0 ]
    return vi_tri_am
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
vi_tri_am = tim_vi_tri_am(a)
print("Vi tri cua phan tu am trong danh sach la:", vi_tri_am)
#d
def tim_vi_tri_duong(a):
    vi_tri_duong = [i for i, num in enumerate(a) if num >0 ]
    return vi_tri_duong
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
vi_tri_duong = tim_vi_tri_duong(a)
print("Vi tri cua phan tu am trong danh sach la:", vi_tri_duong)
#e
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
max = None
c = None
for i, so in enumerate(a):
    if max is None or so >=max:
        max = so
        c = i
if c is not None:
    print("Phan tu lon nhat cua danh sach la:", max)
    print("vi tri phan tu lon nhat cuoi cung la:", c)
else:
    print("danh sach rong")