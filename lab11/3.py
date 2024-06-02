def tim_cuc_tri(numbers):
    n = len(numbers)
    cuc_tri = []
    for i in range(1, n - 1):
        if (numbers[i - 1] < numbers[i] > numbers[i + 1]) or (numbers[i - 1] > numbers[i] <= numbers[i + 1]):
            cuc_tri.append(numbers[i])
    return cuc_tri
def doc_so_tu_tap_tin(ten_tap_tin):
    try:
        with open(ten_tap_tin, 'r') as file:
            noi_dung = file.read()
        numbers = list(map(int, noi_dung.split()))
        return numbers
    except FileNotFoundError:
        print(f"Tập tin {ten_tap_tin} không tồn tại.")
        return []
    except ValueError:
        print("Tập tin chứa giá trị không phải số nguyên.")
        return []

def ghi_cuc_tri_vao_tap_tin(ten_tap_tin, cuc_tri):
    with open(ten_tap_tin, 'w') as file:
        file.write(f"{len(cuc_tri)}\n")
        file.write(' '.join(map(str, cuc_tri)) + '\n')
ten_tap_tin_vao = 'f_in.dat'
ten_tap_tin_ra = 'f_out.dat'
numbers = doc_so_tu_tap_tin(ten_tap_tin_vao)
if numbers:
    cuc_tri = tim_cuc_tri(numbers)  
    ghi_cuc_tri_vao_tap_tin(ten_tap_tin_ra, cuc_tri)