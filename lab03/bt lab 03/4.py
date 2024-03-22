#Viết chương trình in ra tất cả các số nguyên tố bé hơn hoặc bằng n.
n = int(input("Nhập số nguyên tố n: "))
print("Các số nguyên tố bé hơn hoặc bằng", n, "là:")
for so in range(2, n + 1):
    if all(so % i != 0 for i in range(2, int(so ** 0.5) + 1)):
        print(so)