day_so=[int(x) for x in input("Nhập dãy số nguyên:").split(',')]
cap_chi_so=[]
n=len(day_so)
for i in range(n):
    for j in range(i+1, n):
        if day_so[i]+1==day_so[j]:
            cap_chi_so.append((i, j))
print("Cặp chỉ số (i, j) sao cho a[i]+1 = a[j]:", cap_chi_so)