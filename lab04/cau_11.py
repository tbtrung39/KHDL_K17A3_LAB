print("-CHỌN ĐỒ UỐNG-")
while True:
    print("-----MENU-----")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("4. Nước dừa")
    print("0. Thoát")
    
    chon = int(input("Mời bạn chọn đồ uống: "))
    if chon == 1:
        print("Bạn đã gọi cafe")
    elif chon == 2:
        print("Bạn đã gọi cam vắt")
    elif chon == 3:
        print("Bạn đã gọi nước ép cà rốt")
    elif chon == 4:
        print("Bạn đã gọi nước lọc") 
    elif chon == 5:
        print("Bạn đã gọi nước dừa")
    elif chon == 0:
        break
    else:
        print("Vui lòng chọn các đồ uống có trong MENU")