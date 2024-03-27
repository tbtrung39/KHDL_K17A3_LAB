print("|____________________________|")
print("|--------MENU ĐỒ UỐNG--------|")
print("|............................|")
print("|1.Cafe                      |")
print("|2.Cam ép                    |")
print("|3.Nước ép cà rốt            |")
print("|4.Nước lọc                  |")
print("|5.Nước Dừa                  |")
print("|____________________________|")
tiep_tuc = 'y'
while tiep_tuc == 'y':
    a = int(input("mời bạn chọn đồ uống (1-5): "))
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
        print("mục bạn chọn không có trong thực đơn. Vui lòng chọn lại.")
    tiep_tuc = input("Bạn có muốn tiếp tục gọi thêm đồ uống không (y/n): ") 
