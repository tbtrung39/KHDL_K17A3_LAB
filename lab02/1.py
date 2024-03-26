month=int(input("Nhap mot thang:"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("Thang",month,"co 31 ngay")
elif month ==2:
    print("Thang",month,"co 28 ngay hoac 29 ngay neu nam nhuan")
elif month==4 or month==6 or month==9 or month==11:
    print("Thang",month,"co 30 ngay")
else:
    print("So thang nhap khong hop le vui long nhap lai")