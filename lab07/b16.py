
arr=[int(x) for x in input("Nhập dãy số nguyên, cách nhau bằng dấu phẩy:").split(',')]
cap_chi_so=[]
n=len(arr)
for i in range(n):
    for j in range(i+1, n):
        if arr[i]+1==arr[j]:
            cap_chi_so.append((i, j))
print("Cặp chỉ số (i, j) sao cho a[i]+1 = a[j]:", cap_chi_so)