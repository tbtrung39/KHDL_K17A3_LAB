# câu a
n = int(input("Nhập số: "))
sum = 0
i = 1
while i <=n:
    if i % 2 ==0:
        sum += -i
    if i % 2 !=0:
        sum += i
print("Tổng câu a là: ", sum)
