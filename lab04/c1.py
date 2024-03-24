# câu a
n = int(input("Nhập số nguyên dương: "))
sum = 0
i = 1
while n <=0:
    print("Hãy nhập lại số nguyên dương")
while i <=n:
    sum += i**2
    i+=1
print("Tổng dãy số câu a là: ", sum)

# câu b
n = int(input("Nhập số nguyên dương: "))
sum = 0
while n <=0:
    print("Hãy nhập lại số nguyên dương")
for i in range(1,n+1,2):
    if i % 2 !=0:
        sum += i**3
    elif i % 2 ==0:
        print("hãy nhập lại số lẻ")
print("Tổng dãy số câu b là: ", sum)

# câu c
n = int(input("Nhập số nguyên dương: "))
sum = 0
while n <=0:
    print("Hãy nhập lại số nguyên dương")
for i in range(1,n+1,2):
    if i % 2 ==0:
        sum += i**4
    elif i % 2 !=0:
        print("hãy nhập lại số chẵn")
print("Tổng dãy số câu b là: ", sum)

