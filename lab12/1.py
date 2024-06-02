def kiem_tra_tam_giac(a,b,c):
    return a + b > c and b + c > a and a + c > b

def dien_tich_tam_giac(a,b,c):
    p = (a+b+c)/2
    dien_tich = (p*(p-a)*(p-b)*(p-c))**0.5
    return dien_tich
def main():
    try:
        a=input("Do dai canh a la : ")
        b=input("Do dai canh b la : ")
        c=input("Do dai canh c la : ")
        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except ValueError:
            raise ValueError("Cac canh tam giac phai la kieu so ")
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Do dai cac canh tam giac phai la so duong lon hon 0 ")
        if not dien_tich_tam_giac(a,b,c):
            raise ValueError("Ba canh khong the thoa man dieu kien tao thanh tam giac ")
        dien_tich = dien_tich_tam_giac(a,b,c)
        print("Dien tich tam giac la :", dien_tich)
    except ValueError as e :
        print(f"Loi: {e}")
    except Exception as v:
        print(f"Loi: {v}")

main()