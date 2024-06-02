def check_input(user_input):
    if not all(char.isalpha() for char in user_input):
        raise ValueError("Lỗi ký tự !!!")
    
    for i in range(len(user_input) - 1):
        if user_input[i] == user_input[i + 1]:
            raise ValueError("Lỗi nhập liệu !!!")
    
    for i in range(len(user_input) - 3):
        if user_input[i] == user_input[i + 1] == user_input[i + 2] == user_input[i + 3]:
            raise ValueError("Lỗi nhập lặp lại !!!")
    
    words = user_input.split()
    for i in range(len(words) - 4):
        if words[i] == words[i + 1] == words[i + 2] == words[i + 3] == words[i + 4]:
            raise ValueError("Lỗi nhập trùng lặp!!!")

def main():
    while True:
        try:
            user_input = input("Nhập chuỗi ký tự: ")
            check_input(user_input)
            print("Chuỗi hợp lệ!")
        except ValueError as e:
            print(e)

main()