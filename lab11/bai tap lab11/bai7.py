def tim_so_chung(file1, file2, output_file):
    with open(file1, 'r') as f1:
        numbers1 = set(map(int, f1.read().split()))

    with open(file2, 'r') as f2:
        numbers2 = set(map(int, f2.read().split()))

    so_chung = numbers1.intersection(numbers2)

    with open(output_file, 'w') as output:
        for num in sorted(so_chung):
            output.write(str(num) + '\n')

    return so_chung

m_file = "m_nums.txt"
n_file = "n_nums.txt"
output_file = "so_chung.txt"

so_chung = tim_so_chung(m_file, n_file, output_file)
print("Các số chung:", so_chung)
