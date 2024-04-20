Numbers = []
A = set()
while True:
    try:
        num = int(input("Nhập một số tự nhiên (ấn 0 để kết thúc): "))
        if num == 0:
            break
        Numbers.append(num)
    except ValueError:
        print("Vui lòng nhập một số tự nhiên.")
A = set(Numbers)
print("Danh sách Numbers:", Numbers)
print("Tập hợp A:", A)