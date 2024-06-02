def kiem_tra_tam_giac(a,b,c):
    return a+b>c and a+c>b and b+c>a

def dien_tich_tam_giac(a,b,c):
    p = (a+b+c)/2
    dien_tich = (p*(p-a)*(p-b)*(p-c))**0.5
    return dien_tich

def main():
    try:
        a = input("Nhập độ dài cạnh a: ")
        b = input("Nhập độ dài cạnh b: ")
        c = input("Nhập độ dài cạnh c: ")
        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except ValueError:
            raise ValueError("Các cạnh tam giác phải là kiểu số")
        if a <= 0 or b <=0 or c <=0:
            raise ValueError("Độ dài các cạnh tam giác phải là một số dương lớn hơn 0")
        
        if not dien_tich_tam_giac(a,b,c):
            raise ValueError("Ba cạnh không thỏa mãn điều kiện tạo thành một tam giác")
        dien_tich = dien_tich_tam_giac(a,b,c)
        print("Diện tích của tam giác là:",dien_tich)
    except ValueError as v:
        print(f"Lỗi: {v}")
    except Exception as e:
        print(f"Lỗi: {e}")
        
main()           