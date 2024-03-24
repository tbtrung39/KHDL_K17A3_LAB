ngay=int(input("Nhập ngày:"))
thang=int(input("Nhập tháng:"))
nam=int(input("Nhập năm:"))
if ngay < 0 or ngay > 31 or thang < 0 or thang > 12 or nam < 0:
    print("Kiểm tra lại ")
else:
    if thang == 2:
        if ngay < 28 :
            ngay+=1
        elif ngay == 28:
            thang = 3
            ngay = 1
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11 :
        if ngay < 30:
            ngay+=1
        else:
            ngay=1
            thang+=1
    else:
        if ngay < 31:
            ngay+=1
        else:
            ngay=1
            thang+=1
print(f"Ngày tiếp theo là:{ngay}/{thang}/{nam} ")
        
    

