
def read_and_write_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
        with open("copy.dat", "w") as output:
            output.write(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error: ", e)
filename = input("Nhập tên file: ")
read_and_write_file(filename)
