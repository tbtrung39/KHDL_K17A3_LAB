print('\n\n\t\t==========MENU==========')
print('1. Cafe')
print('2. Cam vắt')
print('3. Nước ép cà rốt')
print('4. Nước lọc')
print('5. Nước dừa')
print('\n\t\t==========END==========')
print('Hãy nhập lựa chọn của bạn (1->4:): ', end='')
lua_chon=int(input())
if lua_chon == 1:
    print('Bạn đã lựa chọn Cafe\n')
elif lua_chon == 2:
    print('Bạn đã lựa chọn cam vắt\n')
elif lua_chon == 3:
    print('Bạn đã lựa chọn nước ép cà rốt\n')
elif lua_chon == 4:
    print('Bạn đã lựa chọn nước lọc\n')
elif lua_chon == 5:
    print('Bạn đã lựa chọn nước dừa\n')
else:
    print('Lựa chọn của bạn không hợp lệ, vui lòng kiểm tra lại')