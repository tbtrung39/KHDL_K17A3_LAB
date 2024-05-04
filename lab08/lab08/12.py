def nhap_thong_tin():
    ho_ten = input("Nhập họ và tên của nhân viên: ")
    que_quan = input("Nhập quê quán của nhân viên: ")
    nam_cong_tac = int(input("Nhập số năm công tác của nhân viên: "))
    return ho_ten, que_quan, nam_cong_tac
def tinh_luong(nam_cong_tac):
    luong_co_ban = 10000000 
    phu_cap = 700000 * nam_cong_tac 
    return luong_co_ban + phu_cap
def xuat_thong_tin(ho_ten, que_quan, nam_cong_tac, luong):
    print("Thông tin nhân viên:")
    print("Họ và tên:", ho_ten)
    print("Quê quán:", que_quan)
    print("Thâm niên công tác:", nam_cong_tac, "năm")
    print("Lương:", luong, "VNĐ")
def main():
    ho_ten, que_quan, nam_cong_tac = nhap_thong_tin()
    luong = tinh_luong(nam_cong_tac)
    xuat_thong_tin(ho_ten, que_quan, nam_cong_tac, luong)
if __name__ == "__main__":
    main()
