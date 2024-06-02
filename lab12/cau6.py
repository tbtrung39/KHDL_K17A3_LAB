def check_username(username):
    try:
        if username.isalnum():
            return True
        else:
            raise ValueError('Username không hợp lệ.')
    except ValueError as e:
        print(f'Lỗi: {e}')
        return False

def generate_email(username):
    try:
        if check_username(username):
            return username + '@companyname.com'
        else:
            raise ValueError('Username không hợp lệ.')
    except ValueError as e:
        print(f'Lỗi: {e}')
        return None

def main():
    username = input('Nhập tên người dùng: ')
    email = generate_email(username)
    if email:
        print(f'Email: {email}')

main()