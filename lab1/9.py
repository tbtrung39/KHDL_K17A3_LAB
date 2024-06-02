n=int(input("nhập số lần ="))
# khả năng tung xúc xắc không ra 6 là 
x=(5/6)**n
# khả năng tung ra 6 là
y= 1-x
l_t = round(y,2)
print("xác xuất tung  ",n,"lần được 3 con 6 là",l_t)