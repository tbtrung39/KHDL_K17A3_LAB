def find_local_extremes(n):
    extremes = []
    for i in range(1, len(n) - 1):
        if (n[i-1] < n[i] > n[i+1]) or (n[i-1] > n[i] < n[i+1]):
            extremes.append(n[i])

    return extremes

def main():
    input_file = 'f_in.dat'
    output_file = 'outt.dat'
    try:
        sample_data = "3 1 4 1 5 9 2 6 5 3"
        with open(input_file, 'w') as file:
            file.write(sample_data)
            print(f"Tạo tập tin {input_file} thành công với dữ liệu mẫu: {sample_data}")
        with open(input_file, 'r') as f:
            n = [int(num) for num in f.readline().strip().split()]

        if len(n) < 3:
            print("Dãy số phải có ít nhất 3 phần tử để tìm cực trị.")
            return
        extremes = find_local_extremes(n)
        with open(output_file, 'w') as f:
            f.write(str(len(extremes)) + '\n')
            f.write(' '.join(map(str, extremes)))
            print(f'Đã ghi kết quả vào tập tin {output_file}.')

    except Exception as e:
        print(f"Lỗi không xác định: {e}")

if __name__ == "__main__":
    main()
