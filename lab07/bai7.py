input_A = input("Nhập các ký tự và số cho tập hợp A: ")
A = set(input_A)
input_B = input("Nhập các ký tự và số cho tập hợp B: ")
B = set(input_B)
phan_tu_chung = A & B  
print("Các phần tử chung của A và B:",phan_tu_chung)
