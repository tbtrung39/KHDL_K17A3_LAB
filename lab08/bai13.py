def nam_nhuan(nam):
    if nam % 4 == 0 or (nam % 100 !=0 and nam % 400 == 0):
        return True
    else:
        return False
nam = int(input("Nhập vào năm: "))
if nam_nhuan(nam):
    print("Năm",nam,"là năm nhuận")
else:
    print("Năm",nam,"không là năm nhuận")        
def kiem_tra_ngay(thang):
    if thang == 1:
        return 31
    elif thang == 3:
        return 31
    elif thang == 4:
        return 30
    elif thang == 5:
        return 31
    elif thang == 6:
        return 30
    elif thang == 7:
        return 31
    elif thang == 8:
        return 31
    elif thang == 9:
        return 30
    elif thang == 10:
        return 31
    elif thang == 11:
        return 30
    elif thang == 12:
        return 31
    if(nam_nhuan(nam)):
        if thang == 2:
            return 29  
    else:
        if thang == 2:
            return 28
            
thang = int(input("Nhập tháng: "))
while thang <1 or thang >12:
    print("Không có tháng",thang,"trong năm")
    thang = int(input("Vui lòng nhập lại: "))      
print("Số ngày trong tháng",thang,"của năm",nam,"là",kiem_tra_ngay(thang),"ngày") 