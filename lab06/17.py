n=int(input("Nhập số n: "))
ma_tran_don_vi=[]
for i in range(n):
    hang=[]
    for j in range(n):
        if i==j:
            hang.append(1)
    else:
        hang.append(0)
    ma_tran_don_vi.append(hang)
print("Ma trận đơn vị bậc", n, ":")
for hang in ma_tran_don_vi:
    print(hang)