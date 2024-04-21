import random

# Tạo mới từ điển
employee_dict = {}

# Thêm nhân viên với các thông tin được nhập từ bàn phím
n = int(input("Nhập số lượng nhân viên: "))
for i in range(n):
    emp_id = ''.join(random.choices('0123456789', k=4))
    emp_name = input(f"Nhập họ tên nhân viên {i+1}: ")
    emp_birth_year = int(input(f"Nhập năm sinh nhân viên {i+1}: "))
    emp_salary = int(input(f"Nhập lương nhân viên {i+1}: "))
    employee_dict[emp_id] = {'name': emp_name, 'birth_year': emp_birth_year, 'salary': emp_salary}

# Tìm kiếm nhân viên với giá trị mã nhân viên là x
x = input("Nhập mã nhân viên cần tìm: ")
if x in employee_dict:
    print(f"Thông tin nhân viên có mã {x}:")
    print(employee_dict[x])
else:
    print(f"Không tìm thấy nhân viên có mã {x}")

# Tăng lương 1000000 cho nhân viên có mã là y
y = input("Nhập mã nhân viên cần tăng lương: ")
if y in employee_dict:
    employee_dict[y]['salary'] += 1000000
    print(f"Đã tăng lương cho nhân viên có mã {y}")
else:
    print(f"Không tìm thấy nhân viên có mã {y}")

# Xóa nhân viên có mã là z
z = input("Nhập mã nhân viên cần xóa: ")
if z in employee_dict:
    del employee_dict[z]
    print(f"Đã xóa nhân viên có mã {z}")
else:
    print(f"Không tìm thấy nhân viên có mã {z}")

# Sắp xếp từ điển giảm dần theo năm sinh
sorted_employees = sorted(employee_dict.items(), key=lambda x: x[1]['birth_year'], reverse=True)
employee_dict = dict(sorted_employees)

# In ra toàn bộ thông tin trong từ điển sau khi cập nhật
print("Danh sách nhân viên sau khi cập nhật:")
for emp_id, emp_info in employee_dict.items():
    print(f"Mã nhân viên: {emp_id}, Họ tên: {emp_info['name']}, Năm sinh: {emp_info['birth_year']}, Lương: {emp_info['salary']}")