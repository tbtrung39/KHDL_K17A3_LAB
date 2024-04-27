n = int(input("Nhập số lượng phần tử trong danh sách: "))
while n <= 0:
    n = int(input("Số lượng không hợp lệ, vui lòng nhập lại: "))
phan_tu = []    
for i in range (n):
    phan_tu.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
print("Danh sách các phần tử được nhập vào là:",phan_tu)
binh_phuong = list(map(lambda x: x ** 2, phan_tu))
print("Danh sách các phần tử bình phương là:")
print(binh_phuong)    