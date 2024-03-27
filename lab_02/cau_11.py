# cho số ngày 1 tháng của năm không nhuận
# thg 1: 31 ngày     thg 4: 30 ngày     thg 7: 31 ngày    thg 10: 31 ngày
# thg 2: 28 ngày     thg 5: 31 ngày     thg 8: 31 ngày    thg 11: 30 ngày
# thg 3: 31 ngày     thg 6: 30 ngày     thg 9: 30 ngày    thg 12: 31 ngày
# hãy viết chương trình xuất ra ngày tiếp theo của 1 ngày cho trước:
a=int(input('nhập ngày:'))
b=int(input('nhập tháng:'))
if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
    if a==31:
        if b==12:
            print('ngày tiếp theo là ngày 1 tháng 1')
        else:
            print(f'ngày tiếp theo là ngày 1 tháng {a+1}')
    else:
        print(f'ngày tiếp theo là ngày {a+1} tháng {b}')
elif b==4 or b==6 or b==9 or b==11:
    if a==30:
        print(f'ngày tiếp theo là ngày 1 tháng {b+1}')
    else:
        print(f'ngày tiếp theo là ngày {a+1} tháng {b}')
elif a==2:
    if a==28:
        print(f'ngày tiếp theo là ngày 1 tháng {b+1}')
    else:
        print(f'ngày tiếp theo là ngày {a+1} tháng {b}')