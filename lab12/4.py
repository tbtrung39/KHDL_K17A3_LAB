def copy_file(input_file_name, output_file_name):
    try:
        with open(input_file_name, 'r') as input_file:
            content = input_file.read()
        with open(output_file_name, 'w') as output_file:
            output_file.write(content)
        print(f"Sao chép từ '{input_file_name}' sang '{output_file_name}' thành công")
    except FileNotFoundError:
        print(f"Tập tin '{input_file_name}' không tồn tại. Không thể sao chép")
    except PermissionError:
        print(f"Không có quyền ghi vào tập tin '{output_file_name}'. Không thể sao chép")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
    finally:
        if 'input_file' in locals() and not input_file.closed:
            input_file.close()
        if 'output_file' in locals() and not output_file.closed:
            output_file.close()
def main():
    input_file_name = input("Nhập tên tệp tin đầu vào: ")
    output_file_name = input("Nhập tên tệp tin đầu ra: ")
    copy_file(input_file_name, output_file_name)
main()