import string
def validate_username(username):
    # Kiểm tra xem tên người dùng có hợp lệ không

    valid_chars = set(string.ascii_letters + string.digits)

    if not all(char in valid_chars for char in username):
        raise ValueError("Tên người dùng không hợp lệ. Chỉ được sử dụng chữ cái và chữ số.")

def create_email(username):
    company_domain = "companyname.com"
    return f"{username}@{company_domain}"

def main():
    danh_sach_email = []
    while True:
        try:
            username = input("Nhập tên người dùng (username): ")
            validate_username(username)
            email = create_email(username)
            danh_sach_email.append(email)
            print(f"Đã thêm {email} vào danh sách email.")
        except ValueError as e:
            print(f"Lỗi: {e}")
        finally:
            tiep_tuc = input("Tiếp tục? (y/n): ")
            if tiep_tuc.lower() != "y":
                break

    print("Danh sách email:")
    for email in danh_sach_email:
        print(email)

if __name__ == "__main__":
    main()
