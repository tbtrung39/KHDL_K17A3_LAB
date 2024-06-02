
def sort_numbers(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.readline().strip().split()

    numbers = [int(num) for num in data]

    numbers.sort()

    with open(output_file, 'w') as f:
        for num in numbers:
            f.write(str(num) + ' ')

input_file = 'D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\\lab11\\in.txt'
output_file = 'D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\lab11\\out.dat'
sort_numbers(input_file, output_file)

print('Đã sắp xếp và ghi dữ liệu vào tập tin Out.dat.')