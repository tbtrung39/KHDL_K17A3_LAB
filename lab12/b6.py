def check_username(username):
    if not username.isalnum():
        raise ValueError("Tên nhân viên chỉ được chứa chữ cái và chữ số.")
    return True
def generate_email(username):
    return username + "@companyname.com"
def main():
    emails = []
    while True:
        try:
            username = input("Nhập username của nhân viên (chỉ bao gồm chữ cái và chữ số): ")
            check_username(username)
            email_address = generate_email(username)
            emails.append(email_address)
            print(f"Đã thêm địa chỉ email: {email_address}")
        except ValueError as ve:
            print(f"Lỗi: {ve}")
        choice = input("Bạn có muốn nhập tiếp không? (yes/no): ")
        if choice.lower() != 'yes':
            break
    print("Danh sách địa chỉ email của nhân viên:")
    for email_address in emails:
        print(email_address)

if __name__ == "__main__":
    main()
