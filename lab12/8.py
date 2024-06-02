def find_previous_day(given_date):
    year, month, day = map(int, given_date.split("-"))
    if day > 1:
        previous_day = f"{year}-{month:02d}-{day - 1:02d}"
    else:
        if month > 1:
            previous_day = f"{year}-{month - 1:02d}-31"
        else:
            previous_day = f"{year - 1}-12-31"
    return previous_day

try:
    input_date_str = input("Nhập ngày (theo định dạng YYYY-MM-DD): ")
    previous_day = find_previous_day(input_date_str)
    print(f"Ngày trước đó của {input_date_str} là {previous_day}.")
except ValueError:
    print("Định dạng ngày không hợp lệ. Vui lòng nhập lại theo định dạng YYYY-MM-DD.")
