def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(num.strip()) for num in file.readlines()]
    return numbers

def find_common_numbers(file1_numbers, file2_numbers):
    common_numbers = set(file1_numbers) & set(file2_numbers)
    return common_numbers

def write_common_numbers_to_file(common_numbers):
    with open('so_chung.txt', 'w') as file:
        for num in common_numbers:
            file.write(str(num) + '\n')

def print_file_content(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

def main():
    file1_numbers = read_numbers_from_file('D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\\lab11\\mnums.txt')
    file2_numbers = read_numbers_from_file('D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\\lab11\\nnums.txt')
    
    common_numbers = find_common_numbers(file1_numbers, file2_numbers)
    
    write_common_numbers_to_file(common_numbers)
    
    print('Các số chung đã được ghi vào file so_chung.txt và là:')
    print_file_content('D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\\lab11\\so_chung.txt')

if __name__ == '__main__':
    main()