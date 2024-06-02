def check_username(username):
    if username.isalnum():
        return True
    else:
        return False

def generate_email(username):
    if check_username(username):
        return username + "@companyname.com"
    else:
        return "Username không hợp lệ"

def main():
    username = input("Nhập tên người dùng: ")
    if check_username(username):
        email = generate_email(username)
        print("Email: ", email)
    else:
        print("Username không hợp lệ")

main()