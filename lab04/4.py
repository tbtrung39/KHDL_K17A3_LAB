while True:
    tu_so = int(input("Nhập tử số của phân số: "))
    mau_so = int(input("Nhập mẫu số của phân số: "))
    if mau_so != 0:
        break
    else:
        print("Mẫu số không được = 0, nhập lại")
print(f"phân số là {tu_so/mau_so}")