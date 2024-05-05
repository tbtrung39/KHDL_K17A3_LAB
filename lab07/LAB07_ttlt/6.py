n = int(input("Nhap vao mot so tu nhien n: "))
a = []
num = 2
while len(a) < n:
    is_a = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_a = False
            break
        