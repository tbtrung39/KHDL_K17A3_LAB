
a = int(input("Nhập số sinh viên dự thi cho C++: "))
b = int(input("Nhập số sinh viên dự thi cho Java: "))
c = int(input("Nhập số sinh viên dự thi cho Python: "))
n = int(input("Nhập tổng số sinh viên: "))
students = {i: set() for i in range(1, n + 1)}
for i in range(a, n + 1, 3):
    students[i].add("C++")
for i in range(b, n + 1, 3):
    students[i].add("Java")
for i in range(c, n + 1, 3):
    students[i].add("Python")
only_cpp = set()
only_java = set()
only_python = set()
both_cpp_java = set()
both_cpp_python = set()
both_java_python = set()
all_languages = set()
for student, languages in students.items():
    if len(languages) == 1:
        if "C++" in languages:
            only_cpp.add(student)
        elif "Java" in languages:
            only_java.add(student)
        else:
            only_python.add(student)
    elif len(languages) == 2:
        if "C++" in languages and "Java" in languages:
            both_cpp_java.add(student)
        elif "C++" in languages and "Python" in languages:
            both_cpp_python.add(student)
        else:
            both_java_python.add(student)
    else:
        all_languages.add(student)
print("Sinh viên chỉ dự thi C++:", sorted(only_cpp))
print("Sinh viên chỉ dự thi Java:", sorted(only_java))
print("Sinh viên chỉ dự thi Python:", sorted(only_python))
print("Sinh viên dự thi cả C++ và Java:", sorted(both_cpp_java))
print("Sinh viên dự thi cả C++ và Python:", sorted(both_cpp_python))
print("Sinh viên dự thi cả Java và Python:", sorted(both_java_python))
print("Sinh viên dự thi cả ba ngôn ngữ:", sorted(all_languages))
