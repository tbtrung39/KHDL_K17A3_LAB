def tong(n):
    if n == 0:
        return n
    elif n < 0:
        raise ValueError('Giá trị phải lớn hơn hoặc bằng 0')
    return n + tong(n - 1)

def tong_binh_phuong(a):
    if a == 0:
        return a
    elif a < 0:
        raise ValueError('Giá trị phải lớn hơn hoặc bằng 0')
    return a**2 + tong_binh_phuong(a - 1)

while True:
    try:
        n = int(input('Nhập vào giá trị n: '))
        print("Kết quả của tổng:", tong(n))
        a = int(input('Nhập vào giá trị a: '))
        print("Kết quả của tổng bình phương:", tong_binh_phuong(a))
        break
    except ValueError as ve:
        print(ve)
        print("Vui lòng nhập lại.")