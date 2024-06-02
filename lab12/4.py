try:
    # Mở tập tin nguồn để đọc
    with open('bt.txt', 'r') as src_file:
        # Đọc nội dung tập tin
        content = src_file.read()

    # Mở tập tin đích để ghi
    with open('b4.txt', 'w') as dest_file:
        # Ghi nội dung vào tập tin đích
        dest_file.write(content)

except IOError as e:
    # Xử lý lỗi mở tập tin
    print("Lỗi mở tập tin:", e)
