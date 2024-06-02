m_content = """1 2 3 4
5 6 7 8
"""
n_content = """3 4 5 6
7 8 9 10
"""
with open('m_nums.txt', 'w') as file:
    file.write(m_content)
with open('n_nums.txt', 'w') as file:
    file.write(n_content)
def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.extend(map(int, line.split()))
    return numbers
m_numbers = read_numbers_from_file('m_nums.txt')
n_numbers = read_numbers_from_file('n_nums.txt')
common_numbers = set(m_numbers).intersection(n_numbers)
with open('so_chung.txt', 'w') as file:
    for num in sorted(common_numbers):
        file.write(f"{num}\n")
with open('so_chung.txt', 'r') as file:
    print("Nội dung file so_chung.txt:")
    for line in file:
        print(line.strip())
