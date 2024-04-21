# Nhập số lượng sinh viên tham gia thi ở mỗi ngôn ngữ lập trình
a = int(input("Nhập số lượng sinh viên dự thi C++: "))
b = int(input("Nhập số lượng sinh viên dự thi Java: "))
c = int(input("Nhập số lượng sinh viên dự thi Python: "))

# Nhập danh sách sinh viên tham gia từng ngôn ngữ lập trình
T = [int(x) for x in input("Nhập danh sách sinh viên dự thi C++ (cách nhau bởi dấu cách): ").split()]
K = [int(x) for x in input("Nhập danh sách sinh viên dự thi Java (cách nhau bởi dấu cách): ").split()]
H = [int(x) for x in input("Nhập danh sách sinh viên dự thi Python (cách nhau bởi dấu cách): ").split()]

# Sinh viên chỉ thi một ngôn ngữ lập trình
only_cpp = list(set(T) - set(K) - set(H))
only_java = list(set(K) - set(T) - set(H))
only_python = list(set(H) - set(T) - set(K))

# Sinh viên thi code trên 2 ngôn ngữ lập trình
cpp_and_java = list(set(T) & set(K))
cpp_and_python = list(set(T) & set(H))
java_and_python = list(set(K) & set(H))

# Sinh viên dự thi cả 3 ngôn ngữ lập trình
all_three = list(set(T) & set(K) & set(H))

print("Sinh viên chỉ thi C++:", only_cpp)
print("Sinh viên chỉ thi Java:", only_java)
print("Sinh viên chỉ thi Python:", only_python)
print("Sinh viên thi C++ và Java:", cpp_and_java)
print("Sinh viên thi C++ và Python:", cpp_and_python)
print("Sinh viên thi Java và Python:", java_and_python)
print("Sinh viên dự thi cả 3 ngôn ngữ:", all_three)