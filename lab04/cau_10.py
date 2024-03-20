def convert_number_to_words(number):
    # Dictionary chứa các từ tương ứng với các chữ số
    words_dict = {
        '0': 'không',
        '1': 'một',
        '2': 'hai',
        '3': 'ba',
        '4': 'bốn',
        '5': 'năm',
        '6': 'sáu',
        '7': 'bảy',
        '8': 'tám',
        '9': 'chín'
    }
    
    # Chuyển số thành chuỗi và chia thành từng chữ số
    digits = str(number)
    
    # In ra từng chữ số tương ứng
    for digit in digits:
        print(words_dict[digit], end=' ')

def main():
    number = input("Nhập một số thập phân: ")
    
    # Kiểm tra xem số nhập vào có phải là một số thập phân hợp lệ không
    if number.isdigit():
        convert_number_to_words(number)
    else:
        print("Số bạn nhập không hợp lệ!")

if __name__ == "__main__":
    main()
