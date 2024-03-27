n = int(input("nhập số n: "))
if n < 2:
    la_sont = False
else:
    print(f"các số nguyên tố nhỏ hơn hoặc bằng {n} là: ")
    for num in range(2, n+1):
        la_sont = True
        for i in range(2, int(num **0.5)+1):
            if num % i == 0:
                la_sont =False
                break
        if la_sont:
            print(num, end=" ")
