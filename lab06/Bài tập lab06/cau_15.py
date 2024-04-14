num_tuples = int(input("Nhập số lượng: "))
tuples_list = []

for i in range(num_tuples):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = float(input("Nhập điểm số: "))
    tuples_list.append((name, age, score))

sorted_tuples = sorted(tuples_list, key=lambda x: (x[0], x[1], x[2]))
print("Danh sách sau khi sắp xếp:")
for tup in sorted_tuples:
    print(tup)
