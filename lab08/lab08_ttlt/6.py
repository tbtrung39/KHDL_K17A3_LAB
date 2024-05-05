def bnnn(a,b):
    so_max = max(a,b)
    while True:
        if so_max % a==0 and so_max % b==0:
            return so_max
        so_max +=1
a = int(input("Nhap a: "))
b =int(input("Nhap b: "))
ket_qua = bnnn(a,b)
print(f"Boi chung nho nhat cua a va b la {ket_qua}")       
 