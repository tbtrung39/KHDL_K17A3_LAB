import time
while True:
    print('menu');time.sleep(1);print('1.cafe');print('2.cam vắt');print('3. nước ép cà rốt');print('4.nước lọc');print('5. nước dừa')
    n=int(input('chọn đồ uống(1->5): '))
    while n>5 or n<1:
        n=int(input('vui lòng cho đúng\n : '))
    if n==1:
        print('bạn đã chọn cà phê')
        time.sleep(1.5)
    elif n==2:
        print('bạn đã chọn nước cam vứt')
        time.sleep(1.5)
    elif n==3:
        print('bạn đã chọn nước ép cà dốt')
        time.sleep(1.5)
    elif n==4:
        print('bạn đã chọn nước nọc')
        time.sleep(1.5)
    else:
        print('cảm ơn bạn đã chọn nước rừa')
        time.sleep(1.5)
    print('Vui lòng đánh giá chất lượng của hàng chúng tôi')
    time.sleep(0.5)
    print('1. rất tệ')
    time.sleep(0.5)
    print('2. tệ')
    time.sleep(0.5)
    print('3. bình thường')
    time.sleep(0.5)
    print('4. tốt')
    time.sleep(0.5)
    print('5. rất tốt')
    time.sleep(0.5)
    n=int(input(':'))
    while n<4 or n>5:
        n=int(input('bạn nhập giá trị hông hợp nệ! nhập lại:\n'))
    if n==4:
        print('bạn đã đánh giá tốt!')
    else:
        print('bạn đã đánh giá rất tốt!')
    a=['vui ','lòng ','thanh ','toán ','hóa ','đơn','!\n','của bạn hết ','100000000000000$\n']
    for i in a:
        print(i,end='',flush=True)
        time.sleep(0.7)
    print('cảm ơn bạn đã đến với cửa hàng của tôi!')

    break