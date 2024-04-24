def kt_nam(y):
    if y % 4 ==0 and (y%100!=0 or y %400 ==0):
        return f"Năm {y} là năm nhuận"
    else: return f"Năm {y} là năm không nhuận"

def so_ngay_toi_da(m,y):
    if m in [1,3,5,7,8,10,12]:
        return f"Tháng {m} của năm {y} có tối đa 31 ngày"
    elif m in [4,6,9,11]:
        return f"Tháng {m} của năm {y} có tối đa 30 ngày"
    elif m == 2:
        if kt_nam(y):
            return f"Tháng {m} của năm {y} có tối đa 29 ngày"
        else:
            return  f"Tháng {m} của năm {y} có tối đa 28 ngày"
    else:
        return "tháng không hợp lệ"

nam= int(input("nhập năm là: "))
while True:
    thang= int(input("Nhập tháng là: "))
    if 1 <= thang <= 12:
        break
    else:
        print("Tháng không hợp lệ. Vui lòng nhập lại.")
print(kt_nam(nam))
print(so_ngay_toi_da(thang,nam))



    
