n = int(input("Nhập vào một số nguyên dương: "))
while n <= 0:
    n = int(input("Số bạn nhập không hợp lệ. Vui lòng nhập lại: "))

S = 0
i = 1
while i <= n:
    if i%2==0:
        S -= 1/i
        i += 1
    else:
        S+=1/i
        i+=1

print(f"S_a = {S}")


#b
S = 0
i = 1
while i <= n:
    S += 1/(i*(i+1))
    i += 1

print(f"S_b = {S}")


#c
S = 0
i = 2
while i <= n:
    S +=1/i**(1/2)
    i += 1

print(f"S_c = {S}")
