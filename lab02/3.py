thu = int(input("Nhập thứ trong tuần (1-7): "))
if thu < 1 or thu >7:
    print("Thứ không hợp lệ")
else:
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
    elif thu == 7:
        print("Saturday")                   