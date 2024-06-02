
numbers = []
while True:
    try:
        num = int(input("Nhập số tự nhiên (nhập 0 để dừng): "))
        if num == 0:
            break
        elif num < 0:
            print("Vui lòng nhập số tự nhiên dương.")
        else:
            numbers.append(num)
    except ValueError:
        print("Vui lòng nhập một số tự nhiên hợp lệ.")

#
m = int(input('nhap so m :'))
numbers.append(0,m) # chèn vào đâu danh sách 
numbers.append(m) # chèn vào cuối danh sách
print('danh sach sau khi chen :',numbers)




