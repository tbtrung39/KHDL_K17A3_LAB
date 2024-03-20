n = int(input("Nhập số nguyên dương n: "))
so_hoan_hao = []
for num in range(1,n):
    tong = 0
    for i in range(1, num):
        if num % i == 0 :
            tong +=i
    if tong == num:
        so_hoan_hao.append(num)
print("Các số hoàn hảo nhỏ hơn số",n,"là",so_hoan_hao)