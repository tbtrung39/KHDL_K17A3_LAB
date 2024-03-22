n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Số n phải là số nguyên dương. Dừng chương trình.")
else:
    S1 = sum(range(1, n + 1))
    S2 = sum(range(1, 2 * n + 2, 2))
    S3 = sum(range(2, 2 * n + 1, 2))
    print("a) Tổng S1 =", S1)
    print("b) Tổng S2 =", S2)
    print("c) Tổng S3 =", S3)