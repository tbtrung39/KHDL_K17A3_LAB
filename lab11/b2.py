import os
def sort_numbers(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.readline().strip().split()
    numbers = [int(num) for num in data]
    numbers.sort()
    with open(output_file, 'w') as f:
        for num in numbers:
            f.write(str(num) + ' ')
    print(f'Dữ liệu đã được sắp xếp và ghi vào tập tin {output_file}.')
def main():
    input_file = 'inp.txt'
    output_file = 'out.dat'
    sample_data = "10 3 5 8 6 2 7 1 4 9"
    with open(input_file, 'w') as file:
        file.write(sample_data)
    sort_numbers(input_file, output_file)
    with open(output_file, 'r') as file:
        sorted_data = file.read().strip()
        print(f'Nội dung tập tin {output_file}: {sorted_data}')

if __name__ == "__main__":
    main()
