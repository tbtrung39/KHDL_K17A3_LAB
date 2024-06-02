def find_local_extremes(n):
    extremes = []

    # Xác định các phần tử cực trị
    for i in range(1, len(n) - 1):
        if (n[i-1] < n[i] > n[i+1]) or (n[i-1] > n[i] < n[i+1]):
            extremes.append(n[i])

    return extremes

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        n = [int(num) for num in f.readline().strip().split()]

    extremes = find_local_extremes(n)
    with open(output_file, 'w') as f:
        f.write(str(len(extremes)) + '\n')

        f.write(' '.join(map(str, extremes)))

input_file = 'D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\lab11\\IN.dat'
output_file = 'D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\lab11\\Outt.dat'

main(input_file, output_file)

print('Đã ghi kết quả vào tập tin Outt.dat.')