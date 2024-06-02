import os
def create_sample_file(file_path):
    sample_content = """1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
"""
    with open(file_path, 'w') as file:
        file.write(sample_content)

def sum_odd_numbers(file_name):
    total = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:
                numbers = line.strip().split()
                for num in numbers:
                    try:
                        num = int(num)
                        if num % 2 != 0:
                            total += num
                    except ValueError:
                        print(f"Lỗi: '{num}' không phải là một số nguyên.")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{file_name}'.")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None
    return total
def main():
    file_name = 'dayso.dat'
    create_sample_file(file_name)
    odd_sum = sum_odd_numbers(file_name)
    if odd_sum is not None:
        print(f'Tổng các số hạng lẻ trong dãy số là: {odd_sum}')

if __name__ == "__main__":
    main()
