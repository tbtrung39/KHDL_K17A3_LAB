def dao_nguoc_so(n, so_dao_nguoc=0):
    if n == 0:
        return so_dao_nguoc
    else:
        x = n % 10  
        so_dao_nguoc = (so_dao_nguoc * 10) + x  
        return dao_nguoc_so(n // 10, so_dao_nguoc)  
so = int(input("Nhập một số nguyên dương: "))
a = dao_nguoc_so(so)
print(f"Số {so} sau khi đảo ngược là: {a}")
