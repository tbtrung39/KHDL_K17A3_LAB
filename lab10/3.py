from package.sohoc import ucln, bcnn, sumdivisor
x = [(48, 18), (7, 5), (0, 5), (100, 25)]

for a, b in x:
    print(f"Ước chung lớn nhất của {a} và {b}: {ucln(a, b)}")
    print(f"Bội chung nhỏ nhất của {a} và {b}: {bcnn(a, b)}")
y = [6, 12, 15, -5]

for n in y:
    result = sumdivisor(n)
    if result is not None:
        print(f"Tổng các ước của {n}: {result}")
    else:
        print(f"Số {n} không hợp lệ để tính tổng các ước")
