# Đọc file m_nums.txt và chuyển đổi nó thành một tập hợp (set) các số nguyên
with open('m_nums.txt', 'r') as file:
    m_nums = set(map(int, file.read().split()))

# Đọc file n_nums.txt và chuyển đổi nó thành một tập hợp (set) các số nguyên
with open('n_nums.txt', 'r') as file:
    n_nums = set(map(int, file.read().split()))

# Tìm giao của hai tập hợp
so_chung = m_nums.intersection(n_nums)

# Ghi kết quả vào file so_chung.txt
with open('so_chung.txt', 'w') as file:
    for num in sorted(so_chung):
        file.write(str(num) + '\n')

# In nội dung của file so_chung.txt
with open('so_chung.txt', 'r') as file:
    print(file.read())
