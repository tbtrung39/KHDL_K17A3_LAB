import random

def generate_set(size):
    integers = []
    floats = []
    strings = []

    for _ in range(size):
        rand_type = random.choice(['int', 'float', 'string'])
        if rand_type == 'int':
            integers.append(random.randint(1, 100))
        elif rand_type == 'float':
            floats.append(round(random.uniform(1, 100), 2))
        else:
            strings.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 10))))

    return integers, floats, strings

def count_elements(integers, floats, strings):
    int_count = len(integers)
    float_count = len(floats)
    string_count = len(strings)
    return int_count, float_count, string_count

# Số lượng phần tử trong tập hợp
size = 20

# Sinh tập hợp
integers, floats, strings = generate_set(size)

# Đếm số lượng các phần tử
int_count, float_count, string_count = count_elements(integers, floats, strings)

# Hiển thị kết quả
print("Số lượng số nguyên:", int_count)
print("Số lượng số thực:", float_count)
print("Số lượng chuỗi kí tự:", string_count)
