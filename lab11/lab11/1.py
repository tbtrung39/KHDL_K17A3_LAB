def is_odd(n):
    """Kiểm tra xem số n có phải là số lẻ hay không."""
    return n % 2 != 0

def sum_odd_numbers_in_file(filename):
    """Đọc các số từ tập tin và tính tổng các số lẻ."""
    total = 0
    
    with open(filename, 'r') as file:
        for line in file:
            # Tách các số từ dòng hiện tại
            numbers = line.split()
            
            # Kiểm tra và tính tổng các số lẻ
            for number in numbers:
                if is_odd(int(number)):
                    total += int(number)
    
    return total

# Đường dẫn tới tập tin
filename = 'dayso.dat'

# Tính tổng các số lẻ trong tập tin
total_sum = sum_odd_numbers_in_file(filename)
print("Tổng các số lẻ trong dãy là:", total_sum)
