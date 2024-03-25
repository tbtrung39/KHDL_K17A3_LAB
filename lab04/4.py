while True:
    tu_so=int(input("Nhập tử số: "))
    mau_so=int(input("Nhập mẫu số: "))
    if mau_so==0:
        print("Mẫu số phải lớn hơn 0.Vui lòng nhập lại!")
    else:
        print(f"Phân số bạn nhập là: {tu_so}/{mau_so}")
        break