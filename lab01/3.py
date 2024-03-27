# Nhập vector a từ bàn phím
a = list(map(int, input("Nhập các phần tử của vector a (cách nhau bởi dấu cách): ").split()))

# Nhập vector b từ bàn phím
b = list(map(int, input("Nhập các phần tử của vector b (cách nhau bởi dấu cách): ").split()))

# Tính tích vô hướng của hai vector
tich_vo_huong = sum(ai*bi for ai, bi in zip(a, b))

# In kết quả
print("Tích vô hướng của hai vector là: ",tich_vo_huong )