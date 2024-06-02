import csv
l=[]
def doc_file(l):
    with open('lab11/files/ds_nhanvien.csv','r',encoding='utf-8') as f:
        data=list(csv.reader(f))
        for i in data:
            l.append(i)
def nhap_thong_tin_hs(l):
    while True:
        Ma_NV=input('nhập mã nhân viên: ').strip().upper()
        Ten_NV=input('nhập tên nhân viên: ').strip().upper()
        Chuc_vu=input('nhập chức vụ: ').strip().upper()
        He_so_luong=float(input('nhập hệ số lương: ').strip())
        l.append([Ma_NV,Ten_NV,Chuc_vu,He_so_luong,None,None,None])
        t=input('tiếp tục nhập(y/n): ').strip().upper()
        if t=='N':
            break
def Tinh_luong(l):
    for i in range(1,len(l)):
        l[i][4]=float(l[i][3])*1490000
        if l[i][2]=="TP":
            l[i][5]=1000000
        if l[i][2]=="PP":
            l[i][5]=700000
        if l[i][2]=="NV":
            l[i][5]=300000
        l[i][6]=float(l[i][4])+float(l[i][5])
def in_danh_sach(l):
    for i in l:
        for j in i:
            print(str(j).ljust(20),end='')
        print()
def sap_xep(l):
    data = [l[0]]+sorted(l[1:],key=lambda x: float(x[-1]),reverse=True)
    for i in data:
        for j in i:
            print(str(j).ljust(20),end='')
        print()
def luu_du_lieu(l):
    with open('lab11/files/ds_nhanvien.csv','w',encoding='utf-8') as file:
        csv.writer(file,lineterminator='\n').writerows(l)
