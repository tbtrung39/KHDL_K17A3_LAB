def read_and_write_file(file_name):
    try:
        with open(file_name, 'r') as file_input:
            content = file_input.read()
        with open('copy.dat', 'w') as file_output:
            file_output.write(content)
        print(f"Đã sao chép nội dung từ '{file_name}' sang 'copy.dat' thành công.")
    except FileNotFoundError:
        print(f"Tập tin '{file_name}' không tồn tại. Không thể sao chép.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    file_name = input("Nhập tên tập tin: ")
    read_and_write_file(file_name)

if __name__ == "__main__":
    main()