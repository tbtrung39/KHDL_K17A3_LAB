def check_input():
    try:
        chuoi = input('Nhập chuỗi: ')
        if len(chuoi) == 2 and chuoi[0] == chuoi[1]:
            raise ValueError('Lỗi nhập liệu: Hai ký tự đầu tiên giống nhau.')

        for i in range(len(chuoi)-3):
            if chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3]:
                raise ValueError('Lỗi nhập lặp lại: Có 4 ký tự liên tiếp giống nhau.')
            if i < len(chuoi) - 4 and chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3] == chuoi[i+4]:
                raise ValueError('Lỗi nhập trùng lặp: Có 5 ký tự liên tiếp giống nhau.')
                
        if not chuoi.isalpha():
            raise ValueError('Lỗi ký tự: Chuỗi chỉ được chứa các ký tự chữ cái.')
            
    except ValueError as e:
        print(e)

check_input()
