while True:
    ki_tu = input("Nhập một ký tự để tìm giá trị ASCII của nó: ")

    if len(ki_tu) == 1:
        ascii= ord(ki_tu)
        print("Giá trị ASCII của ký tự",ki_tu,"là:",ascii)
        break
    else:
        print("Vui lòng nhập đúng một ký tự.")