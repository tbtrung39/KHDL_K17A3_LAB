def file():
    with open('Numbers.txt', 'w') as file:
        file.write("4\n")
        file.write("211 133 180 5\n")
        file.write("192 168 1 254\n")
        file.write("11 1 11 233\n")
def hien_thi(file_name, line_numbers):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for i in line_numbers:
            if 0 <= i < len(lines):
                print(lines[i].strip())
def cac_thu(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
def so(file_name, output_file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    odd_matrix = []
    for line in lines[1:]:  
        numbers = list(map(int, line.split()))
        odd_line = [num if num % 2 != 0 else 0 for num in numbers]
        odd_matrix.append(odd_line)
    
    with open(output_file_name, 'w') as file:
        for line in odd_matrix:
            file.write(' '.join(map(str, line)) + '\n')
def nhieu_thu(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        if lines:
            print(lines[-1].strip())
file()
print("Nội dung dòng đầu tiên và dòng thứ 3:")
hien_thi('Numbers.txt', [0, 2])
print()
print("Nội dung toàn bộ file:")
cac_thu('Numbers.txt')
print()
so('Numbers.txt', 'ODD.txt')
print("Nội dung dòng cuối của file ODD.txt:")
nhieu_thu('ODD.txt')
