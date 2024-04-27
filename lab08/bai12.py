def tinh_luong(luong_co_ban,he_so):
    return luong_co_ban * he_so
def xuat_ket_qua(ho_ten, que_quan,tnct, tong_luong):
    print("Họ và tên: ",ho_ten)
    print("Quê quán: ",que_quan)
    print("Thâm niên công tác: ",tnct)
    print("Lương của nhân viên là: ",tong_luong)
    

ho_ten = input("Nhập họ tên của nhân viên: ")
que_quan = input("Nhập quê quán của nhân viên: ")
tnct = int(input("Nhập thâm niên công tác: "))
luong_co_ban = 10000000
while tnct <0:
    tnct = int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))
he_so = 0
if tnct < 12:
    he_so = 2.34
elif tnct >=12 and tnct <36:
    he_so = 3.33
elif tnct >=36 and tnct <60:
    he_so = 3.66
else:
    he_so = 3.99 
tong_luong = tinh_luong(luong_co_ban,he_so) 
xuat_ket_qua(ho_ten,que_quan,tnct,tong_luong)                      