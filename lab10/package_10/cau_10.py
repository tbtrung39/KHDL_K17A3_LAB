import package_c10 as b10
def main_b10():
    day = float(input("Nhập cạnh đáy của tam giác: "))
    cao = float(input("Nhập chiều cao của tam giác: "))
    canh1 = float(input("Nhập cạnh 1 của tam giác: "))
    canh2 = float(input("Nhập cạnh 2 của tam giác: "))
    canh3 = float(input("Nhập cạnh 3 của tam giác: "))
    
    dien_tich = b10.dien_tich(day, cao)
    chu_vi = b10.chu_vi(canh1, canh2, canh3)
    
    print(f"Diện tích tam giác: {dien_tich}")
    print(f"Chu vi tam giác: {chu_vi}")

def main_b10():
    canh = float(input("Nhập cạnh của hình vuông: "))
    
    dien_tich = b10.dien_tich(canh)
    chu_vi = b10.chu_vi(canh)
    
    print(f"Diện tích hình vuông: {dien_tich}")
    print(f"Chu vi hình vuông: {chu_vi}")

if __name__ == "__main__":
    print("1. Tính toán tam giác")
    print("2. Tính toán hình vuông")
    lua_chon = input("Chọn tùy chọn (1/2): ")
    
    if lua_chon == "1":
        main_b10()
    elif lua_chon == "2":
        main_b10()
    else:
        print("Lựa chọn không hợp lệ")