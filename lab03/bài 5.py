# viết chương trình vẽ hình chữ nhật điền dấu * như hình:
'''* * * * * 
   * * * * *
   * * * * * '''
hàng =  3
cột =  5
# dùng vòng lặp lồng
for i in range(hàng):
   for j in range(cột):
        print('*',end = " ")
   print()