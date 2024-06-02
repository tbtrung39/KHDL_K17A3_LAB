def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = file.read().split()
    return set(map(int, numbers))

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

def find_common_numbers():
    numbers1 = read_numbers_from_file('m_nums.txt')
    numbers2 = read_numbers_from_file('n_nums.txt')
    
    common_numbers = numbers1.intersection(numbers2)
    
    write_numbers_to_file('so_chung.txt', common_numbers)
    
    with open('so_chung.txt', 'r') as file:
        print(file.read())

with open('m_nums.txt', 'w') as file:
    file.write('7 8 9 10 12 13 5 ')

with open('n_nums.txt', 'w') as file:
    file.write('7 12 5 6 1 3 4')

find_common_numbers()
