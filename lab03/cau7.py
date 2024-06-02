n = int(input("Nhập số nguyên: "))
sum = 0
if n <0:
    print("Vui lòng nhập lại số nguyên dương")
else:
    for i in range(1,n+1):
        sum += 1/i
print("Tổng nghịch đảo của ", n, "số nguyên đầu tiên là: ", sum)