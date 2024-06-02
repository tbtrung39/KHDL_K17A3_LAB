chuoi1 = input("Nhập chuỗi: ")
chuoi2 = input('Nhập chuỗi: ')
do_dai = [[0] * (1 + len(chuoi2)) for _ in range(1 + len(chuoi1))]
do_dai_max = 0
vi_tri_max = 0

for vi_tri1 in range(1, 1 + len(chuoi1)):
    for vi_tri2 in range(1, 1 + len(chuoi2)):
        if chuoi1[vi_tri1 - 1] == chuoi2[vi_tri2 - 1]:
            do_dai[vi_tri1][vi_tri2] = do_dai[vi_tri1 - 1][vi_tri2 - 1] + 1
            if do_dai[vi_tri1][vi_tri2] > do_dai_max:
                do_dai_max = do_dai[vi_tri1][vi_tri2]
                vi_tri_max = vi_tri1
        else:
            do_dai[vi_tri1][vi_tri2] = 0

chuoi_con_chung = chuoi1[vi_tri_max - do_dai_max: vi_tri_max]
print(chuoi_con_chung)  # In ra chuỗi con chung dài nhất
