numbers = []

while True:
    try:
        num = float(input("Nhập số (nhập số âm để kết thúc): "))
        if num < 0:
            break
        numbers.append(num)
    except ValueError:
        print("Vui lòng chỉ nhập số.")

if numbers:
    print("Các số bạn đã nhập là:", numbers)
else:
    print("Bạn chưa nhập số nào.")
