def read_and_sort_numbers(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        numbers = list(map(int, content.split()))
        sorted_numbers = sorted(numbers)
        with open(output_filename, 'w') as outfile:
            outfile.write(' '.join(map(str, sorted_numbers)))

    except FileNotFoundError:
        print(f"Tập tin {input_filename} không tồn tại.")
    except ValueError:
        print("Tập tin chứa giá trị không phải số nguyên.")

input_filename = 'Inp.txt'
output_filename = 'out.dat'
read_and_sort_numbers(input_filename, output_filename)