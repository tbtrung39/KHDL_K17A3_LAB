def kiem_tra_nhuan(nam):
    if (nam%4==0 and nam%100!=0) or (nam%400==0):
        return True
    else:
        return False
def so_ngay_toi_da(thang, nam):
    if thang==2:
        if kiem_tra_nhuan(nam):
            return 29
        else:
            return 28
    elif thang in [4, 6, 9, 11]:
        return 30
    else:
        return 31
nam=int(input("Nhập năm: "))
thang=int(input("Nhập tháng: "))
if kiem_tra_nhuan(nam):
    print("Năm", nam, "là năm nhuận")
else:
    print("Năm", nam, "không phải là năm nhuận")
print("Số ngày tói đa của tháng", thang, "trong năm", nam, "là:", so_ngay_toi_da(thang, nam))
