n = int(input("Nhập một số nguyên: "))
sum = 0
if n <0:
    print("Hãy nhập lại số nguyên dương")
else:
    for i in range(1,n+1):
        sum += i**3
print("Tổng bậc 3 của ", n, "số nguyên đầu tiên là: ", sum)
