def read_and_write_file(input_file, output_file):
    try:
        # Mở tập tin đầu vào để đọc
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Mở tập tin đầu ra để ghi
        with open(output_file, 'w') as outfile:
            outfile.write(content)

        print("Đã đọc và ghi tập tin thành công.")

    except FileNotFoundError:
        print(f"Lỗi: Tập tin '{input_file}' không tồn tại.")
    
    except IOError as e:
        print(f"Lỗi khi thao tác với tập tin: {e}")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Tên của các tập tin
input_file = "input.txt"
output_file = "output.txt"

# Gọi hàm để đọc và ghi tập tin
read_and_write_file(input_file, output_file)
