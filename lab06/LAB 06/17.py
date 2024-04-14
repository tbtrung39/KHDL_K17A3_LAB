n = int(input("Nhap mot so n: "))
ma_tran =[1 if i==j else 0 for j in range(n) for i in range(n)]
print("Ma tran hang don vi bac la:", n)
for hang in ma_tran:
    print(hang)
    