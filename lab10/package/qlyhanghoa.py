def nhap_thong_tin(a):
    a.append(['mã hàng', 'tên hàng', 'đơn vị tính', 'đơn giá', 'số lượng', 'thành tiền', 'thuế VAT'])
    while True:
        while True:
            mh = input('nhập mã hàng: ').strip()
            if len(mh)==4:
                break
        ten_h= input('nhập tên hàng: ').strip()
        don_vi_tinh = input('nhập đơn vị tính: ').strip()
        don_gia = float(input('nhập đơn giá: '))
        so_luong = int(input('nhập số lượng: '))
        a.append([mh,ten_h,don_vi_tinh,don_gia,so_luong])
        t=input('tiếp tục không?(y/n): ').strip().lower()
        if t=='n': break
def tinh_cot_thanh_tien(a):
    for i in range(1,len(a)):
        a[i].append(a[i][3]*a[i][4])
def Thue(a):
    for i in range(1,len(a)):
        a[i].append(a[i][5]*(1/10))
        print(a[i])
def sap_xep(a):
    print('trước khi sắp xếp:')
    for i in range(len(a)):
        for j in a[i]:
            print(str(j).ljust(15),end='')
        print()
    print('danh sách sau khi sắp xếp:')
    b = [a[0]]+sorted(a[1:],key = lambda x: x[5],reverse= True)
    for i in b:
        for j in i:
            print(str(j).ljust(15),end='')
        print()