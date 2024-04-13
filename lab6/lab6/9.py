while True:
    number = input("Nhập số: ")
    if number.upper()== 'ESC':
        break
    assert int(number) % 2 ==0, "Số nhập vào là số chẵn"
print("Tất cả các số được nhập là số chẵn")