thu = int(input("Nhập thứ: "))
if thu <1 or thu >7:
    print("Thứ đã nhập không hợp lệ, vui lòng nhập lại")
if thu == 1:
    print("Sunday")
elif thu == 2:
    print("Monday")
elif thu == 3:
    print("Tuesday")        
elif thu == 4:
    print("Wednesday")
elif thu == 5:
    print("Thursday")
elif thu == 6:
    print("Friday")
else:
    print("Saturday")                                                      