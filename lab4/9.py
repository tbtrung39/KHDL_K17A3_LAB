n = input("Nhập một số nguyên dương: ")
tong_chu_so = 0

try:
    num = int(n)
    if num <= 0:
        print("Vui lòng nhập một số nguyên dương.")
    else:
        for chu_so in n:
            tong_chu_so += int(chu_so)
        print("Tổng các chữ số của số đã nhập là:", tong_chu_so)
except ValueError:
    print("Vui lòng chỉ nhập số nguyên.")
