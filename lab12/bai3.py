def main():
    file_name = input("Nhập tên tập tin: ")

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()

        with open('lab12\copy.dat', 'w', encoding='utf-8') as copy_file:
            copy_file.write(content)
        print("Đã sao chép nội dung vào tập tin copy.dat.")
    
    except FileNotFoundError:
        print("Lỗi: Tập tin không tồn tại.")
    except Exception as e:
        print(f"Lỗi: {e}")

main()