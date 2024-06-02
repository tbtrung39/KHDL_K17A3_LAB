from datetime import datetime, timedelta

def get_next_day(day, month, year):
    try:
        # Tạo đối tượng datetime từ ngày, tháng, năm đã cho
        input_date = datetime(year, month, day)
        
        # Thêm một ngày để tìm ngày kế tiếp
        next_date = input_date + timedelta(days=1)
        
        # Trả về ngày kế tiếp dưới dạng chuỗi
        return next_date.strftime("%d/%m/%Y")
    
    except ValueError:
        return "Ngày không hợp lệ. Vui lòng nhập lại."

def main():
    # Nhập vào ngày, tháng, năm từ người dùng
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))
    # Tìm và in ngày kế tiếp
    next_day = get_next_day(day, month, year)
    print("Ngày kế tiếp là:", next_day)

if __name__ == "__main__":
    main()
