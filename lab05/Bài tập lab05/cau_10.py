str = input("Nhập một chuỗi ký tự nhị phân: ")
binary = True
for char in str:
    if char != "0" and char != "1":
        binary = False
        break
if binary:
    decimal = 0
    power = len(str) - 1
    for i in str:
        decimal += int(i) * (2 ** power)
        power -= 1
    print("Số thập phân tương úng là: ", decimal)
else: 
    print("Chuỗi ký tự bạn nhập không phải là chuỗi nhị phân.")
