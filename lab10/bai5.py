import package_5 
n = (input("Nhập số nguyên n: "))
def isInt(num):
    try:
        if int(num):
            return True
    except ValueError:
        return False
while True:    
    if isInt(n):
        n = int(n)
        print(f"Số vừa nhập là số {n}")    
        co_so_2 = package_5.dcs.nhi_phan(n)
        co_so_8 = package_5.dcs.bat_phan(n)
        co_so_16 = package_5.dcs.thap_luc_phan(n)
        print(f"Số {n} đổi sang cơ số 2 là {co_so_2}")
        print(f"Số {n} đổi sang cơ số 8 là {co_so_8}")
        print(f"Số {n} đổi sang cơ số 16 là {co_so_16}")
        break
    else:
        n = input("Số vừa nhập không hợp lệ, hãy nhập số nguyên: ")
        