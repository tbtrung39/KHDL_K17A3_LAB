tiep_tuc = "y"
dem =0
while tiep_tuc == "y":
    choice = input("Chọn đồ uống: ")
    if choice == "1":
        print("Bạn đã chọn cà phê")
    elif choice == "2":
        print("Bạn đã chọn cam vắt ")
    elif choice == "3":
        print("Bạn đã chọn nước ép cà rốt ") 
    elif choice == "4":
        print("Bạn đã chọn nước lọc ") 
    elif choice == "5":
        print("Bạn đã chọn nước dừa ") 
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại")
    dem+=1  

    tiep_tuc = input("Bạn có muốn tiếp tục gọi thêm đồ uống không (y/n): ")
print("Bạn đã gọi",dem,"đồ uống")                     