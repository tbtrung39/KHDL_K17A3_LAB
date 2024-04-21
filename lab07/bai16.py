n = int(input("Nhập số lượng phần tử của mảng: "))
a = list(map(int, input("Nhập các phần tử của mảng (Cách nhau bởi khoảng trắng): ").split()))
if len(a) != n:
    print("Số lượng phần tử không khớp, vui lòng nhập lại!")
else:
    cap_so = []
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + 1 == a[j]:
                cap_so.append((i + 1, j + 1))

    print("Các cặp chỉ số (i, j) sao cho a[i] + 1 = a[j] là:")
    for cap in cap_so:
        print(cap)
