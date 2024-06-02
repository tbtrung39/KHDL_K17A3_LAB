def nguoi_dung(username):
    if not username.isalnum():
        raise ValueError("Tên nhân viên chỉ được chứa chữ cái và chữ số.")
    return True
def email(username):
    return username + "@companyname.com"
def main():
    emails = []
    while True:
        try:
            username = input("Nhập username của nhân viên (chỉ bao gồm chữ cái và chữ số): ")
            nguoi_dung(username)
            email = email(username)
            emails.append(email)
            print(f"Đã thêm địa chỉ email: {email}")
        except ValueError as ve:
            print(f"Lỗi: {ve}")
        choice = input("Bạn có muốn nhập tiếp không? (yes/no): ")
        if choice.lower() != 'yes':
            break
    print("Danh sách địa chỉ email của nhân viên:")
    for email in emails:
        print(email)
if __name__ == "__main__":
    main()