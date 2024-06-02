def doc_so(file_name):
    with open(file_name, 'r') as file:
        numbers = {int(num) for num in file.read().split()}
    return numbers
def viet_so(file_name, numbers):
    with open(file_name, 'w') as file:
        for number in sorted(numbers):
            file.write(f"{number}\n")

def noi_dung(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
m_numbers = doc_so('m_nums.txt')
n_numbers = doc_so('n_nums.txt')
common_numbers = m_numbers.intersection(n_numbers)
viet_so('so_chung.txt', common_numbers)
print("Nội dung file so_chung.txt:")
noi_dung('so_chung.txt')
