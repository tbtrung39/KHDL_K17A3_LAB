import os
print('\n  CHƯƠNG TRÌNH GỌI THỨC UỐNG. ')
while True:
    #hiển thị menu chọn chức năng
    print(' ___________________________________')
    print("|     Menu chọn chức năng:          |")
    print("|[1] gọi cafe                       |")
    print("|[2] gọi nước cam vắt               |")
    print("|[3] gọi nước ép cà rốt             |")
    print("|[4] gọi nước lọc                   |")
    print("|[5] gọi nước dừa.                  |")
    print("| Bấm số 0 để thoát                 |")
    print(' ___________________________________|')

    chon=int(input('Chọn chức năng cần thức hiện: '))
    if chon ==1:
        print('Bạn đã gọi cafe.')
    elif chon ==2:
        print('Bạn đã gọi nước cam vắt.')
    elif chon ==3:
        print('Bạn đã gọi nước ép cà rốt.')
    elif chon ==4:
        print('Bạn đã nước lọc.')
    elif chon ==5:
        print('Bạn đã nước dừa.')
    elif chon ==0:
        break
    else:
        print('Chỉ chọn trong các số từ 1-5')
        #break
    tt=input('Nhấn phím bất kì để tiếp tục, bấm số 0 để thoát.')