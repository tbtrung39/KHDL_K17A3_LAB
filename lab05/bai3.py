so = (input("Nhập vào một số tự nhiên: "))
while float(so)<0:
    so = input("Đây không phải là số tự nhiên, vui lòng nhập lại")
isInt = False    
try:
    int(so)
    isInt = True
except ValueError:
    isInt = False
    
while isInt == False:
    so = (input("Đây không phải là số tự nhiên, vui lòng nhập lại: "))
    try:
        int(so)
        isInt= True
    except ValueError:
        isInt = False
        
nhi_phan = ""

while int(so)>0:
    nhi_phan = str(int(so) % 2) + nhi_phan
    so = int(so) / 2
print("Chuyển số",so,"từ hệ cơ số 10 sang hệ nhị phân là: ",nhi_phan)          