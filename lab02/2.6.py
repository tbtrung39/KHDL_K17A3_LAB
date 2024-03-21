a = int(input("Nhập một số có 3 chữ số: "))
a1 = a//100
a2 = (a//10)%10
a3 = a%10
if a1 == 1:
    a1 = "Một trăm"
elif a1 == 2:
    a1 = "Hai trăm"
elif a1 == 3:
    a1 = "Ba trăm"
elif a1 == 4:
    a1 = "Bốn trăm"
elif a1 == 5:
    a1 = "Năm trăm"
elif a1 == 6:
    a1 = "Sáu trăm"
elif a1 == 7:
    a1 = "Bảy trăm"
elif a1 == 8:
    a1 = "Tám trăm"
elif a1 == 9:
    a1 = "Chín trăm"
if a2 == 1:
    a2 = "Mười"
elif a2 == 2:
    a2 = "Hai mươi"
elif a2 == 3:
    a2 = "Ba mươi"
elif a2 == 4:
    a2 = "Bốn mươi"
elif a2 == 5:
    a2 = "Năm mươi"
elif a2 == 6:
    a2 = "Sáu mươi"
elif a2 == 7:
    a2 = "Bảy mươi"
elif a2 == 8:
    a2 = "Tám mươi"
elif a2 == 9:
    a2 = "Chín mươi"
elif a2 == 0 and a3!=0:
    a2 = "Linh"
if a3 ==1:
    a3 ="Một"
if a3 ==2:
    a3 ="Hai"
if a3 ==3:
    a3 ="Ba"
if a3 ==4:
    a3 ="Bốn"
if a3 ==5:
    a3 ="Năm"
if a3 ==6:
    a3 ="Sáu"
if a3 ==7:
    a3 ="Bảy"
if a3 ==8:
    a3 ="Tám"
if a3 ==9:
    a3 ="Chín"
if a3 ==0:
    a3 =""
print("Cách đọc là:", a1,a2,a3)