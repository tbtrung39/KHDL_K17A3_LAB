def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_uoc_so_nguyen_to(n):
    uoc_so_nguyen_to = []
    for i in range(2, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            uoc_so_nguyen_to.append(i)
    return uoc_so_nguyen_to

def doc_so_tu_tap_tin(ten_tap_tin):
    try:
        with open(ten_tap_tin, 'r') as file:
            lines = file.readlines()
        numbers = [int(line.strip()) for line in lines]
        return numbers
    except FileNotFoundError:
        print(f"Tập tin {ten_tap_tin} không tồn tại.")
        return []
    except ValueError:
        print("Tập tin chứa giá trị không phải là số nguyên.")
        return []

def ghi_uoc_so_vao_tap_tin(ten_tap_tin, uoc_so_nguyen_to_list):
    with open(ten_tap_tin, 'w') as file:
        for uoc_so_nguyen_to in uoc_so_nguyen_to_list:
            file.write(' '.join(map(str, uoc_so_nguyen_to)) + '\n')
ten_tap_tin_vao = 'f_in.dat'
ten_tap_tin_ra = 'f_out.dat'
numbers = doc_so_tu_tap_tin(ten_tap_tin_vao)

if numbers:
    uoc_so_nguyen_to_list = [tim_uoc_so_nguyen_to(number) for number in numbers]
    ghi_uoc_so_vao_tap_tin(ten_tap_tin_ra, uoc_so_nguyen_to_list)