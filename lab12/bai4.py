def main():
    try:
        with open("lab12\input.txt", 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        output_file_name = input("Nhập tên tập tin đầu ra: ")
        
        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            output_file.write(content)

        print("Đã sao chép nội dung vào tập tin", output_file_name)

    except FileNotFoundError:
        print("Lỗi: Tập tin đầu vào không tồn tại.")
    except PermissionError:
        print("Lỗi: Không có quyền truy cập vào tập tin.")
    except Exception as e:
        print("Lỗi:", e)

main()