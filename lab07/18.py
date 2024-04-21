# Tạo từ điển lưu trữ thông tin thí sinh
student_dict = {
    "123456": {"name": "Nguyễn Văn A", "score": 85},
    "789012": {"name": "Trần Thị B", "score": 92},
    "345678": {"name": "Lê Hồng C", "score": 78}
}

# Nhập số báo danh từ người dùng
registration_number = input("Nhập số báo danh: ")

# Kiểm tra xem số báo danh có trong từ điển không
if registration_number in student_dict:
    # Nếu có, in ra họ tên và điểm thi
    print(f"Họ và tên: {student_dict[registration_number]['name']}")
    print(f"Điểm thi: {student_dict[registration_number]['score']}")
else:
    # Nếu không có, yêu cầu người dùng nhập thông tin mới và thêm vào từ điển
    name = input("Nhập họ và tên: ")
    score = int(input("Nhập điểm thi: "))
    student_dict[registration_number] = {"name": name, "score": score}
    print("Thông tin thí sinh đã được thêm vào từ điển.")

# In ra toàn bộ thông tin trong từ điển sau khi cập nhật
print(student_dict)