heights_list = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]

# Tính số lượng sinh viên
num_students = len(heights_list)
print("Số lượng sinh viên trong nhóm:", num_students)

# Tính chiều cao trung bình
avg_height = sum(heights_list) / num_students
print("Chiều cao trung bình của nhóm:", avg_height, "cm")

# Tạo một tập hợp các chiều cao khác nhau
heights_kn = set(heights_list)

heights_counts = {h:heights_list.count(h) for h in heights_kn}

print("Các chiều cao khác nhau và số lượng sinh viên có chiều cao đó: ")

for height, count in heights_counts.items():
    print(f"{height} cm : {count} sinh viên ")

# Tính chiều cao trung bình của nhóm
heights_tb = sum(heights_list) / float(num_students)
print(f"Chiều cao trung bình của nhóm là: {heights_tb} cm")