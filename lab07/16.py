n = int(input("Nhập số phần tử của dãy số nguyên: "))
a = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(so)
x = []
for i in range(n):
    for j in range(i+1, n):
        if a[j] + 1 == a[i]:
            x.append((i, j))
if len(x) > 0:
    print("Các cặp chỉ số thỏa mãn điều kiện a[j] + 1 = a[i]:")
    for x in x:
        print(x)
else:
    print("Không có cặp chỉ số nào thỏa mãn điều kiện a[j] + 1 = a[i].")
