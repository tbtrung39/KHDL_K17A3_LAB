import random
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Các phần tử của List_:")
for item in List_:
    print(item)
n = List_[2][1]
print("\nPhần tử thứ hai, thuộc vị trí thứ 3 của sublist:", n)
print("\nĐộ dài của List_ trước khi thêm:", len(List_))
ngau_nhien = ["random", random.randint(50, 150)]
List_.append(ngau_nhien)
print("Độ dài của List_ sau khi thêm:", len(List_))
a = [List_[1][1], List_[2][1], List_[5][1], List_[6][1]]
b = sum(a)
print("\nTổng sale value trong ngày thứ hai, thứ ba, thứ bảy, chủ nhật:", b)
