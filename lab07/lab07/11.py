a = int(input('Nhập số sinh viên dự thi cho C++: '))
b = int(input('Nhập số sinh viên dự thi cho Java: '))
c = int(input('Nhập số sinh viên dự thi cho Python: '))
n = int(input('Nhập tổng số sinh viên: '))
sv = {i: set() for i in range(1, n + 1)}
for i in range(a, n + 1, 3):
    sv[i].add('C++')
for i in range(b, n + 1, 3):
    sv[i].add('Java')
for i in range(c, n + 1, 3):
    sv[i].add('Python')
cpp = set()
java = set()
python = set()
cpp_java = set()
cpp_python = set()
java_python = set()
all_languages = set()
for student, languages in sv.items():
    if len(languages) == 1:
        if 'C++' in languages:
            cpp.add(student)
        elif 'Java' in languages:
            java.add(student)
        else:
            python.add(student)
    elif len(languages) == 2:
        if 'C++' in languages and 'Java' in languages:
            cpp_java.add(student)
        elif 'C++' in languages and 'Python' in languages:
            cpp_python.add(student)
        else:
            java_python.add(student)
    else:
        all_languages.add(student)
print(f'Sinh viên chỉ dự thi C++: {sorted(cpp)}')
print(f'Sinh viên chỉ dự thi Java: {sorted(java)}')
print(f'Sinh viên chỉ dự thi Python: {sorted(python)}')
print(f'Sinh viên dự thi cả C++ và Java: {sorted(cpp_java)}')
print(f'Sinh viên dự thi cả C++ và Python: {sorted(cpp_python)}')
print(f'Sinh viên dự thi cả Java và Python: {sorted(java_python)}')
print(f'Sinh viên dự thi cả ba ngôn ngữ: {sorted(all_languages)}')