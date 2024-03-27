n = int(input("nhập số n: "))
for num in range(1, n):
    tong = 0
    for i in range(1,num):
        if num % i == 0:
            tong+=i
    if tong == num:
        print(f"các số hoàn hảo nhỏ hơn {n} là: {num}")