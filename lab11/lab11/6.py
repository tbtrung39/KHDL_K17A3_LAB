def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def display_line(file_name, line_numbers):
    lines = read_file(file_name)
    for line_number in line_numbers:
        if 0 < line_number <= len(lines):
            print(lines[line_number - 1])

def display_whole_file(file_name):
    lines = read_file(file_name)
    for line in lines:
        print(line.strip())

def find_odd_numbers(file_name):
    lines = read_file(file_name)
    odd_numbers = []
    for line in lines:
        numbers = line.split()
        for number in numbers:
            if int(number) % 2 != 0:
                odd_numbers.append(number)
    return odd_numbers

def write_odd_numbers(file_name, odd_numbers):
    with open(file_name, 'w') as file:
        for i in range(4):
            for j in range(4):
                if len(odd_numbers) > 0:
                    file.write(odd_numbers.pop(0) + ' ')
                else:
                    file.write('0 ')
            file.write('\n')

def display_last_line(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(lines[-1])

# Thực hiện các yêu cầu
input_file = "input.txt"
odd_file = "ODD.txt"

# a. Hiển thị nội dung dòng đầu tiên và dòng thứ 3.
print('dong 1 và dòng 3 lần lượt là:')
display_line(input_file, [1, 3])

# b. Hiển thị nội dung toàn bộ file.
print('toàn bộ nội dung là')
display_whole_file(input_file)

# c. Tìm và ghi các số lẻ vào file ODD.txt
odd_numbers = find_odd_numbers(input_file)
write_odd_numbers(odd_file, odd_numbers)

# d. In ra nội dung dòng cuối của file ODD.txt
print('dòng cuối của file odd là')
display_last_line(odd_file)
