# câu a
n = int(input("Nhập số nguyên: "))
sum1 = 0
if n <=0:
    print("Hãy nhập lại số nguyên dương")
else:
    for i in range(1,n+1):
        sum1 += i
print("Tổng dãy số câu a là: ", sum1)

# câu b
n = int(input("Nhập số nguyên: "))
sum2 = 0
if n <=0:
    print("Hãy nhập lại số nguyên dương")
else:
    for j in range(1,n+1,2):
        if j % 2 ==0:
            print("Hãy nhập lại số lẻ")
            break
        else:
            sum2 += j
    print("Tổng dãy số câu b là: ", sum2)

#câu c 
n = int(input("Nhập số nguyên: "))
sum3 = 0
if n <=0:
    print("Hãy nhập lại số nguyên dương")
else:
    for h in range(2,n+1,2):
        if h % 2 !=0:
            print("Hãy nhập lại số chẵn")
            break 
        else:
            sum3 += h
    print("Tổng dãy số câu c là: ", sum3)