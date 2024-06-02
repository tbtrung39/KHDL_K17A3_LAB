def read_file(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
    return content
def display_first_and_third_lines(content):
    print('Dòng đầu tiên:', content[0].strip())
    print('Dòng thứ ba:', content[2].strip())
def display_file_content(content):
    print('Nội dung toàn bộ file:')
    for line in content:
        print(line.strip())
def find_odd_numbers(content):
    odd_numbers = []
    for line in content:
        numbers = line.strip().split()
        for number in numbers:
            if int(number) % 2 != 0:
                odd_numbers.append(int(number))
    return odd_numbers
def write_odd_numbers_to_file(odd_numbers):
    with open('ODD.txt', 'w') as file:
        for i in range(4):
            for j in range(4):
                if len(odd_numbers) > 0:
                    file.write(str(odd_numbers.pop(0)) + ' ')
                else:
                    file.write('0 ')
            file.write('\n')
def print_last_line_of_odd_file():
    with open('ODD.txt', 'r') as file:
        lines = file.readlines()
        print('Nội dung dòng cuối của file ODD.txt:')
        print(lines[-1].strip())
def main():
    content = read_file('input.txt')
    display_first_and_third_lines(content)
    display_file_content(content)
    odd_numbers = find_odd_numbers(content)
    write_odd_numbers_to_file(odd_numbers)
    print_last_line_of_odd_file()
if __name__ == '__main__':
    main()