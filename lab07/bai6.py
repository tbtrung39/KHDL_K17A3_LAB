songuyento1=set()
n = int(input("Nhập vào số n: "))

tong = 0
number = 2

while tong < n:
    songuyento = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            songuyento = False
            break
    if songuyento:
        songuyento1.add(number)
        tong += 1
    number += 1
print(songuyento1)