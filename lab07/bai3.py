import random
A = set()
while True:
    n = input("Nhập số lượng phần tử: ")
    try:
        if int(n) > 0:  
            for _ in range(int(n)):
                A.add(random.random())
            break
        else:
            print("Giá trị không hợp lệ, vui lòng nhập một số tự nhiên lớn hơn 0.")
    except ValueError:
        print("Đây không phải là số tự nhiên, vui lòng nhập lại.")

print("Tập hợp A là:", A)
phan_tu_max = max(A)
phan_tu_min = min(A)
tong = sum(A)
print("Phần tử lớn nhất của tập hợp là:",phan_tu_max)
print("Phần tử nhỏ nhất của tập hợp là:",phan_tu_min)
print("Tổng các phần tử của tập hợp là:",tong)

