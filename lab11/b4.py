import math

def find_prime_factors(number):
    factors = []
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

def main():
    input_file = 'D:\THỰC TẬP LẬP TRÌNH\KHDL_K17A3_LAB\lab11\IN.dat'
    output_file = 'D:\THỰC TẬP LẬP TRÌNH\KHDL_K17A3_LAB\lab11\ou.dat'

    try:
        with open(input_file, 'r') as file:
            data = file.readlines()

        results = []

        for line in data:
            number = int(line.strip())
            factors = find_prime_factors(number)
            results.append(factors)

        with open(output_file, 'w') as file:
            for factors in results:
                file.write(' '.join(map(str, factors)) + '\n')

        print(f'Kết quả đã được ghi vào tệp {output_file}.')

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{input_file}'.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

if __name__ == "__main__":
    main()
