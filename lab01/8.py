x = float(input("Nhập giá trị của x: "))
if x <= 0:
    print("Vui lòng nhập một số dương.")
else:
    if x == 1:
        log4_x = 0
        logx_2 = 0
    else:
        log4_x = 2 ** (1 / 2)
        logx_2 = 2 ** (1 / x)
    result = log4_x + logx_2
    print("Giá trị của biểu thức f(x) tại x = {} là: {:.2f}".format(x, result))
