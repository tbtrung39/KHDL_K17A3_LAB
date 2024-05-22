import package_3
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
uoc_chung = package_3.so_hoc.ucln(a,b)
boi_chung = package_3.so_hoc.bcnn(a,b)
print(f"Ước chung lớn nhất của hai số {a} và {b} là {uoc_chung}")
print(f"Bội chung nhỏ nhất của hai số {a} và {b} là {boi_chung}")

n = int(input("Nhập số nguyên n: "))
uoc_cua_n,tong_cac_uoc = package_3.so_hoc.sumDivisor(n)
print(f"Các ước của số {n} là {uoc_cua_n}")
print(f"Tổng các ước của số {n} là {tong_cac_uoc}")