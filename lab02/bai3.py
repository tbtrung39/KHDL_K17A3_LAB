while True:
    day = int(input("Nhập vào thứ (1->7): "))
    if day < 1 or day > 7:
        print("Thứ không hợp lệ. Vui lòng nhập lại.")
    elif day == 1:
        print(f"{day}: Sunday")
    elif day == 2:
        print(f"{day}: Monday")
    elif day == 3:
        print(f"{day}: Tuesday")
    elif day == 4:
        print(f"{day}: Wednesday")
    elif day == 5:
        print(f"{day}: Thursday")
    elif day == 6:
        print(f"{day}: Friday")
    elif day == 7:
        print(f"{day}: Saturday")       
    break