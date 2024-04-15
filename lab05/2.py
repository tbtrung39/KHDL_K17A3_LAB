Str = input("nhập 1 chuỗi kí tự: ")
dem = 0
for i in Str:
    if not i.isalpha() and i.isnumeric():
        dem += 1
print(f"có {dem} ký tụe kp là chữ cái TA và kp là số trong chuỗi vừa nhập")

