lst = []
n = int(input("Nhập n phần tử: "))
for i in range(1,n+1):
    if i % 2 !=0:
        lst.append(n)
result_using_map = map(lambda x: x ** 2, lst)      # sử dụng map function và lambda để tạo 1 list chứa các bình phương số lẻ
print(list(result_using_map), "là các bình phương số lẻ")


# cách dùng lambda và filter
square_of_odd_numbers = filter(lambda x: x **2, lst)
print(list(square_of_odd_numbers))