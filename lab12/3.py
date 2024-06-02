import sys
import os

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except Exception as e:
        print(f'Lỗi khi đọc file: {e}')
        sys.exit(1)

def write_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f'Lỗi khi ghi file: {e}')
        sys.exit(1)

def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError('Vui lòng cung cấp tên tệp tin.')

        file_name = sys.argv[1]

        if not os.path.exists(file_name):
            raise FileNotFoundError('File không tồn tại.')

        content = read_file(file_name)
        write_file('copy.dat', content)
        print('Nội dung đã được sao chép vào copy.dat.')
    except ValueError as ve:
        print(ve)
    except FileNotFoundError as fnfe:
        print(fnfe)
    except Exception as e:
        print(f'Có lỗi xảy ra: {e}')

if __name__ == '__main__':
    main()