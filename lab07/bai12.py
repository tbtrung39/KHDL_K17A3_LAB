while True:
    n = (input("Nhập vào số tự nhiên n: "))
    try:
        if int(n) >0:
            break
        else:
            print("Giá trị không hợp lệ, vui lòng nhập lại")
    except ValueError:
        print("Đây không phải là số tự nhiên, vui lòng nhập lại.")
tu_dien = {}
for i in range(1, (int(n)+1)):
    tu_dien[i] = i*i
print(tu_dien)            