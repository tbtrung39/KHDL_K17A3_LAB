Str = input("Nhập chuỗi: ")
so = ""
for i in Str:
    if "0" <= i <= "9":
        so = so + str(i)
print("Chuỗi số sau khi xóa các ký tự không phải số là: ", so)
n = int(so)
tong = 0
for i in range(1, n):
    if n % i == 0:
        tong += i
if tong == n:
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không phải là số hoàn hảo")
    