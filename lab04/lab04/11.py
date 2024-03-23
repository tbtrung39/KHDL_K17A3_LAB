while True:
    print("|--------MENU ĐỒ UỐNG--------|")
    print("|1.Cafe                      |")
    print("|2.Cam ép                    |")
    print("|3.Nước ép cà rốt            |")
    print("|4.Nước lọc                  |")
    print("|5.Nước Dừa                  |")
    
    a = int(input('Vui lòng chọn đồ uống: '))
    if a == 1:
        print("bạn đã chọn cafe.")
    elif a == 2:
        print("bạn đã chọn cam ép.")
    elif a == 3:
        print("bạn đã chọn nước ép cà rốt.")
    elif a == 4:
        print("bạn đã chọn nước lọc.")
    elif a == 5:
        print("bạn đã chọn nước dừa.")
    else:
        print("không chọn")
        break