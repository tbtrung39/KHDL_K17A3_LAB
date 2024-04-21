import random
List_ = [["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
print("Danh sách list là:",List_)
sublist = List_[2]
print("Độ dài của List_ trước khi thêm:", len(List_))
random_sublist = ["random", random.randint(50, 150)]
List_.append(random_sublist)
print("Độ dài của List_ sau khi thêm:", len(List_))
sum = 0
for day in List_:
    if day[0] in ["tue", "wed", "sat", "sun"]:
        sum += day[1]

print("Tổng sale value trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật là:", sum)