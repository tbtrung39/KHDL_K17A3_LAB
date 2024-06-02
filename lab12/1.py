import math
def ktra_so(n):  # Xử lí ngoại lệ không phải kiểu số
    while True:
        try:
            giá_trị=float(input(n))
            return giá_trị
        except ValueError:
            print("Bạn đã nhập sai! Yêu cầu nhập lại số thực!")
def ktra_dk_so(giá_trị):
        if giá_trị<=0:
            raise ValueError('giá trị phải lớn hớn 0')
        return giá_trị
def ktra_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a
def tinh_dien_tich(a, b, c):  # Tính diện tích tam giác sử dụng công thức Heron
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Nhập độ dài 3 cạnh tam giác
while True:
    try:
        a = ktra_so("Nhập cạnh a: ")
        a = ktra_dk_so(a)

        b = ktra_so("Nhập cạnh b: ")
        b = ktra_dk_so(b)

        c = ktra_so("Nhập cạnh c: ")
        c = ktra_dk_so(c)

        if ktra_tam_giac(a, b, c):
            print(f"Độ dài {a}, {b}, {c} tạo thành một tam giác hợp lệ.")
            dien_tich = tinh_dien_tich(a, b, c)
            print(f"Diện tích của tam giác là: {dien_tich}")
        else:
            print(f"Độ dài {a}, {b}, {c} không tạo thành một tam giác hợp lệ.")
        
        break  # Thoát vòng lặp nếu không có lỗi
    except ValueError as ve:
        print(ve)
        print("Vui lòng nhập lại.")

# Hàm nhập danh sách với xử lý lỗi
def input_list(prompt):
    while True:
        try:
            list_elements = input(prompt).split(",")
            # Loại bỏ khoảng trắng thừa và chuyển các phần tử thành chuỗi
            list_elements = [element.strip() for element in list_elements]
            return list_elements
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")





    




