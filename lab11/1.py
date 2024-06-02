def read_and_sum_odd_numbers(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        numbers = map(int, content.split())
        sum_of_odds = sum(num for num in numbers if num % 2 != 0)
        return sum_of_odds
    except FileNotFoundError:
        print(f"Tập tin {filename} không tồn tại.")
        return None
    except ValueError:
        print("Tập tin chứa giá trị không phải số nguyên.")
        return None
filename = 'dayso.dat'
sum_of_odds = read_and_sum_odd_numbers(filename)
if sum_of_odds is not None:
    print(f"Tổng các số hạng lẻ trong dãy là: {sum_of_odds}")