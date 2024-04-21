while True:
    n = (input("Nhập vào số tự nhiên n: "))
    try:
        if int(n) >0:
            break
        else:
            print("Giá trị không hợp lệ, vui lòng nhập lại")
    except ValueError:
        print("Đây không phải là số tự nhiên, vui lòng nhập lại.")
        
nguyen_to = []
num = 2
while len(nguyen_to) < int(n):
    isNguyenTo = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            isNguyenTo = False
            break
    if isNguyenTo:
        nguyen_to.append(num)
    num += 1
print("Dãy",n,"số nguyên tố đầu tiên là:",nguyen_to)            