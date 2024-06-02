
def sort_numbers(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.readline().strip().split()

    numbers = [int(num) for num in data]

    numbers.sort()

    with open(output_file, 'w') as f:
        for num in numbers:
            f.write(str(num) + ' ')

input_file = 'Inp.txt'
output_file = 'Out.dat'
sort_numbers(input_file, output_file)

print('Đã sắp xếp và ghi dữ liệu vào tập tin Out.dat.')