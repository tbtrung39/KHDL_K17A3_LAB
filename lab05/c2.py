text = '''
hút thuốc có hại cho sức khỏe
đừng hút thuốc
123456789'''
count = 0
for char in text:
    if 'a' <= char <= 'z' or "A" <= char <= "Z" or char.isnumeric == False:
        count +=1
print("Số kí tự không phải bảng chữ cái tiếng Anh hoặc không phải số là: ", count)