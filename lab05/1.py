Str = input("nhập 1 chuỗi kí tự: ")
print('Chuỗi ký tự vừa nhâp', Str)
dem=0
for i in Str:
    if "0" <= i <="9":
        dem+=1
print('các ký tự số là số trong chuỗi đã nhập =', dem)
