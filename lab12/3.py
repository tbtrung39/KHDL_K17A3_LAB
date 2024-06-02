import sys
import os

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def main():
    if len(sys.argv) < 2:
        print("Vui lòng cung cấp tên tệp tin.")
        return

    file_name = sys.argv[1]

    if not os.path.exists(file_name):
        print("File không tồn tại.")
        return

    content = read_file(file_name)
    write_file("copy.dat", content)
    print("Nội dung đã được sao chép vào copy.dat.")

if __name__ == "__main__":
    main()