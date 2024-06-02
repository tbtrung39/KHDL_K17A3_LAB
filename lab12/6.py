def validate_username(username):
    if not username.isalnum():
        raise ValueError("Tên nhân viên không hợp lệ. Tên chỉ chứa chữ cái và số, không có dấu cách")
    return True
def generate_email(username):
    return f"{username}@companyname.com"
def main():
    emails = []
    while True:
        try:
            username = input("Nhập tên nhân viên: ")
            validate_username(username)
            email = generate_email(username)
            emails.append(email)
            print(f"Email của nhân viên là: {email}")
        except ValueError as ve:
            print(f"Lỗi: {ve}")
        finally:
            tiep_tuc = input("Bạn có muốn nhập tiếp không? (c/k): ")
            if tiep_tuc.lower() != 'c':
                break
    print("Danh sách email của nhân viên:")
    for email in emails:
        print(email)
main()