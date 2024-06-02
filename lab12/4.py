def read_and_write_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

        with open('copy.dat', 'w') as output:
            output.write(content)

        print('Nội dung đã được sao chép vào copy.dat.')

    except FileNotFoundError:
        print('Lỗi: Không tìm thấy file.')
    except PermissionError:
        print('Lỗi: Không có quyền truy cập file.')
    except IOError as e:
        print(f'Lỗi vào/ra: {e}')
    except Exception as e:
        print(f'Đã xảy ra lỗi: {e}')

file_name = input('Nhập tên file: ')
read_and_write_file(file_name)