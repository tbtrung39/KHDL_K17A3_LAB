try:
    with open('bt.txt', 'r') as src_file:
        content = src_file.read()

    with open('b4.txt', 'w') as dest_file:
        dest_file.write(content)

except IOError as e:
    print("Lỗi mở tập tin:", e)
