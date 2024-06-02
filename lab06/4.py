
numbers = []
while True:
    try:
        num = int(input("Nhập số tự nhiên (nhập 0 để dừng): "))
        if num == 0:
            break
        elif num < 0:
            print("Vui lòng nhập số tự nhiên dương.")
        else:
            numbers.append(num)
    except ValueError:
        print("Vui lòng nhập một số tự nhiên hợp lệ.")
#                
insert_list = [1, 2, 3]
numbers = insert_list + numbers
numbers += insert_list
print("Danh sách sau khi chèn:", numbers)
#
num_to_remove = int(input("Nhập số cần xóa: "))
if num_to_remove in numbers:
    numbers.remove(num_to_remove)
    print(f"Số {num_to_remove} đã được xóa khỏi danh sách.")
else:
    print(f"Số {num_to_remove} không có trong danh sách.")
print("Danh sách sau khi xóa:", numbers)







