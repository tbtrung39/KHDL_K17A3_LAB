import csv
def nhap_thong_tin(l):
    with open('lab11/files/ds_sinhvien.csv','r',encoding='utf-8') as file:
        data = list(csv.reader(file))
        for i in data:
            l.append(i)
    while True:
        ma_sv=input('mã sinh viên: ').strip()
        ho_ten=input('họ tên: ').strip().upper()
        diem_TB = float(input('điểm trung bình: ').strip())
        diem_RL = int(input('nhập điểm rèn luyện: ').strip())
        l.append([ma_sv,ho_ten,diem_TB,diem_RL,None])
        t=input('tiep tuc(y/n): ').strip().lower()
        if t=='n':
            break
def tinh_diem_tich_luy(l):
    for i in range(1,len(l)):
        l[i][4]=(float(l[i][2])+float(l[i][3]))/2
def doc_duoi_dang_bang_va_luu(l):
    for i in l:
        for j in i:
            print(str(j).ljust(15),end='')
        print()
    with open('lab11/files/ds_sinhvien.csv','w',encoding='utf-8') as file:
        csv.writer(file,lineterminator='\n').writerows(l)
def sap_xep_theo_diem_ren_luyen(l):
    data = [l[0]]+sorted(l[1:],key= lambda x: float(x[3]))
    print('danh sách sau khi sắp xếp')
    for i in data:
        for j in i:
            print(str(j).ljust(15),end='')
        print()
def thong_tin_sinh_vien_co_diem_cao_nhat(l):
    m = 0
    a=[l[0]]
    for i in range(1,len(l)):
        if float(l[i][4])>m:
            m=float(l[i][4])
    for i in range(1,len(l)):
        if float(l[i][4])==m:
            a.append(l[i])
    print('danh sách sinh có điểm cao nhất')
    for i in a:
        for j in i:
            print(str(j).ljust(15),end='')
        print()