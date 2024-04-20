def tim_cap_chi_so(a):
    cap_chi_so = []
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] + 1 == a[j]:
                cap_chi_so.append((i, j))
    return cap_chi_so
a = [1, 2, 3, 4,5]
ket_qua = tim_cap_chi_so(a)
print("Các cặp chỉ số thỏa mãn điều kiện là:", ket_qua)
