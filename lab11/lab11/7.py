def find_common_numbers(file1, file2, output_file):
    # Đọc số từ file 1
    with open(file1, 'r') as f1:
        numbers1 = set(map(int, f1.read().split()))

    # Đọc số từ file 2
    with open(file2, 'r') as f2:
        numbers2 = set(map(int, f2.read().split()))

    # Tìm các số chung
    common_numbers = sorted(list(numbers1.intersection(numbers2)))

    # Ghi các số chung vào file output
    with open(output_file, 'w') as output:
        output.write('\n'.join(map(str, common_numbers)))

    return common_numbers


m_file = "m_nums.txt"
n_file = "n_nums.txt"
output_file = "so_chung.txt"

common_numbers = find_common_numbers(m_file, n_file, output_file)

print("Các số chung là:")
for number in common_numbers:
    print(number)