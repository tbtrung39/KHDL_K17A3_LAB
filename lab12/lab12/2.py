def kiem_tra_chuoi(chuoi):
    # Kiểm tra xem tất cả các ký tự có phải là chữ cái hay không
    if not chuoi.isalpha():
        raise ValueError("Lỗi ký tự !!!")
    # Kiểm tra xem có hai ký tự liên tiếp giống nhau hay không
    for i in range(len(chuoi) - 1):
        if chuoi[i] == chuoi[i + 1]:
            raise ValueError("Lỗi nhập liệu !!!")
    # Kiểm tra xem có bốn ký tự liên tiếp giống nhau hay không
    for i in range(len(chuoi) - 3):
        if chuoi[i] == chuoi[i + 1] == chuoi[i + 2] == chuoi[i + 3]:
            raise ValueError("Lỗi nhập lặp lại !!!")
    # Kiểm tra xem có năm từ giống nhau liên tiếp hay không
    tu = chuoi.split()
    for i in range(len(tu) - 4):
        if tu[i] == tu[i + 1] == tu[i + 2] == tu[i + 3] == tu[i + 4]:
            raise ValueError("Lỗi nhập trùng lặp!!!")

while True:
    try:
        chuoi = input("Nhập một chuỗi: ")
        kiem_tra_chuoi(chuoi)
        print("Chuỗi hợp lệ.")
    except Exception as e:
        print(str(e))