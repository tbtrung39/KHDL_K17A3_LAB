def sao_chep_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in:
            with open(output_file, 'w') as f_out:
                for line in f_in:
                    f_out.write(line)
        print(f"Đã sao chép nội dung từ {input_file} vào {output_file} thành công.")
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy tập tin.")
    except PermissionError:
        print("Lỗi: Không thể mở tập tin. Kiểm tra quyền truy cập.")
    except Exception as e:
        print(f"Lỗi: {e}")
def main():
    input_file = input("Nhập tên tập tin vào cần đọc: ")
    output_file = input("Nhập tên tập tin muốn ghi vào: ")
    sao_chep_file(input_file, output_file)
if __name__ == "__main__":
    main()